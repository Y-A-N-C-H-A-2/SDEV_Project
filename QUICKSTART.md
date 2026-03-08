# CrossPaths - Quick Start Guide

## ✅ Project Structure Created Successfully!

All files and folders have been created according to the architecture specification.

## 🚀 Next Steps to Run the Application

### 1. Set up Python Virtual Environment

```bash
cd /Users/yanachulovska/SDEV_Project

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
```

### 2. Install Dependencies

**From the project root** (where `requirements.txt` lives). The app uses SQLite by default; no PostgreSQL needed for local dev.

```bash
# With venv activated:
pip install -r requirements.txt
```

### 3. Compile Translations

**Run from the project root** (where the `translations` folder lives).

```bash
# This compiles the .po files into .mo files that Flask-Babel needs
pybabel compile -d translations
```

### 4. Run the Application

```bash
# Set environment variable
export FLASK_ENV=development

# Run the app
python run.py
```

### 5. Open in Browser

Navigate to: http://127.0.0.1:5000

### 6. Test Locale Switching

Click on the flag buttons in the navigation bar to switch between:
- 🇮🇪 EN (English - Ireland) - Minimal, direct interface
- 🇺🇦 UK (Ukrainian) - Formal, structured with safety features
- 🇧🇷 PT (Brazilian Portuguese) - Warm, social, expressive

## 📝 What's Included

✅ Flask application with Babel internationalization
✅ Three locale-specific interfaces (en_IE, uk_UA, pt_BR)
✅ Culturally adaptive CSS styling
✅ Complete translation files for all three locales
✅ Four main pages: Home, Events, Profile, About
✅ Sample event data and profile information
✅ Language switcher in navigation
✅ Responsive design

## 🎨 Cultural Adaptations

### Ukrainian (uk_UA)
- Formal, structured layouts
- Verified host badges
- Detailed safety information
- Soft pastel periwinkle/lavender color scheme

### Brazilian Portuguese (pt_BR)
- Warm orange color palette (Bumble BFF-inspired)
- Social proof elements
- Expressive language with emojis
- Community-focused messaging

### English/Irish (en_IE)
- Clean, minimal design
- Direct, concise copy
- Soft sage/mint pastel colors
- Self-directed navigation

## 🔧 Development Tips

### Update Translations
After modifying text in templates or Python files:
```bash
# Extract new strings
pybabel extract -F babel.cfg -o messages.pot .

# Update translation files
pybabel update -i messages.pot -d translations

# Edit the .po files in translations/*/LC_MESSAGES/
# Then compile
pybabel compile -d translations
```

### Add New Pages
1. Create HTML template in `templates/`
2. Add route in `app/routes.py`
3. Add translations to all `.po` files
4. Compile translations

## 📚 File Overview

- **app/__init__.py** - Flask app factory with Babel setup
- **app/routes.py** - All page routes and language switcher
- **app/utils.py** - Locale detection helpers
- **templates/*.html** - Jinja2 templates with cultural variations
- **static/css/main.css** - Locale-specific styling
- **static/js/main.js** - Client-side cultural adaptations
- **translations/*/LC_MESSAGES/messages.po** - Translation strings
- **run.py** - Application entry point

## 🐛 Troubleshooting

**Issue: "No module named 'flask_babel'" or "No module named 'flask'"**
- Activate the venv: `source venv/bin/activate` (from project root).
- Install deps: from project root, `pip install -r requirements.txt`.

**Issue: "Could not open requirements file"**
- Run `pip install -r requirements.txt` from the **project root**.

**Issue: "Failed to build psycopg2-binary" / "pg_config executable not found"**
- Root `requirements.txt` includes psycopg2-binary for Heroku; the app uses SQLite when `DATABASE_URL` is not set.
- For PostgreSQL later: install client libs (e.g. `brew install postgresql` on macOS) then `pip install psycopg2-binary==2.9.9`.

**Issue: "No such file or directory: 'translations'"**
- Run `pybabel compile -d translations` from the **project root** (where the `translations` folder lives).

**Issue: "Translations not working"**
- From project root, compile translations: `pybabel compile -d translations`.

**Issue: "Template not found"**
- Check that `templates/` is at project root, not inside `app/`

**Issue: "Static files not loading"**
- Check that `static/` is at project root, not inside `app/`

## 📧 Support

For questions about the project structure or implementation, refer to the main README.md
in /Users/yanachulovska/SDEV_Project/README.md

---

**Happy Coding! 🎉**
