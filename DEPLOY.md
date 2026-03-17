# Deployment (Heroku)

## Required config vars

Set these in **Heroku → Settings → Config Vars** (or via CLI).

### SECRET_KEY (required in production)

Without `SECRET_KEY`, the app raises a `RuntimeError` on startup when `FLASK_ENV=production` (Heroku’s default). Set it before the first deploy:

**Dashboard:** Settings → Config Vars → Add `SECRET_KEY` = `<long random string>`

**CLI:**

```bash
heroku config:set SECRET_KEY="your-long-random-secret"
```

Generate a secure value locally, e.g.:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## Optional / recommended

- **DATABASE_URL** – Set automatically if you use Heroku Postgres.
- **FLASK_ENV** – Heroku sets `production` by default; no need to set it.

---

## Translations

Compiled `.mo` files are committed so they are present on Heroku. If you add or change translations:

```bash
pybabel compile -d translations
git add translations/
git commit -m "Update compiled .mo files"
```

---

## Python version

The repo includes a `runtime.txt` (e.g. `python-3.12.3`) so Heroku uses a consistent Python version. Update it when you upgrade Python locally.

---

## Database migrations

The repo includes a `migrations/` folder (Flask-Migrate). The Procfile release phase runs `flask init-db` for initial deploy. For future schema changes, use:

```bash
flask db migrate -m "Description"
flask db upgrade
```

and run `flask db upgrade` in the release phase (or manually after deploy) instead of `flask init-db` for existing apps.

---

## Profile pictures (uploads)

Uploads are stored under `static/uploads/`. On Heroku the filesystem is **ephemeral** — files are lost on dyno restart. For production, plan to use **Cloudinary** or **AWS S3** (or similar) for user uploads.
