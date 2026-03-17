"""
CrossPaths Flask Application Factory
Culturally adaptive speed-friending platform
"""
import logging
import os
from pathlib import Path

import click
from flask import Flask, g, request
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from babel.messages import mofile, pofile

# Initialize extensions
babel = Babel()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
csrf = CSRFProtect()


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
    Checks URL prefix (view args) first, then session, then accepts-language.
    """
    from flask import session
    # URL prefix locale (/<locale>/...) wins for culturally adaptive pages.
    url_locale = None
    if request and request.view_args:
        url_locale = request.view_args.get('locale')
    if not url_locale and hasattr(g, 'url_locale'):
        url_locale = getattr(g, 'url_locale')
    if url_locale in ['en_IE', 'uk_UA', 'pt_BR']:
        session['lang'] = url_locale
        return url_locale

    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(['en_IE', 'uk_UA', 'pt_BR']) or 'en_IE'

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    translation_dir = (Path(app.root_path).parent / 'translations').resolve()

    # Configuration — require SECRET_KEY in production
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        if os.environ.get('FLASK_ENV') == 'production':
            raise RuntimeError(
                "SECRET_KEY environment variable is not set. "
                "A secret key is required in production to secure sessions and CSRF tokens."
            )
        secret_key = 'dev-secret-key'
    app.config['SECRET_KEY'] = secret_key

    app.config['BABEL_DEFAULT_LOCALE'] = 'en_IE'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['en_IE', 'uk_UA', 'pt_BR']
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = str(translation_dir)

    # Database configuration
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Heroku provides 'postgres://' URLs but SQLAlchemy 1.4+ requires 'postgresql://'
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Default to SQLite for local development; use PostgreSQL in production
        db_path = os.path.join(Path(app.root_path).parent, 'crosspaths.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Upload configuration
    app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Ensure production dynos can use translations
    _compile_translations_if_needed(translation_dir)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # Register routes
    from app import routes
    app.register_blueprint(routes.bp)

    # Locale-prefixed MVP routes (/<locale>/...)
    from app.crosspaths_mvp import bp as crosspaths_bp
    app.register_blueprint(crosspaths_bp)

    # Context processor to inject locale into all templates
    @app.context_processor
    def inject_locale():
        from flask_babel import format_date
        return dict(locale=get_locale(), format_date=format_date)

    @app.before_request
    def _capture_url_locale():
        if request and request.view_args:
            loc = request.view_args.get('locale')
            if loc in app.config['BABEL_SUPPORTED_LOCALES']:
                g.url_locale = loc

    # ---------- CLI commands (replaces automatic db.create_all / seed) ----------
    @app.cli.command('init-db')
    def init_db_command():
        """Create all database tables."""
        from app import models  # noqa: F401
        db.create_all()
        click.echo('Database tables created.')

    @app.cli.command('seed-db')
    def seed_db_command():
        """Seed the database with sample data."""
        from app.seed import seed_database
        seed_database()
        click.echo('Database seeding complete.')

    return app