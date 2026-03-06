"""
CrossPaths Route Definitions
All application routes and view functions
"""
from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_babel import gettext as _

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    """Home page (Yana)"""
    return render_template('index.html')

@bp.route('/events')
def events():
    """Events listing page (Lívia)"""
    # Sample event data - in production this would come from a database
    sample_events = [
        {
            'id': 1,
            'title': _('Friday Night Speed-Friending'),
            'date': '2026-03-13',
            'time': '19:00',
            'location': 'The Bernard Shaw, Dublin 8',
            'attendees': 12,
            'max_attendees': 20,
            'host': 'Maria Kelly',
            'verified': True
        },
        {
            'id': 2,
            'title': _('Coffee Connections'),
            'date': '2026-03-15',
            'time': '11:00',
            'location': 'Kaph Café, Drury Street',
            'attendees': 8,
            'max_attendees': 15,
            'host': 'John O\'Brien',
            'verified': True
        }
    ]
    return render_template('events.html', events=sample_events)

@bp.route('/profile')
def profile():
    """User profile page (Kashish)"""
    # Sample profile data - in production this would come from a database
    sample_profile = {
        'name': 'Sample User',
        'age': 28,
        'country': 'Ukraine',
        'languages': ['Ukrainian', 'English', 'Russian'],
        'interests': ['Photography', 'Hiking', 'Coffee'],
        'bio': _('Looking to meet new friends in Dublin!')
    }
    return render_template('profile.html', profile=sample_profile)

@bp.route('/about')
def about():
    """About / community page (Simphiwe)"""
    return render_template('about.html')

@bp.route('/set-language', methods=['POST'])
def set_language():
    """Handle language switching"""
    locale = request.form.get('locale', 'en_IE')
    
    # Validate locale
    if locale in ['en_IE', 'uk_UA', 'pt_BR']:
        session['lang'] = locale
    
    # Redirect back to the referring page or home
    return redirect(request.referrer or url_for('main.index'))
