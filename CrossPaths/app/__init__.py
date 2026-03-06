"""
CrossPaths Flask Application Factory
Culturally adaptive speed-friending platform
"""
from flask import Flask, request
from flask_babel import Babel

# Initialize Babel instance
babel = Babel()

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
    # Configuration
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['BABEL_DEFAULT_LOCALE'] = 'en_IE'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['en_IE', 'uk_UA', 'pt_BR']
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'
    
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