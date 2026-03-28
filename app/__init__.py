"""
CrossPaths Flask Application Factory
Culturally adaptive community events platform
"""
import logging
import os
import sys
from pathlib import Path

import click
from flask import Flask, request
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
        except Exception as e:
            logging.exception("Failed to compile translation catalog for locale '%s'", locale_dir.name)
            # Ensure failure is visible in server logs (e.g. read-only filesystem)
            print(
                f"[CrossPaths] Translation compile failed for {locale_dir.name}: {e}. "
                "Ensure .mo files are committed or filesystem is writable.",
                file=sys.stderr,
            )

def get_locale():
    """
    Determine the best locale to use for the request.
    Checks session first, then accepts language header.
    """
    from flask import session
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(['en_IE', 'uk_UA', 'pt_BR']) or 'en_IE'

def create_app():
    """Create and configure the Flask application"""
    # Use absolute paths so templates/static/translations resolve regardless of CWD
    _project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=str(_project_root / 'templates'),
        static_folder=str(_project_root / 'static'),
    )
    translation_dir = (_project_root / 'translations').resolve()

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

    # Database configuration (optional DATABASE_URL for PostgreSQL in production)
    database_url = (os.environ.get('DATABASE_URL') or '').strip()
    if database_url:
        # Some hosts use postgres://; SQLAlchemy 1.4+ expects postgresql://
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        # Managed Postgres often requires SSL; add sslmode=require if not already present
        if 'postgresql://' in database_url and 'sslmode=' not in database_url:
            separator = '&' if '?' in database_url else '?'
            database_url = f'{database_url}{separator}sslmode=require'
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Default to SQLite for local development; use PostgreSQL in production
        db_path = str(_project_root / 'crosspaths.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Upload configuration
    app.config['UPLOAD_FOLDER'] = str(_project_root / 'static' / 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

    # Ensure upload directory exists (skip on read-only filesystem)
    try:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    except OSError as e:
        logging.warning("Could not create upload folder %s: %s", app.config['UPLOAD_FOLDER'], e)

    # Ensure production can use translations
    _compile_translations_if_needed(translation_dir)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    # User loader for Flask-Login (harden against invalid/tampered user_id in session)
    @login_manager.user_loader
    def load_user(user_id):
        if user_id is None:
            return None
        try:
            uid = int(user_id)
            if uid <= 0:
                return None
        except (ValueError, TypeError):
            return None
        from app.models import User
        return db.session.get(User, uid)

    # Register routes
    from app import routes
    app.register_blueprint(routes.bp)

    # Context processor to inject locale into all templates
    @app.context_processor
    def inject_locale():
        return dict(locale=get_locale())

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