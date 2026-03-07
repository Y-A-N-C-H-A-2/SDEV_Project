# CrossPaths - Quick Start Guide

## ✅ Project Structure Created Successfully!

All files and folders have been created according to the architecture specification.

## 🚀 Next Steps to Run the Application

### 1. Set up Python Virtual Environment

```bash
cd /Users/yanachulovska/SDEV_Project/CrossPaths

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Compile Translations

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

**Issue: "No module named 'flask'"**
- Solution: Make sure virtual environment is activated and dependencies are installed

**Issue: "Translations not working"**
- Solution: Compile translations with `pybabel compile -d translations`

**Issue: "Template not found"**
- Solution: Check that templates/ folder is at the root level, not inside app/

**Issue: "Static files not loading"**
- Solution: Check that static/ folder is at the root level, not inside app/

## 📧 Support

For questions about the project structure or implementation, refer to the main README.md
in /Users/yanachulovska/SDEV_Project/README.md

---

**Happy Coding! 🎉**
