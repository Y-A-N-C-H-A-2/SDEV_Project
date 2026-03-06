"""
CrossPaths Utility Functions
Helper functions for locale detection and other utilities
"""
from flask import session, request

def get_locale():
    """
    Determine the best locale to use for the request.
    Checks session first, then accepts language header.
    Returns one of: en_IE, uk_UA, pt_BR
    """
    # Check if user has manually selected a locale
    if 'lang' in session:
        return session['lang']
    
    # Use request accept languages as fallback
    return request.accept_languages.best_match(['en_IE', 'uk_UA', 'pt_BR']) or 'en_IE'

def get_cultural_layout_class(locale):
    """
    Return the CSS class name for cultural layout adaptation
    """
    layout_map = {
        'en_IE': 'layout-minimal',
        'uk_UA': 'layout-formal',
        'pt_BR': 'layout-warm'
    }
    return layout_map.get(locale, 'layout-minimal')

def get_locale_display_name(locale):
    """
    Return human-readable name for locale
    """
    names = {
        'en_IE': 'English (Ireland)',
        'uk_UA': 'Українська (Ukraine)',
        'pt_BR': 'Português (Brasil)'
    }
    return names.get(locale, 'English (Ireland)')
