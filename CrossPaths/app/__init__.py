"""
CrossPaths Flask Application Factory
Culturally adaptive speed-friending platform
"""
import logging
import os
from pathlib import Path

from flask import Flask, request
from flask_babel import Babel
from babel.messages import mofile, pofile

# Initialize Babel instance
babel = Babel()


def _compile_translations_if_needed(translation_dir: Path) -> None:
    """Compile .po files into .mo files when missing or outdated."""
    if not translation_dir.exists():
        logging.warning("Translation directory not found: %s", translation_dir)
        return

    for locale_dir in translation_dir.iterdir():
        if not locale_dir.is_dir():
            continue

        po_path = locale_dir / 'LC_MESSAGES' / 'messages.po'
        mo_path = locale_dir / 'LC_MESSAGES' / 'messages.mo'

        if not po_path.exists():
            continue

        needs_compile = (not mo_path.exists()) or (po_path.stat().st_mtime > mo_path.stat().st_mtime)
        if not needs_compile:
            continue

        try:
            with po_path.open('rb') as po_file:
                catalog = pofile.read_po(po_file)
            with mo_path.open('wb') as mo_file:
                mofile.write_mo(mo_file, catalog)
            logging.info("Compiled translation catalog: %s", mo_path)
        except Exception:
            logging.exception("Failed to compile translation catalog for locale '%s'", locale_dir.name)

def get_locale():
    """
    Determine the best locale to use for the request.
    Checks session first, then accepts language header.
    """
    from flask import session
    # Check if user has manually selected a locale
    if 'lang' in session:
        return session['lang']
    # Use request accept languages as fallback
    return request.accept_languages.best_match(['en_IE', 'uk_UA', 'pt_BR']) or 'en_IE'

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    translation_dir = (Path(app.root_path).parent / 'translations').resolve()

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['BABEL_DEFAULT_LOCALE'] = 'en_IE'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['en_IE', 'uk_UA', 'pt_BR']
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = str(translation_dir)

    # Ensure production dynos can use translations even when .mo files are not committed.
    _compile_translations_if_needed(translation_dir)
    
    # Initialize Babel with app
    babel.init_app(app, locale_selector=get_locale)
    
    # Register routes
    from app import routes
    app.register_blueprint(routes.bp)
    
    # Context processor to inject locale into all templates
    @app.context_processor
    def inject_locale():
        return dict(locale=get_locale())
    
    return app