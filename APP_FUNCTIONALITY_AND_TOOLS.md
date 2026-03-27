# CrossPaths — Application Functionality & Tools

This document describes what the CrossPaths application does and how every technology and tool in the project is used.

---

## 1. Application Overview

**Name:** CrossPaths — *Where cultures meet and friendships begin.*

**Type:** Culturally adaptive web application for community cultural events.

**Purpose:** Help international newcomers in Dublin discover, join, and engage with community-based cultural events. The interface adapts by locale (Ireland, Ukraine, Brazil) so layout, tone, imagery, and interaction patterns match the user’s cultural context.

**Target users:** International newcomers (students, professionals, migrants) in Dublin, with a focus on Ukrainian and Brazilian communities and English (Ireland) as the default.

**Supported locales:**
- **en_IE** — English (Ireland): minimal, direct UI and copy.
- **uk_UA** — Ukrainian: structured, formal, safety-focused.
- **pt_BR** — Portuguese (Brazil): warm, social, expressive.

---

## 2. Core Functionality

### 2.1 Public (no login)

| Feature | Description |
|--------|-------------|
| **Home** | Lists up to 4 upcoming events and 4 communities; hero copy and layout vary by locale in `index.html`. |
| **Events list** | Paginated list of upcoming events; filter by city and free-text search (title/description). |
| **Event detail** | Single event page with title, description, date/time, city, venue, category, photo, organizer. |
| **Communities list** | Paginated list of communities. |
| **Community detail** | Single community with description, image, and **upcoming events linked to that community** (not global). |
| **About** | Static/about page; content can be locale-specific via partials. |
| **Language switch** | User chooses locale (en_IE / uk_UA / pt_BR); stored in session; redirect is same-origin only (no open redirect). |

### 2.2 Authentication

| Feature | Description |
|--------|-------------|
| **Register** | Email, password, name, optional age/gender/nationality/city; predefined + custom interests. Duplicate email is rejected. |
| **Login** | Email + password; supports safe `?next=` redirect (relative URL only). |
| **Logout** | Clears session and redirects to home. |

### 2.3 Authenticated user

| Feature | Description |
|--------|-------------|
| **Profile** | View own profile (name, age, gender, nationality, city, interests). |
| **Edit profile** | Update name, age, gender, nationality, city, and interests (predefined checkboxes + comma-separated custom). Changes and interest sync are inside a single transaction; DB errors trigger rollback and a flash message. |
| **Create event** | Title, description, city, venue, date/time (must be in the future), category, optional photo. Photo is validated as a real image (Pillow) and saved with a unique name; max upload 16 MB. |
| **Join community** | POST to join; user is added to community members. |
| **Leave community** | POST to leave; user is removed from community members. |

### 2.4 Data model (summary)

- **User:** name, email, hashed password, age, gender, nationality, city; many-to-many with Interest, Community; one-to-many organized events; many-to-many attending events.
- **Interest:** name, predefined flag; many-to-many with User.
- **Event:** title, description, date_time, city, venue, category, photo, organizer_id; many-to-many with Community and with attendees (User).
- **Community:** name, description, image; many-to-many with User (members) and Event (community_events).

Indexes on `Event.date_time` and `Event.city` support filtering and sorting.

---

## 3. Routes Reference

| Route | Methods | Auth | Purpose |
|-------|---------|------|--------|
| `/`, `/index` | GET | No | Home: upcoming events + communities. |
| `/events` | GET | No | Events list with city filter, search, pagination. |
| `/event/<id>` | GET | No | Event detail. |
| `/create-event` | GET, POST | Yes | Create event (form + future-date validation). |
| `/communities` | GET | No | Communities list, paginated. |
| `/community/<id>` | GET | No | Community detail + **that community’s** upcoming events. |
| `/community/<id>/join` | POST | Yes | Join community. |
| `/community/<id>/leave` | POST | Yes | Leave community. |
| `/register` | GET, POST | No | User registration. |
| `/login` | GET, POST | No | Login (safe `next` redirect). |
| `/logout` | GET | Yes | Logout. |
| `/profile` | GET | Yes | Own profile. |
| `/edit-profile` | GET, POST | Yes | Edit profile and interests. |
| `/about` | GET | No | About page. |
| `/set-language` | POST | No | Set session locale; redirect same-origin only. |

---

## 4. Tools and Technologies (How They Are Used)

### 4.1 Python & runtime

- **Python 3** — Application language.
- **run.py** — Local development entry: creates app, runs `db.create_all()` and `seed_database()` in app context, then `app.run()` with host/port/debug from environment.
- **wsgi.py** — Production WSGI entry; only creates the app. No DB init or seed here (handled by Heroku release or CLI).

### 4.2 Web framework and server

| Tool | Version | Role |
|------|---------|------|
| **Flask** | 3.0.0 | Core framework: app factory, routing, request/response, templates, session, config. |
| **Werkzeug** | 3.0.1 | WSGI utilities, request/response, security (e.g. password hashing), routing. Used implicitly by Flask. |
| **gunicorn** | 21.2.0 | Production WSGI server (Heroku `web` process). |

Flask is used with an application factory (`create_app()` in `app/__init__.py`), one blueprint (`main` in `app/routes.py`), and template/static folders at repo root.

### 4.3 Database and ORM

| Tool | Version | Role |
|------|---------|------|
| **Flask-SQLAlchemy** | 3.1.1 | Binds SQLAlchemy to the Flask app; provides `db` (session, models, queries). |
| **SQLAlchemy** | ≥2.0.47 | ORM: models, relationships, queries, migrations (via Alembic). |
| **Flask-Migrate** | 4.0.5 | Integrates Alembic with Flask for `flask db` CLI (migrate, upgrade, etc.). |
| **Alembic** | 1.13.1 | Schema migrations (versions, upgrade/downgrade). |
| **SQLite** | — | Default DB when `DATABASE_URL` is not set (file: `crosspaths.db`). |
| **PostgreSQL** | — | Production (Heroku); used when `DATABASE_URL` is set. |
| **psycopg2-binary** | ≥2.9.11 | PostgreSQL driver for SQLAlchemy. |

Models live in `app/models.py` (User, Interest, Event, Community and association tables). Indexes on `Event.date_time` and `Event.city` improve list/filter performance. CLI: `flask init-db` (create tables), `flask seed-db` (seed data).

### 4.4 Authentication and security

| Tool | Version | Role |
|------|---------|------|
| **Flask-Login** | 0.6.3 | Session-based login: `login_user`, `logout_user`, `current_user`, `@login_required`, user loader. |
| **Werkzeug** | — | `generate_password_hash` / `check_password_hash` in User model. |
| **Flask-WTF** | 1.2.1 | CSRF protection (CSRFProtect), form integration. |
| **itsdangerous** | 2.2.0 | Signed tokens/session (used by Flask/Werkzeug). |

SECRET_KEY is required in production (`FLASK_ENV=production`); otherwise the app refuses to start.

### 4.5 Forms and validation

| Tool | Version | Role |
|------|---------|------|
| **WTForms** | 3.1.2 | Form classes and field types (String, Password, Integer, Select, TextArea, DateTimeLocal, File, etc.). |
| **Flask-WTF** | 1.2.1 | FlaskForm, CSRF token in forms, FileAllowed. |
| **email-validator** | 2.1.0 | Email validation for WTForms. |

Forms in `app/forms.py`: RegistrationForm, LoginForm, ProfileForm, EventForm. Custom `validate_future_date` ensures event date/time is in the future. Choices (cities, gender, categories, predefined interests) are centralized and use lazy gettext for labels.

### 4.6 Internationalisation (i18n)

| Tool | Version | Role |
|------|---------|------|
| **Babel** | 2.14.0 | Message extraction and compilation: `.po` / `.mo` catalogs. |
| **flask-babel** | 4.0.0 | Flask integration: `gettext` / `lazy_gettext`, locale selection, translation directories. |
| **pytz** | 2026.1.post1 | Timezone support for Babel/datetime. |

Locale selection: session `lang` first, then `Accept-Language` match from `en_IE`, `uk_UA`, `pt_BR`; default `en_IE`. App compiles `.po` → `.mo` on startup when needed. Templates use `{{ _('...') }}`; Python uses `_('...')` or `_l('...')`. `babel.cfg` defines extraction for Python and Jinja2.

### 4.7 File uploads and images

| Tool | Version | Role |
|------|---------|------|
| **Pillow** | ≥10.4.0 | Image validation: open and verify upload stream before saving; reject non-images. |
| **Werkzeug** | — | `secure_filename` for safe filenames. |

Event photos: optional upload in EventForm; validated with Pillow; filename truncated and prefixed with UUID; stored under `static/uploads` (max 16 MB). Invalid image returns a flash error instead of saving.

### 4.8 Templates and front-end

| Tool | Version | Role |
|------|---------|------|
| **Jinja2** | 3.1.6 | Server-side templates: inheritance, blocks, loops, conditionals, `url_for`, `_()`. |
| **MarkupSafe** | 3.0.3 | Safe string escaping for Jinja2. |

Layout: `templates/base.html`; pages extend it and fill `content` and `title`. Locale is injected as `locale` (e.g. `en_IE`) and used for body class and conditional blocks (e.g. home, about). No front-end build; plain CSS and JS.

### 4.9 Configuration and environment

| Tool | Version | Role |
|------|---------|------|
| **python-dotenv** | 1.0.0 | Loads `.env` for local env vars (if used). |
| **Click** | 8.3.1 | Used by Flask CLI for `flask init-db` and `flask seed-db`. |

Config in `create_app()`: SECRET_KEY, BABEL_*, SQLALCHEMY_DATABASE_URI (with Heroku `postgres://` → `postgresql://`), UPLOAD_FOLDER, MAX_CONTENT_LENGTH. Blinker is a Flask dependency for signals.

### 4.10 Deployment (Heroku)

| Tool | Role |
|------|------|
| **Procfile** | `web: gunicorn wsgi:app` and `release: flask init-db && flask seed-db`. |
| **wsgi.py** | Exposes `app` for gunicorn; no DB/seed logic. |

Release phase runs once per deploy to create tables and seed; web workers only serve the app.

---

## 5. Application Modules and Key Files

| File / folder | Role |
|---------------|------|
| **app/__init__.py** | App factory, config, extension init (Babel, DB, Migrate, Login, CSRF), locale selector, translation compile, user loader, blueprint registration, context processor for `locale`, CLI `init-db` and `seed-db`. |
| **app/routes.py** | All routes; helpers: `_is_safe_redirect_url`, `_validate_image`, `_safe_truncate_filename`; uses `sync_user_interests` and `is_same_origin_referrer` from utils. |
| **app/models.py** | SQLAlchemy models and association tables (user_interests, user_communities, event_attendees, community_events). |
| **app/forms.py** | WTForms forms, choices, and `validate_future_date`. |
| **app/seed.py** | Idempotent seed: predefined interests, sample events, sample communities (skips if data exists). |
| **app/utils.py** | `normalize_custom_interests`, `sync_user_interests`, `is_same_origin_referrer`. |
| **templates/** | Jinja2 HTML; `base.html`; locale-specific about content under `partials/about/`. |
| **static/css/main.css** | Global and locale-specific (body class) styles. |
| **static/js/main.js** | Locale-based behaviour (e.g. uk_UA confirmations/safety, pt_BR animations/emoji, en_IE quick actions), mobile nav, smooth scroll, form validation; `CrossPaths` namespace for utilities. |
| **translations/** | Per-locale `LC_MESSAGES/messages.po` and compiled `messages.mo`. |
| **babel.cfg** | Babel extraction rules for Python and Jinja2. |
| **messages.pot** | Extracted template for translations. |
| **scripts/** | Helper scripts (e.g. translation/seed helpers). |

---

## 6. Security and Robustness (Relevant Tools and Patterns)

- **CSRF:** Flask-WTF CSRF on forms.
- **Passwords:** Werkzeug hashing in User model.
- **Redirects:** Login `next` only relative URLs (`_is_safe_redirect_url`); language switcher only same-origin (`is_same_origin_referrer`).
- **Uploads:** Pillow image check; `secure_filename` and length limit; unique filenames.
- **DB errors:** Routes catch `SQLAlchemyError`, rollback, log with `current_app.logger.exception`, and show a generic flash message.
- **Production:** SECRET_KEY required; DB and seed via release/CLI, not in worker startup.

---

## 7. Quick Reference: Dependency → Purpose

| Dependency | Purpose |
|------------|--------|
| Flask | Web app, routing, templates, config, app factory. |
| Werkzeug | WSGI, request/response, password hashing, secure_filename. |
| Flask-SQLAlchemy | DB binding and session. |
| SQLAlchemy | ORM, models, queries, indexes. |
| Flask-Migrate + Alembic | DB migrations. |
| Flask-Login | Login/logout, current_user, login_required. |
| Flask-WTF | CSRF, FlaskForm. |
| WTForms + email-validator | Form fields and validation. |
| Babel + flask-babel + pytz | i18n: extraction, compilation, locale, gettext. |
| Pillow | Image validation for uploads. |
| gunicorn | Production WSGI server. |
| Click | Flask CLI commands. |
| psycopg2-binary | PostgreSQL driver. |
| Jinja2 + MarkupSafe | Templates and escaping. |
| python-dotenv | Optional .env loading. |
| itsdangerous | Signed data (sessions/tokens). |
| blinker | Flask signals. |

This file, together with **README.md** (design, personas, architecture) and **QUICKSTART.md** (run instructions), gives a full picture of CrossPaths functionality and the tools used to implement it.
