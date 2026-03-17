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

The app lives at **repository root** (no nested app folder). Single `requirements.txt` for local and Heroku.

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
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── img/
│       ├── common/          # Shared images
│       ├── en_IE/
│       ├── uk_UA/
│       └── pt_BR/
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
├── messages.pot
├── requirements.txt         # Single source for deps (local + Heroku)
├── run.py                   # Local dev entry point
├── wsgi.py                  # Heroku/gunicorn entry point
├── Procfile                 # Heroku: web process
├── QUICKSTART.md            # Run instructions
└── README.md
```

### Template Inheritance Strategy

All pages extend `base.html` using Jinja's `{% extends %}` directive. `base.html` provides:
- Site-wide navigation including the language/locale switcher
- Common `<head>` metadata, CSS links, and JS includes
- A `{% block content %}` placeholder for page-specific content
- A `{% block title %}` placeholder for page-specific titles
- Locale-aware CSS class on `<body>` (e.g., `class="locale-uk_UA"`) to enable culture-specific styling

### Static File Management

Static files are organised with locale-specific images stored in subfolders under `static/img/` (e.g., `static/img/uk_UA/hero.jpg`). Shared CSS lives in `static/css/main.css` with locale-specific overrides triggered by body class (e.g., `.locale-pt_BR .hero { ... }`). JavaScript is shared across all locales in `static/js/main.js`.

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

## 9. Design Thinking Deliverables (Week 5 Lab – Part B)

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

## 10. Limitations

- Translations are not exhaustive — some dynamic content (e.g., error messages) may remain in English
- Cultural adaptations are applied at the locale level; sub-regional differences within Ukraine or Brazil are not addressed
- Images are locale-specific but sourced from static files — no CDN or dynamic image fetching
- Right-to-left (RTL) layout not required for current locales but architecture does not yet support it
- Application has not been tested on mobile devices
- Persona-based design is grounded in Hofstede's cultural dimensions, which are national-level generalisations — individual users may not align perfectly with their culture's average scores
- The culturally adaptive UI relies on user-selected locale as a proxy for cultural preference, which may not always be accurate.
