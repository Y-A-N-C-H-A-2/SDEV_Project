# Group [NUMBER] – SDEV2004 Culturally Adaptive Web Application

> **Module:** SDEV2004 Software for the Global Market  
> **Academic Year:** 2025–2026, Semester 2  
> **Group Members:**
> | Student Number | Name |
> |----------------|------|
> | C24490782 | Yana Chulovska |
> | C24329646 | Livia Ferreira Guimaraes Neves |
> | D24125557 | Kashish Kakran |
> | D24125357 | Simphiwe Klassen |
 

---

## 1. Project Overview

**Target Area:** [e.g. Online News / E-Commerce / Travel / Healthcare – TO BE AGREED]

[2–3 sentences describing the application and its purpose. What does it do? Who is it for?]

> _Example: This application is a culturally adaptive news portal designed to present current affairs content in a way that reflects the communication styles, values, and visual preferences of users from Ireland, Ukraine, and Brazil._

---

## 2. Cultural Scope

| Attribute | Details |
|-----------|---------|
| **Supported Languages** | English (en), Ukrainian (uk), Portuguese – Brazilian (pt_BR) |
| **Supported Countries / Locales** | Ireland (en_IE), Ukraine (uk_UA), Brazil (pt_BR) |
| **Cultural Models Applied** | [e.g. Hofstede's Cultural Dimensions, Hall's High/Low Context Communication] |
| **Cultural Dimension 1** | [Dimension name] – Ireland/UK scores [X], Ukraine scores [Y], Brazil scores [Z] |
| **Cultural Dimension 2** | [Dimension name] – Ireland/UK scores [X], Ukraine scores [Y], Brazil scores [Z] |

---

## 3. Design Rationale

### Problem Statements (Point of View)

> _This section explains **why** the app behaves as it does — not a restatement of the UI._

**PoV 1 – [Cultural dimension / country]:**  
[e.g. Ukrainian users, coming from a high uncertainty-avoidance culture, need clear structure, explicit instructions, and formal language because ambiguity in UI design reduces trust and engagement.]

**PoV 2 – [Cultural dimension / country]:**  
[e.g. Brazilian users, operating in a high-context, collectivist culture, need social proof, warm imagery, and community-oriented language because decisions are often influenced by group identity and relationship-building.]

**PoV 3 – [Cultural dimension / country]:**  
[e.g. Irish/English users, in a low-context, individualist culture, need concise, direct content and minimal visual noise because they prefer efficiency and self-directed navigation.]

### Shared Hypotheses

| # | Hypothesis | Pages Affected |
|---|-----------|----------------|
| H1 | We believe that [Ukrainian/pt_BR/en_IE] users will [expected behaviour] if we [design change], because [cultural rationale]. | [Page(s)] |
| H2 | We believe that … | [Page(s)] |
| H3 | We believe that … | [Page(s)] |
| H4 | We believe that … | [Page(s)] |

### How Cultural Considerations Influenced Design

| Element | Ireland (en_IE) | Ukraine (uk_UA) | Brazil (pt_BR) |
|---------|----------------|----------------|----------------|
| **Layout** | [e.g. Clean, minimal, LTR] | [e.g. Structured, formal, LTR] | [e.g. Warm, layered, LTR] |
| **Navigation** | [description] | [description] | [description] |
| **Colour Palette** | [description] | [description] | [description] |
| **Imagery** | [description] | [description] | [description] |
| **Language / Tone** | [e.g. Direct, informal] | [e.g. Formal, explicit] | [e.g. Warm, relational] |
| **Symbols / Icons** | [description] | [description] | [description] |

---

## 4. Architecture and Structure

```
Group[NUMBER]-Phase2/
├── app/
│   ├── __init__.py          # App factory, Flask config, Babel setup
│   ├── routes.py            # All route definitions
│   └── utils.py             # Helper functions (locale detection, etc.)
├── templates/
│   ├── base.html            # Master template – shared layout, nav, lang switcher
│   ├── index.html           # Home page (Member X)
│   ├── [page2].html         # [Member Y's page]
│   ├── [page3].html         # [Member Z's page]
│   └── [page4].html         # [Member W's page]
├── static/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── img/
│       ├── en_IE/
│       ├── uk_UA/
│       └── pt_BR/
├── translations/
│   ├── en_IE/
│   │   └── LC_MESSAGES/
│   │       ├── messages.po
│   │       └── messages.mo
│   ├── uk_UA/
│   │   └── LC_MESSAGES/
│   │       ├── messages.po
│   │       └── messages.mo
│   └── pt_BR/
│       └── LC_MESSAGES/
│           ├── messages.po
│           └── messages.mo
├── babel.cfg
├── messages.pot
├── requirements.txt
└── README.md
```

### Template Inheritance Strategy

All pages extend `base.html` using Jinja's `{% extends %}` directive. `base.html` provides:
- Site-wide navigation including the language/locale switcher
- Common `<head>` metadata, CSS links, and JS includes
- A `{% block content %}` placeholder for page-specific content
- A `{% block title %}` placeholder for page-specific titles

### Static File Management

[Describe how static files are organised — e.g. locale-specific images stored in subfolders, shared CSS in root of css/]

### Dynamic Behaviour

[Describe how the app detects/stores the user's selected locale — e.g. URL prefix `/en_IE/`, session variable, or query parameter `?lang=uk_UA`]

---

## 5. Internationalisation and Localisation Strategy

### GNU gettext Usage

All user-facing strings in templates are wrapped with `{{ _('string') }}` and in Python files with `_('string')`, using Flask-Babel's gettext integration.

```python
# app/__init__.py
from flask_babel import Babel, gettext as _

babel = Babel(app)

@babel.localeselector
def get_locale():
    return session.get('lang', 'en_IE')
```

```html
<!-- templates/base.html -->
<title>{{ _('Site Title') }}</title>
```

### Language Switching Mechanism

[Describe how users switch language — e.g. clicking a flag/button in the nav sets `session['lang']` and redirects to the same page]

### Default Language and Fallback

- **Default locale:** `en_IE` (English – Ireland)  
- **Fallback:** If a translation string is missing in `uk_UA` or `pt_BR`, the app falls back to `en_IE`.

### Translation File Management

| Command | Purpose |
|---------|---------|
| `pybabel extract -F babel.cfg -o messages.pot .` | Extract all translatable strings |
| `pybabel init -i messages.pot -d translations -l uk_UA` | Initialise Ukrainian translations |
| `pybabel init -i messages.pot -d translations -l pt_BR` | Initialise Brazilian Portuguese translations |
| `pybabel update -i messages.pot -d translations` | Update .po files after adding new strings |
| `pybabel compile -d translations` | Compile .po → .mo (required to take effect) |

All `.po` files are committed to the repository. `.mo` files are compiled locally before submission.

---

## 6. Cultural Adaptation Mechanisms

### How Cultural Differences Are Implemented

[Describe the technical approach — e.g. Jinja conditionals based on `g.locale`, context variables passed from routes, locale-specific CSS classes, config dictionaries]

```python
# Example: passing locale to template context
@app.context_processor
def inject_locale():
    return dict(locale=get_locale())
```

```html
<!-- Example: Jinja conditional for cultural layout -->
{% if locale == 'pt_BR' %}
  <div class="layout-warm">...</div>
{% elif locale == 'uk_UA' %}
  <div class="layout-formal">...</div>
{% else %}
  <div class="layout-minimal">...</div>
{% endif %}
```

### UI Elements That Change by Culture

| UI Element | Changes Based On | Hypothesis Addressed |
|-----------|-----------------|----------------------|
| Layout direction / density | Locale | H[X] |
| Navigation style | Locale | H[X] |
| Colour scheme / CSS class | Locale | H[X] |
| Hero imagery | Locale (locale-specific image folders) | H[X] |
| Tone of body text | Language translation | H[X] |
| Date / number formatting | Locale (Flask-Babel `format_date`) | H[X] |
| [Add more as implemented] | | |

---

## 7. Individual Contributions

> Each subsection below documents one student's contribution as required by the Phase 2 specification.

---

### 7.1 [Member 1 Name] – [Student Number]

**Pages / Features Implemented:**  
[e.g. Home page (`index.html`), language switcher logic in `routes.py`]

**Cultural Dimensions Addressed:**  
[e.g. Hofstede's Individualism/Collectivism – Ireland vs Brazil]

**Hypotheses Implemented:**  
| Hypothesis | Where in UI |
|-----------|-------------|
| H1 | [e.g. Hero image changes by locale – line 34 of index.html] |
| H2 | [e.g. CTA button text and colour – index.html lines 50–60] |

**Deviations from Group Guidelines (if any):**  
[None / or describe and justify any deviation]

---

### 7.2 [Member 2 Name] – [Student Number]

**Pages / Features Implemented:**  
[Page name and files]

**Cultural Dimensions Addressed:**  
[Dimension and countries]

**Hypotheses Implemented:**  
| Hypothesis | Where in UI |
|-----------|-------------|
| H[X] | [Location in code/UI] |

**Deviations from Group Guidelines (if any):**  
[None / justification]

---

### 7.3 [Member 3 Name] – [Student Number]

**Pages / Features Implemented:**  
[Page name and files]

**Cultural Dimensions Addressed:**  
[Dimension and countries]

**Hypotheses Implemented:**  
| Hypothesis | Where in UI |
|-----------|-------------|
| H[X] | [Location in code/UI] |

**Deviations from Group Guidelines (if any):**  
[None / justification]

---

### 7.4 [Member 4 Name] – [Student Number]

**Pages / Features Implemented:**  
[Page name and files]

**Cultural Dimensions Addressed:**  
[Dimension and countries]

**Hypotheses Implemented:**  
| Hypothesis | Where in UI |
|-----------|-------------|
| H[X] | [Location in code/UI] |

**Deviations from Group Guidelines (if any):**  
[None / justification]

---

## 8. Setup and Execution Instructions

### Environment Requirements

- Python 3.10+
- pip
- Flask, Flask-Babel (see `requirements.txt`)

### Installation

```bash
# 1. Clone the repository
git clone [repo URL]
cd Group[NUMBER]-Phase2

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Compile translations
pybabel compile -d translations

# 5. Run the application
flask run
# or
python app.py
```

### Testing Language / Cultural Switching

The language switcher is accessible via the navigation bar on every page.

| Locale | Language | Flag / Label |
|--------|----------|-------------|
| `en_IE` | English (Ireland) | 🇮🇪 English |
| `uk_UA` | Ukrainian | 🇺🇦 Українська |
| `pt_BR` | Portuguese (Brazil) | 🇧🇷 Português |

To manually test a locale, click the corresponding option in the nav. The page will reload with translated content and cultural UI adaptations applied.

### Configuration Notes

[Any additional config — e.g. setting `FLASK_APP`, `SECRET_KEY`, Babel config path, etc.]

```bash
export FLASK_APP=app
export FLASK_ENV=development
export SECRET_KEY=dev-secret-key
```

---

## 9. Limitations

- [e.g. Translations are not exhaustive — some dynamic content (e.g. error messages) may remain in English]
- [e.g. Cultural adaptations are applied at the locale level; sub-regional differences within Ukraine or Brazil are not addressed]
- [e.g. Images are locale-specific but sourced from static files — no CDN or dynamic image fetching]
- [e.g. Right-to-left (RTL) layout not required for current locales but architecture does not yet support it]
- [e.g. Application has not been tested on mobile devices]
- [Add any known bugs or incomplete features here before submission]
