# CrossPaths - Culturally Adaptive Speed-Friending Platform

> *Where cultures meet and friendships begin.*

A Flask-based web application supporting the social integration of international newcomers in Dublin through culturally adaptive community-based cultural events. The platform is designed for group gatherings that bring together people from multiple countries and cultural backgrounds — not one-on-one meetings. The platform adapts its interface based on user locale (English-Ireland, Ukrainian, Brazilian Portuguese) following Hofstede's Cultural Dimensions framework.

## 🌍 Supported Locales

- **en_IE** - English (Ireland): Direct, minimal, self-directed
- **uk_UA** - Ukrainian: Formal, structured, high uncertainty avoidance
- **pt_BR** - Portuguese (Brazil): Warm, social, expressive

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd CrossPaths
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Compile translations:**
   ```bash
   pybabel compile -d translations
   ```

### Running the Application

**Development mode:**
```bash
export FLASK_ENV=development  # macOS/Linux
set FLASK_ENV=development     # Windows

python run.py
```

The application will be available at `http://127.0.0.1:5000`

## 📁 Project Structure

```
CrossPaths/
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
│   ├── event_detail.html    # Single event detail page
│   ├── create_event.html    # Event creation page
│   ├── communities.html     # Communities listing page
│   ├── community_detail.html # Single community detail page
│   ├── profile.html         # User profile page
│   ├── edit_profile.html    # Edit profile page
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   ├── about.html           # About / community page
│   └── partials/            # Locale-specific partial templates
│       ├── index/           # Home page partials per locale
│       ├── events/          # Events page partials per locale
│       ├── profile/         # Profile page partials per locale
│       └── about/           # About page partials per locale
├── static/
│   ├── css/
│   │   └── main.css         # Culturally adaptive styles
│   ├── js/
│   │   └── main.js          # Client-side functionality
│   └── img/
│       ├── common/          # Shared images
│       ├── en_IE/           # Irish/English images
│       ├── uk_UA/           # Ukrainian images
│       └── pt_BR/           # Brazilian images
├── translations/
│   ├── en_IE/LC_MESSAGES/   # English translations
│   ├── uk_UA/LC_MESSAGES/   # Ukrainian translations
│   └── pt_BR/LC_MESSAGES/   # Brazilian Portuguese translations
├── babel.cfg                # Babel extraction configuration
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md               # This file
```

## 🔄 Working with Translations

### Extract new strings from code:
```bash
pybabel extract -F babel.cfg -o messages.pot .
```

### Update existing translation files:
```bash
pybabel update -i messages.pot -d translations
```

### Compile translations after editing .po files:
```bash
pybabel compile -d translations
```

## 🎨 Cultural Adaptations

The platform implements different UI patterns based on locale:

### **Ukrainian (uk_UA) - High Uncertainty Avoidance**
- Formal, structured layouts
- Verified host badges and safety information
- Detailed event agendas and schedules
- Clear privacy and security messaging
- Step-by-step guided flows
- Soft pastel periwinkle/lavender color scheme

### **Brazilian Portuguese (pt_BR) - Relationally Driven**
- Warm orange color palette inspired by Bumble BFF
- Social feed with attendee photos
- Expressive language with emojis
- Group chat and social proof elements
- Personality-first profiles

### **English/Irish (en_IE) - Low Context, High Individualism**
- Clean, minimal design
- Direct, concise copy
- Self-directed navigation
- Fast, efficient interactions
- Soft sage/mint pastel color palette

### 🐝 Design Inspiration
The visual style is inspired by [Bumble BFF](https://www.bumble.com/bff) — featuring rounded cards, pill-shaped buttons, generous whitespace, and a warm, approachable color palette. The focus is on community-based cultural events for groups rather than one-on-one meetings.

## 🛠️ Development

### Environment Variables

Create a `.env` file for local configuration:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```

### Adding New Pages

1. Create template in `templates/`
2. Add route in `app/routes.py`
3. Add translations in all `.po` files
4. Compile translations

### Adding New Translations

1. Add `{{ _('Your text here') }}` in templates
2. Add `_('Your text here')` in Python files
3. Extract strings: `pybabel extract -F babel.cfg -o messages.pot .`
4. Update translations: `pybabel update -i messages.pot -d translations`
5. Edit `.po` files in each locale
6. Compile: `pybabel compile -d translations`

## 📝 Pages

- **/** - Home page with culturally adaptive hero and features
- **/events** - Events listing with locale-specific layouts
- **/event/<id>** - Single event detail page
- **/create-event** - Create a new event (login required)
- **/communities** - Communities listing
- **/community/<id>** - Single community detail page
- **/profile** - User profile page with cultural variations
- **/edit-profile** - Edit user profile (login required)
- **/register** - User registration
- **/login** - User login
- **/logout** - User logout
- **/about** - About page explaining the platform
- **/set-language** - Language switching endpoint

## 🌐 Language Switching

Users can switch between locales using the flag buttons in the navigation bar. The selected locale is stored in the session and persists across pages.

## 📚 Framework & Libraries

- **Flask** - Web framework
- **Flask-Babel** - Internationalization and localization
- **Flask-SQLAlchemy** - Database ORM
- **Flask-Login** - User session management
- **Flask-WTF** - Form handling and CSRF protection
- **Flask-Migrate** - Database migrations
- **Jinja2** - Template engine
- **Werkzeug** - WSGI utilities

## 👥 Contributors

Group 4 - SDEV2004 Software for Global Market

- Yana Chulovska (C24490782) - Home page
- Lívia Ferreira Guimarães Neves (C24329646) - Events page
- Kashish Kakran (D24125557) - Profile page
- Simphiwe Klassen (D24125357) - About page

## 📄 License

Academic project for TU Dublin - 2025/2026

---

*For full project documentation, see the main README.md in the parent directory.*
