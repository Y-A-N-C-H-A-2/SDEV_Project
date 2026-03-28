# Group 8 – CrossPaths

> *Where cultures meet and friendships begin.*

> **Module:** SDEV2004 Software for Global Market
> **Academic Year:** 2025–2026, Semester 2
> **Group Members:**
> | Student Number | Name |
> |----------------|------|
> | C24490782 | Yana Chulovska |
> | C24329646 | Lívia Ferreira Guimarães Neves |
> | D24125557 | Kashish Kakran |
> | D24125357 | Simphiwe Klassen |

---

## PART 1. Project Overview

**Target Context - Type of App:** Culturally Adaptive Community Cultural Events Platform

**Purpose:** CrossPaths supports the social integration of international newcomers in Dublin by providing a culturally adaptive interface for discovering, joining, and engaging with community-based cultural events designed for groups from multiple countries. The platform adapts its layout, tone, imagery, and interaction patterns based on the user's cultural locale.

**Main Audience:** International newcomers (students, professionals, migrants) living in Dublin — specifically targeting Ukrainian and Brazilian communities, with English (Ireland) as the default locale.

---

## 2. Cultural Scope

| Attribute | Details |
|-----------|---------|
| **Supported Languages** | English (en), Ukrainian (uk), Portuguese – Brazilian (pt_BR) |
| **Target Culture / Market** | Ireland (en_IE), Ukraine (uk_UA), Brazil (pt_BR) |
| **Cultural Models Applied** | Hofstede's Cultural Dimensions, Hall's High/Low Context Communication |
| **Cultural Dimension 1** | Uncertainty Avoidance (UA) – Ireland scores 35, Ukraine scores 95, Brazil scores 76 |
| **Cultural Dimension 2** | Individualism vs Collectivism (IDV) – Ireland scores 70, Ukraine scores 25, Brazil scores 38 |

---

## 3. Design Rationale

### Personas

#### Persona 1 — Oksana (Ukrainian, 28, High UA / Low IDV)

A recently relocated Ukrainian professional in Dublin. Cautious, detail-oriented, and deliberate in decision-making. She comes from a culture with very high uncertainty avoidance (~95) and strong collectivism (~25 IDV).

**Cultural Influence:**
- **Trust:** Earned slowly through verified credentials — host badges, institutional backing, official indicators
- **Authority:** Expects clear roles and hierarchy — who is the host? what is the agenda?
- **Uncertainty:** Very low tolerance for ambiguity — needs exact event details (time, location, agenda, attendees, safety)
- **Communication:** Prefers explicit, formal, written instructions; dislikes vague or overly casual language
- **Decision-making:** Deliberate — researches all details before committing to an event

**Goals:**
1. Find safe, structured meetup events to build a social circle in Dublin
2. Know exactly what to expect before attending (agenda, host details, attendee list)
3. Connect with other Ukrainian speakers or people who understand her cultural background
4. Build a small, trusted friend group rather than a large network

**Frustrations:**
1. Events with no clear agenda or host information feel unsafe and unprofessional
2. Vague event descriptions ("Come hang out!") provide no useful information
3. No way to verify who the organiser is or whether the event is legitimate
4. Overly casual, emoji-heavy interfaces feel untrustworthy and juvenile

**Behaviour Patterns:**
1. Guidance over autonomy — wants step-by-step flows and clear CTAs
2. Detail over speed — reads all event details, FAQs, and host bios before committing
3. Structure over flexibility — prefers timed agendas, conversation prompts, fixed schedules
4. Individual caution — joins events alone but researches thoroughly; small-group preference
5. Low risk tolerance — avoids unknown locations or unverified hosts
6. Formal digital behaviour — expects professional tone, clear typography, minimal clutter

**Persona Hypothesis:**
> We believe there is a user type in **Ukrainian culture** who is a recently relocated professional seeking social connections in Dublin. They behave like a cautious, detail-oriented planner who researches every aspect of an event before committing. They struggle with ambiguity, lack of structure, and unverified social platforms that offer no safety cues or formal event details.

---

#### Persona 2 — Rafael (Brazilian, 24, Moderate UA / Higher IDV)

A recently arrived Brazilian newcomer in Dublin. Energetic, socially driven, and spontaneous. He comes from a culture with high (but lower than Ukraine) uncertainty avoidance (~76) and moderate collectivism (~38 IDV).

**Cultural Influence:**
- **Trust:** Relational — built through warmth, shared humour, and mutual connections; social proof is the trust signal
- **Authority:** Comfortable with flat, informal dynamics; prefers egalitarian open group settings
- **Uncertainty:** Moderate tolerance — fine with spontaneity and "let's see what happens"
- **Communication:** High-context and expressive; communicates through emotion and enthusiasm; prefers warm, conversational, emoji-friendly tone
- **Decision-making:** Spontaneous and social — decides based on who else is going and how the event feels

**Goals:**
1. Quickly find fun, lively social events with other international newcomers
2. See who else is attending and connect with people before the event
3. Express his personality through his profile and find people with similar energy
4. Build a wide and diverse social network as fast as possible

**Frustrations:**
1. Platforms that feel clinical, corporate, or impersonal — "like filling out a government form"
2. Not being able to see other attendees' personalities or interests before the event
3. Events that are too rigid or scripted — feels like a job interview, not friendship
4. Slow onboarding processes that require too much reading before you can do anything

**Behaviour Patterns:**
1. Autonomy over guidance — wants to explore freely, browse, and discover
2. Speed over detail — skims visuals, checks attendee photos, makes gut decisions
3. Flexibility over structure — prefers open-ended events, spontaneous chat, loose timelines
4. Social-first — checks if friends are going, joins group chats, prefers large groups
5. High risk tolerance — willing to try new events, new people, new neighbourhoods
6. Expressive digital behaviour — wants colour, personality, reactions, and visual energy

**Persona Hypothesis:**
> We believe there is a user type in **Brazilian culture** who is an energetic, socially-driven newcomer seeking community in Dublin. They behave like a spontaneous, visually-oriented social explorer who makes fast, feeling-based decisions. They struggle with cold, overly structured platforms that suppress personal expression and social warmth.

---

### Problem Statements (Point of View)

> _This section explains **why** the app behaves as it does — not a restatement of the UI._

**PoV 1 – Uncertainty Avoidance / Ukraine:**
A recently relocated Ukrainian professional in Dublin needs to feel safe and informed before attending social events with strangers because her high uncertainty-avoidance cultural background means that ambiguity and lack of structure erode trust and prevent social engagement.

**PoV 2 – Individualism–Collectivism / Brazil:**
A recently arrived Brazilian newcomer in Dublin needs to feel socially energised and personally connected through the platform because his relationally-driven, expressive cultural background means that impersonal or rigid interfaces suppress the social motivation he needs to engage.

**PoV 3 – Low UA, High IDV / Ireland:**
Irish/English-speaking users in Dublin need concise, direct content and efficient self-directed navigation because their low uncertainty-avoidance and high individualism culture prioritises personal autonomy, speed, and minimal friction in digital interactions.

### Shared Hypotheses

| # | Hypothesis | Pages Affected |
|---|-----------|----------------|
| H1 | We believe that Ukrainian users will trust the platform more and RSVP to events if we include verified host badges and structured event agendas, because high uncertainty avoidance demands explicit safety and credibility cues. | Events, Event Detail |
| H2 | We believe that Brazilian users will engage more frequently if we include a visual social feed showing attendee photos and personality-first profiles, because relational cultures prioritise social proof and warmth. | Home, Profiles, Events |
| H3 | We believe that Ukrainian users will feel less social anxiety if we provide conversation prompts and timed ice-breaker structures, because structured interaction reduces ambiguity for high-UA users. | Event Detail, During Event |
| H4 | We believe that Brazilian users will attend more events if we enable open group chat and "happening now" spontaneous events, because spontaneous social engagement aligns with lower structure preference. | Events, Chat |
| H5 | We believe that Irish users will complete onboarding faster if we use a minimal, direct UI with concise copy and self-directed navigation, because individualist cultures prefer efficiency and autonomy. | Onboarding, Home |
| H6 | We believe that a culturally adaptive UI (switching layout, tone, and imagery by locale) will increase overall engagement across all three cultures without fragmenting the community. | All Pages |

### How Cultural Considerations Influenced Design

| Element | Ireland (en_IE) | Ukraine (uk_UA) | Brazil (pt_BR) |
|---------|----------------|----------------|----------------|
| **Layout** | Clean, minimal, direct — card-based with whitespace | Structured, grid-based, clear sections with explicit labels | Warm, layered, social-feed style with visual density |
| **Navigation** | Self-directed, tab-based, minimal hand-holding | Step-by-step, linear, breadcrumb-guided with clear CTAs | Explorative, browse-first, swipe-friendly |
| **Colour Palette** | Soft sage/mint pastels — approachable and calm | Soft pastel periwinkle/lavender — trustworthy and gentle | Warm orange palette (Bumble BFF-inspired) — energetic and inviting |
| **Imagery** | Minimal — functional icons, Dublin landmarks | Verified host photos, venue images, maps, safety icons | Personality photos, group shots, expressive graphics |
| **Language / Tone** | Direct, informal, concise | Formal, explicit, reassuring | Warm, conversational, enthusiastic |
| **Symbols / Icons** | Functional UI icons (search, filter, calendar) | Verified badges ✓, lock icons 🔒, agenda icons 📋 | Social icons (hearts, reactions, group indicators) |

---

## 4. Architecture and Structure

The app lives at **repository root** (no nested app folder). Single `requirements.txt` for local and production dependencies.

```
<repo root>/
├── app/
│   ├── __init__.py          # App factory, Flask config, Babel setup
│   ├── routes.py            # All route definitions
│   ├── models.py            # Database models (User, Event, Community, Interest)
│   ├── forms.py             # WTForms definitions
│   └── seed.py              # Database seeding with sample data
├── templates/
│   ├── base.html            # Master template – shared layout, nav, lang switcher
│   ├── index.html           # Home page
│   ├── events.html          # Events listing page
│   ├── profile.html         # User profile page
│   ├── about.html           # About / community page
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   ├── create_event.html    # Event creation page
│   ├── event_detail.html    # Single event detail page
│   ├── edit_profile.html    # Edit profile page
│   ├── communities.html     # Communities listing page
│   ├── community_detail.html # Single community detail page
│   └── partials/            # Locale-specific partial templates
├── static/
│   ├── css/
│   │   ├── main.css         # Shared styles
│   │   └── locale-*.css     # Per-locale theme (en_IE, uk_UA, pt_BR)
│   ├── js/
│   │   └── main.js
│   └── img/
│       ├── common/          # Shared images (logo, hero, discover)
│       └── seed/            # Sample event/community images
├── translations/
│   ├── en_IE/
│   │   └── LC_MESSAGES/
│   │       └── messages.po
│   ├── uk_UA/
│   │   └── LC_MESSAGES/
│   │       └── messages.po
│   └── pt_BR/
│       └── LC_MESSAGES/
│           └── messages.po
├── scripts/                 # Translation/seed helpers
├── babel.cfg
├── requirements.txt         # Dependencies (local + production)
├── Dockerfile               # Optional: local / other hosts that run containers
├── .dockerignore            # Used only when building the Docker image
├── render.yaml              # Render Blueprint (Docker web + PostgreSQL)
├── run.py                   # Local dev entry point
├── gunicorn.conf.py         # Bind + 120s timeout when start cmd is plain `gunicorn app:app`
├── wsgi.py                  # Production WSGI entry (e.g. gunicorn wsgi:app)
└── README.md                # This file (design + run/deploy reference)
```

### Template Inheritance Strategy

All pages extend `base.html` using Jinja's `{% extends %}` directive. `base.html` provides:
- Site-wide navigation including the language/locale switcher
- Common `<head>` metadata, CSS links, and JS includes
- A `{% block content %}` placeholder for page-specific content
- A `{% block title %}` placeholder for page-specific titles
- Locale-aware CSS class on `<body>` (e.g., `class="locale-uk_UA"`) to enable culture-specific styling

### Static File Management

Static files: shared images under `static/img/common/` and seed images under `static/img/seed/`. Shared CSS is `static/css/main.css`; each locale loads an additional file (`static/css/locale-en_IE.css`, `locale-uk_UA.css`, or `locale-pt_BR.css`) from `base.html`. JavaScript is shared in `static/js/main.js`.

### Dynamic Behaviour

The app stores the user's selected locale in a Flask session variable (`session['lang']`). When a user clicks a locale option in the navigation bar, a route sets `session['lang']` to the chosen locale and redirects to the same page. All templates and route handlers reference `get_locale()` to determine the active locale for translations, imagery, and cultural layout switching.

```python
# Example: passing locale to template context
@app.context_processor
def inject_locale():
    return dict(locale=get_locale())
```

```html
<!-- Example: Jinja conditional for cultural layout -->
{% if locale == 'pt_BR' %}
  <div class="layout-warm">
    <!-- Visual social feed, personality-first profiles, warm imagery -->
  </div>
{% elif locale == 'uk_UA' %}
  <div class="layout-formal">
    <!-- Structured event agenda, verified host badges, conversation prompts -->
  </div>
{% else %}
  <div class="layout-minimal">
    <!-- Clean, direct, self-directed navigation -->
  </div>
{% endif %}
```

### Internationalisation and Localisation Strategy

### GNU gettext Usage

All user-facing strings in templates are wrapped with `{{ _('string') }}` and in Python files with `_('string')`, using Flask-Babel's gettext integration.

```python
# app/__init__.py
from flask_babel import Babel

babel = Babel()

def get_locale():
    from flask import session
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(['en_IE', 'uk_UA', 'pt_BR']) or 'en_IE'

# In create_app():
babel.init_app(app, locale_selector=get_locale)
```

```html
<!-- templates/base.html -->
<title>{{ _('CrossPaths – Where cultures meet and friendships begin') }}</title>
```

### Language Switching Mechanism

Users switch language by clicking a flag/label button in the navigation bar. This triggers a POST request to a `/set-language` route, which sets `session['lang']` to the selected locale (`en_IE`, `uk_UA`, or `pt_BR`) and redirects the user back to their current page. The language switcher is visible and accessible on every page.

**What to look for when switching locales:**
- **uk_UA:** Structured layouts, verified badges, formal tone, event agendas, safety reassurance
- **pt_BR:** Visual social feed, warm imagery, personality-first profiles, expressive UI tone, group chat indicators
- **en_IE:** Clean minimal layout, direct concise copy, self-directed navigation, neutral colour palette

### Configuration Notes

```bash
export FLASK_APP=app
export FLASK_ENV=development
export SECRET_KEY=dev-secret-key
```

---

## 5. Development, deployment, and technical reference

### 5.1 Run locally

From the repository root (where `requirements.txt` lives):

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
pybabel compile -d translations

export FLASK_ENV=development
python run.py
```

Open http://127.0.0.1:5000 . If port 5000 is busy (e.g. AirPlay on macOS): `FLASK_PORT=5001 python run.py` .

The app uses **SQLite** (`crosspaths.db`) when `DATABASE_URL` is not set. No PostgreSQL is required for local development.

### 5.2 Translations

After changing translatable strings in templates or Python:

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
# Edit translations/*/LC_MESSAGES/messages.po, then:
pybabel compile -d translations
```

The `messages.pot` file is **generated** by `extract` and is listed in `.gitignore`. The app also compiles outdated `.mo` files on startup when possible.

### 5.3 Production on Render (Docker)

1. Push this repository to GitHub (or another Git host Render supports).
2. In the [Render Dashboard](https://dashboard.render.com), choose **New → Blueprint**, connect the repo, and apply **`render.yaml`**. That creates a **Docker** web service (image built from **`Dockerfile`**) and **PostgreSQL**; **`render.yaml`** sets:
   - **Build:** Docker build from **`./Dockerfile`** (includes `pip install`, `pybabel compile`, **`docker-entrypoint.sh`** → gunicorn on `$PORT`)
   - **Env:** `FLASK_APP=wsgi:app`, `FLASK_ENV=production`, generated **`SECRET_KEY`**, **`DATABASE_URL`** from the database  
   Confirm database pricing in the UI if prompted. In **Environment**, confirm **`SECRET_KEY`** has a non-empty value; if it is missing, add one (`openssl rand -base64 32` locally) — Render’s `generateValue` only runs when that variable does not already exist (e.g. empty placeholder from an earlier setup).
3. **Database tables and seed data:** On **paid** plans you can use **Shell** and run `flask init-db && flask seed-db`. On the **free** tier (no Shell), **`render.yaml`** sets **`AUTO_DB_SETUP=1`**, so the Docker **entrypoint** runs those commands once before gunicorn on each deploy; they are safe to repeat (`create_all` / seed only if empty). After the first good deploy you may set **`AUTO_DB_SETUP`** to **`0`** in **Environment** if you prefer not to run them on every restart.
4. **Without `AUTO_DB_SETUP`:** From your laptop, copy the Postgres **External Database URL** from the Render dashboard, then from the project root with `venv` active:  
   `export DATABASE_URL='…' SECRET_KEY='…' FLASK_APP=wsgi:app FLASK_ENV=production` → `flask init-db && flask seed-db`.
5. Optional: set **`WEB_CONCURRENCY`** in **Environment** for gunicorn workers. **`/health`** is the health-check path.

**Already created the service manually?** Choose **Environment → Docker**, set **Dockerfile path** to `./Dockerfile`, and add **`FLASK_APP=wsgi:app`**, **`FLASK_ENV=production`**, **`SECRET_KEY`**, **`DATABASE_URL`**, and (free tier) **`AUTO_DB_SETUP=1`** if you cannot use Shell. Render sets **`PORT`**; the image **entrypoint** starts gunicorn. For a **native Python** service instead of Docker, use build `pip install -r requirements.txt && pybabel compile -d translations`, start `gunicorn --bind 0.0.0.0:$PORT --timeout 120 wsgi:app`, and the same env vars.

**Ephemeral disk:** Each deploy gets a fresh disk unless you add a **persistent disk** or external object storage; uploads under `static/uploads` are not kept across redeploys unless you add storage.

**Local Docker:** `docker build` / `docker run` using **`Dockerfile`** matches what Render builds from **`render.yaml`**.

### 5.4 Production deployment (any host)

- Point **`DATABASE_URL`** at PostgreSQL when not using local SQLite; the app maps `postgres://` to `postgresql://` and adds `sslmode=require` when needed.
- Set **`SECRET_KEY`** in the environment (required when `FLASK_ENV=production`).
- After deploy, create and seed tables if needed: `FLASK_APP=wsgi:app flask init-db` and `FLASK_APP=wsgi:app flask seed-db`.
- Use `/health` on the deployed URL to surface configuration/DB issues.

### 5.5 Core features and routes

**Public:** Home (upcoming events + featured communities), paginated events list (city filter + search), event detail, communities list and detail (community-specific upcoming events), About (locale partials), locale switch via POST `/set-language` (same-origin redirect only).

**Auth:** Register, login (safe relative `next` redirect), logout.

**Signed-in:** Profile, edit profile (interests in one transaction), create event (optional image validated with Pillow, stored under `static/uploads`), join/leave community.

| Route | Methods | Auth | Purpose |
|-------|---------|------|--------|
| `/`, `/index` | GET | No | Home |
| `/events` | GET | No | Events list + filters |
| `/event/<id>` | GET | No | Event detail |
| `/create-event` | GET, POST | Yes | Create event |
| `/communities` | GET | No | Communities list |
| `/community/<id>` | GET | No | Community detail |
| `/community/<id>/join` `leave` | POST | Yes | Membership |
| `/register` `/login` `/logout` | — | — | Auth |
| `/profile` `/edit-profile` | GET, POST | Yes | Profile |
| `/about` | GET | No | About |
| `/set-language` | POST | No | Session locale |

**Data model (summary):** `User`, `Interest`, `Event`, `Community` with many-to-many links (interests, event attendance, community membership, events linked to communities). Indexes on `Event.date_time` and `Event.city` support listing and filters.

**Stack (high level):** Flask (app factory, blueprint), Flask-SQLAlchemy + Alembic/Flask-Migrate, Flask-Login, Flask-WTF/CSRF, Flask-Babel, Werkzeug (passwords, `secure_filename`), Pillow (upload validation), gunicorn (production WSGI server). Entry points: `run.py` (local, may create/seed DB in app context), `wsgi.py` (production).

### 5.6 Troubleshooting

| Issue | What to try |
|-------|-------------|
| Missing Flask / Babel modules | Activate `venv`, then `pip install -r requirements.txt` from project root |
| Translations not updating | Run `pybabel compile -d translations` from project root |
| Production 500 / no tables | Ensure PostgreSQL + `DATABASE_URL` + `SECRET_KEY`; run `init-db` and `seed-db` |
| Render: worker exits, `SECRET_KEY ... not set` | Dashboard → web service → **Environment** → add **`SECRET_KEY`** (random string). Remove any empty **`SECRET_KEY`** row, save, **Manual Deploy** |
| `psycopg2` build errors locally | Local dev uses SQLite; full Postgres support may need system libs + `psycopg2-binary` |

---

## 6. Design Thinking Deliverables (Week 5 Lab – Part B)

### Emerging Design Tensions

| # | Tension | Description |
|---|---------|-------------|
| 1 | **Structure vs. Spontaneity** | Oksana needs a timed agenda, conversation prompts, and clear event flow. Rafael wants open-ended, free-flowing social events. The UI must accommodate both without forcing one model. |
| 2 | **Verification vs. Warmth** | Oksana looks for authority cues — verified host badges, official logos, attendee caps. Rafael looks for warmth cues — photos, emojis, group energy. Balancing these signals in a single event card is a core design challenge. |
| 3 | **Detail-first vs. Visual-first** | Oksana's decision flow is: read details → evaluate safety → commit. Rafael's is: see vibe → check people → jump in. The information architecture must serve both scanning styles. |

### Key Assumptions

1. Ukrainian newcomers in Dublin experience higher social anxiety around unstructured meetup events compared to Brazilian newcomers, and this is culturally driven (not just personality).
2. Brazilian newcomers make attendance decisions primarily based on social/visual cues (who's going, how it looks) rather than informational cues (agenda, host credentials).
3. A single platform can serve both user types through culturally adaptive UI (locale-based layout switching) without fragmenting the community into separate experiences.
4. Users will self-identify their cultural preferences through locale selection, and this is a reliable-enough proxy for serving culturally appropriate UI patterns.
5. Providing structured conversation prompts and ice-breakers will not feel patronising to Brazilian users, and open group chat will not feel unsafe to Ukrainian users — or these features can be selectively shown.

**Riskiest Assumption:** #3 — That a single adaptive platform can genuinely serve both user types without one cultural mode feeling like a "lesser" or "default" version. If the adaptive switching feels superficial (just colour changes) rather than structural (different information architecture, different flows), both personas may feel underserved.

---

## 7. Limitations

- Translations are not exhaustive — some dynamic content (e.g., error messages) may remain in English
- Cultural adaptations are applied at the locale level; sub-regional differences within Ukraine or Brazil are not addressed
- Images are locale-specific but sourced from static files — no CDN or dynamic image fetching
- Right-to-left (RTL) layout not required for current locales but architecture does not yet support it
- Application has not been tested on mobile devices
- Persona-based design is grounded in Hofstede's cultural dimensions, which are national-level generalisations — individual users may not align perfectly with their culture's average scores
- The culturally adaptive UI relies on user-selected locale as a proxy for cultural preference, which may not always be accurate.
