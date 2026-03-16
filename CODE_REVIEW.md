# CrossPaths — Code Review & Improvement Suggestions

## Summary

The codebase is well-structured for an academic Flask project: clear separation of models, forms, routes, and i18n; safe redirect handling; image validation; and production-aware config. Below are focused improvements to security, maintainability, performance, and robustness.

---

## 1. Security & Configuration

### 1.1 Production: Don’t seed on every gunicorn startup

**Issue:** `wsgi.py` runs `db.create_all()` and `seed_database()` on every worker startup. In production this can cause unnecessary load and, if seed logic changes, inconsistent or duplicate data.

**Suggestion:** Only create tables and seed in production via one-off commands (e.g. release phase or manual):

```python
# wsgi.py — minimal production entry
from app import create_app
app = create_app()
# Rely on Heroku release phase or: flask init-db && flask seed-db
```

Use Heroku’s release phase in `Procfile`:

```
web: gunicorn wsgi:app
release: flask init-db && flask seed-db
```

(Or run `flask init-db` / `flask seed-db` manually after deploy.)

### 1.2 SECRET_KEY

**Good:** You already require `SECRET_KEY` when `FLASK_ENV == 'production'`.

**Suggestion:** Also reject the default dev key in production so it’s never used by mistake:

```python
if not secret_key or secret_key == 'dev-secret-key':
    if os.environ.get('FLASK_ENV') == 'production':
        raise RuntimeError("SECRET_KEY must be set to a non-default value in production.")
if not secret_key:
    secret_key = 'dev-secret-key'
```

### 1.3 set_language: open redirect

**Issue:** `redirect(request.referrer or url_for('main.index'))` can redirect to an external site if `Referer` is from another domain (depending on browser/client). Safer to only redirect to your own paths.

**Suggestion:** Validate that `request.referrer` is from your app (e.g. same host) or ignore it and use a stored “return URL” or always `url_for('main.index')` / the current path.

---

## 2. Routes (`app/routes.py`)

### 2.1 Split the blueprint

**Issue:** One large file with auth, events, communities, and profile is harder to navigate and test.

**Suggestion:** Split into blueprints, e.g.:

- `app/auth.py` — register, login, logout
- `app/events.py` — events list, event detail, create_event
- `app/communities.py` — communities list, detail, join, leave
- `app/profile.py` — profile, edit_profile
- `app/main.py` — index, about, set_language

Register them in `create_app()`. Shared helpers (`_is_safe_redirect_url`, `_validate_image`, `_safe_truncate_filename`, `_normalize_custom_interests`) can live in `app/utils.py` (or a small `app/helpers.py`).

### 2.2 Narrow exception handling

**Issue:** Several `except Exception:` blocks swallow all errors and only show a generic message. This hides bugs and makes debugging hard.

**Suggestion:** Catch specific exceptions (e.g. `SQLAlchemyError`, `IntegrityError`) and re-raise or log before flashing:

```python
except Exception as e:
    db.session.rollback()
    current_app.logger.exception("Create event failed")
    flash(_('An error occurred...'), 'danger')
```

Prefer `current_app.logger.exception(...)` so stack traces appear in logs.

### 2.3 Duplicate interest-update logic

**Issue:** Register and edit_profile both have similar “predefined + custom interests” logic. Duplication increases the chance of bugs and inconsistent behaviour.

**Suggestion:** Extract to a helper, e.g. in `app/utils.py` or `app/models.py`:

```python
def sync_user_interests(user, predefined_names, custom_text):
    user.interests.clear()
    # ... same logic for predefined + _normalize_custom_interests(custom_text)
```

Then call it from both the registration and edit_profile routes.

### 2.4 Event create: rollback on validation failure

**Issue:** If image validation fails after building `event`, you return without adding to the session, which is fine. If `db.session.commit()` fails, you rollback but the uploaded file has already been saved to disk.

**Suggestion:** Save the file only after a successful commit, or delete the file in the `except` block if you keep saving before commit. Prefer “save file only after commit” to avoid orphan files.

### 2.5 community_detail: N+1 and scope of “upcoming”

**Issue:** `upcoming_events = Event.query.filter(...).limit(5).all()` is not tied to the community, so it shows any 5 upcoming events, not the community’s events.

**Suggestion:** If “upcoming” should be community-specific, filter by the community (e.g. via `community_events` or a relationship). If it’s global, rename the variable/template to avoid implying it’s community-specific. Also use a single query with joins if you need community + its events to avoid N+1.

---

## 3. Models (`app/models.py`)

### 3.1 Indexes for common queries

**Issue:** Events are often filtered by `date_time` and `city`; users by `email`. Lack of indexes can slow these queries as data grows.

**Suggestion:** Add indexes:

```python
# Event
date_time = db.Column(db.DateTime, nullable=False, index=True)
city = db.Column(db.String(50), nullable=False, index=True)

# User
email = db.Column(db.String(120), unique=True, nullable=False, index=True)  # unique already creates index in most DBs
```

If you use composite filters (e.g. city + date_time), consider a composite index. Generate a new migration after changing the model.

### 3.2 datetime.utcnow vs timezone-aware

**Issue:** `default=datetime.utcnow` is UTC; if you later need timezone-aware times or “local” display, mixing naive UTC and local can be confusing.

**Suggestion:** Keep UTC in the DB. For display, use Flask-Babel’s date/time formatting with the user’s locale. If you introduce “local” event times, consider storing UTC and a timezone name, or use a library like `zoneinfo` (Python 3.9+).

### 3.3 Event.organizer_id and seed data

**Issue:** Seed creates events with no `organizer_id`. The column is nullable, which is fine, but the app should handle “no organizer” in templates (e.g. “CrossPaths” or “Community”) so the UI is consistent.

**Suggestion:** In templates, use something like `event.organizer.name if event.organizer else _('CrossPaths')` (and ensure no `.organizer` access when it’s None).

---

## 4. Forms (`app/forms.py`)

### 4.1 Single source for choices and interests

**Good:** You have `PREDEFINED_INTERESTS` and `PREDEFINED_INTEREST_CHOICES`; seed uses a similar list.

**Suggestion:** Define the list of predefined interest names once (e.g. in `forms.py` or a shared `constants.py`) and derive choices and seed from it so you don’t have to update multiple places.

### 4.2 EventForm date_time in past

**Issue:** No validation that `date_time` is in the future. Users could create events in the past.

**Suggestion:** Add a custom validator:

```python
from datetime import datetime

def validate_future_date(form, field):
    if field.data and field.data <= datetime.utcnow():
        raise ValidationError(_l('Event date and time must be in the future.'))

# In EventForm:
date_time = DateTimeLocalField(..., validators=[DataRequired(), validate_future_date])
```

Use timezone-aware now if your server uses a non-UTC timezone.

---

## 5. Seed (`app/seed.py`)

### 5.1 Idempotency

**Good:** You skip seeding if `Interest.query.first()` is not None.

**Suggestion:** Document that behaviour in the docstring. If you ever need to re-seed (e.g. new interests), consider a “seed only missing data” mode or a separate script, so you don’t duplicate events/communities.

### 5.2 Event.organizer_id in seed

**Issue:** Sample events don’t set `organizer_id`. If the model or UI assumes an organizer, ensure templates and any links (e.g. “Contact organizer”) handle `None`.

---

## 6. Frontend (`static/js/main.js`)

### 6.1 Confirmation dialogs (uk_UA)

**Issue:** The comment says “In production, this would show a proper modal” but the handler only logs. Users get no real confirmation.

**Suggestion:** Implement a small modal (or `confirm()`) for destructive or important actions (e.g. “Leave community”, “RSVP”) so the uk_UA experience matches the intent.

### 6.2 Form validation and i18n

**Issue:** `alert('Please fill in all required fields')` is hardcoded in English.

**Suggestion:** Either inject a translated message from the server (e.g. a data attribute on `<body>` or the form) or use a small map keyed by locale for client-side strings.

### 6.3 Duplicate form submit listeners

**Issue:** `forms.forEach(form => form.addEventListener('submit', ...))` runs on every form. If you load new content via AJAX or duplicate forms, you might attach multiple listeners.

**Suggestion:** Use event delegation (one listener on `document` for `submit` on forms) or ensure forms are only bound once (e.g. when they’re rendered).

### 6.4 Console.log in production

**Issue:** Several `console.log` calls will show in the browser console for all users.

**Suggestion:** Remove or guard with a dev flag (e.g. `if (window.CrossPaths && window.CrossPaths.debug) console.log(...)`).

---

## 7. Testing

**Issue:** There are no automated tests; `.gitignore` references pytest/coverage but no tests exist.

**Suggestion (high impact):**

- Add `pytest`, `pytest-flask`, and `factory_boy` (or similar) to `requirements-dev.txt`.
- Create `tests/` with:
  - `conftest.py`: app fixture, client, test DB (SQLite in-memory or separate DB).
  - Tests for: login/register (success and validation), event list/filter, create event (auth + validation), community join/leave, safe redirect, `_normalize_custom_interests`.
- Optionally: a few model tests (password hash, relationships).  
This will catch regressions and make refactors (e.g. splitting blueprints) safer.

---

## 8. Dependencies (`requirements.txt`)

- **Good:** Most versions are pinned.
- **Suggestion:** Pin `Pillow` and `psycopg2-binary` to exact versions for reproducible builds; run `pip freeze` or use a tool to audit for known vulnerabilities.

---

## 9. Quick wins (priority order)

1. **Production:** Stop running `db.create_all()` and `seed_database()` in `wsgi.py` on every worker start; use release phase or CLI.
2. **Security:** Validate `request.referrer` (or avoid it) in `set_language` to prevent open redirects.
3. **Routes:** Log exceptions with `current_app.logger.exception` instead of bare `except Exception`.
4. **Forms:** Add “date in future” validation for `EventForm.date_time`.
5. **Models:** Add DB indexes for `Event.date_time`, `Event.city`, and keep `User.email` unique (index).
6. **Code quality:** Extract interest-sync logic and consider splitting routes into multiple blueprints.
7. **Tests:** Add a minimal pytest suite for auth and one or two main flows.

---

## 10. What’s already solid

- Safe redirect check (`_is_safe_redirect_url`) for login `next`.
- Image validation with Pillow before saving uploads.
- Filename truncation and `secure_filename` to avoid path/overflow issues.
- SECRET_KEY required in production.
- Database URL fix for Heroku (`postgres://` → `postgresql://`).
- Babel integration and translation structure.
- Use of blueprints and Flask application factory.
- CLI commands for `init-db` and `seed-db`.

Implementing the suggestions above will improve security, maintainability, and reliability without changing the overall architecture of CrossPaths.
