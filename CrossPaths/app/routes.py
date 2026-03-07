"""
CrossPaths Route Definitions
All application routes and view functions
"""
import os
import uuid
from datetime import datetime

from flask import Blueprint, render_template, session, redirect, url_for, request, flash, current_app
from flask_babel import gettext as _
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename

from app import db
from app.models import User, Event, Community, Interest
from app.forms import RegistrationForm, LoginForm, ProfileForm, EventForm, PREDEFINED_INTERESTS

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    """Home page"""
    events = Event.query.filter(Event.date_time >= datetime.utcnow()).order_by(Event.date_time.asc()).limit(4).all()
    communities = Community.query.limit(4).all()
    return render_template('index.html', events=events, communities=communities)


@bp.route('/events')
def events():
    """Events listing page with search and city filter"""
    city = request.args.get('city', '')
    search = request.args.get('search', '')

    query = Event.query.filter(Event.date_time >= datetime.utcnow())

    if city:
        query = query.filter(Event.city == city)
    if search:
        query = query.filter(
            db.or_(
                Event.title.ilike(f'%{search}%'),
                Event.description.ilike(f'%{search}%')
            )
        )

    events_list = query.order_by(Event.date_time.asc()).all()
    return render_template('events.html', events=events_list, selected_city=city, search_query=search)


@bp.route('/event/<int:event_id>')
def event_detail(event_id):
    """Single event detail page"""
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)


@bp.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    """Create a new event"""
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            city=form.city.data,
            venue=form.venue.data,
            date_time=form.date_time.data,
            category=form.category.data,
            organizer_id=current_user.id
        )

        # Handle photo upload
        if form.photo.data:
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename))
            event.photo = unique_filename

        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('main.events'))

    return render_template('create_event.html', form=form)


@bp.route('/communities')
def communities():
    """Communities listing page"""
    communities_list = Community.query.all()
    return render_template('communities.html', communities=communities_list)


@bp.route('/community/<int:community_id>')
def community_detail(community_id):
    """Single community detail page"""
    community = Community.query.get_or_404(community_id)
    upcoming_events = Event.query.filter(Event.date_time >= datetime.utcnow()).order_by(Event.date_time.asc()).limit(5).all()
    return render_template('community_detail.html', community=community, events=upcoming_events)


@bp.route('/community/<int:community_id>/join', methods=['POST'])
@login_required
def join_community(community_id):
    """Join a community"""
    community = Community.query.get_or_404(community_id)
    if current_user not in community.members.all():
        community.members.append(current_user)
        db.session.commit()
        flash(f'You joined {community.name}!', 'success')
    else:
        flash('You are already a member of this community.', 'info')
    return redirect(url_for('main.community_detail', community_id=community_id))


@bp.route('/community/<int:community_id>/leave', methods=['POST'])
@login_required
def leave_community(community_id):
    """Leave a community"""
    community = Community.query.get_or_404(community_id)
    if current_user in community.members.all():
        community.members.remove(current_user)
        db.session.commit()
        flash(f'You left {community.name}.', 'info')
    return redirect(url_for('main.community_detail', community_id=community_id))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('main.login'))

        user = User(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            gender=form.gender.data if form.gender.data else None,
            nationality=form.nationality.data,
            city=form.city.data if form.city.data else None
        )
        user.set_password(form.password.data)

        # Handle predefined interests
        if form.interests.data:
            for interest_name in form.interests.data:
                interest = Interest.query.filter_by(name=interest_name).first()
                if interest:
                    user.interests.append(interest)

        # Handle custom interests
        if form.custom_interests.data:
            custom_list = [i.strip() for i in form.custom_interests.data.split(',') if i.strip()]
            for interest_name in custom_list:
                interest = Interest.query.filter_by(name=interest_name).first()
                if not interest:
                    interest = Interest(name=interest_name, is_predefined=False)
                    db.session.add(interest)
                user.interests.append(interest)

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Welcome back!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))


@bp.route('/profile')
@login_required
def profile():
    """User profile page"""
    return render_template('profile.html', user=current_user)


@bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Edit user profile"""
    form = ProfileForm()

    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.age = form.age.data
        current_user.gender = form.gender.data if form.gender.data else None
        current_user.nationality = form.nationality.data
        current_user.city = form.city.data if form.city.data else None

        # Update interests
        current_user.interests.clear()

        if form.interests.data:
            for interest_name in form.interests.data:
                interest = Interest.query.filter_by(name=interest_name).first()
                if interest:
                    current_user.interests.append(interest)

        if form.custom_interests.data:
            custom_list = [i.strip() for i in form.custom_interests.data.split(',') if i.strip()]
            for interest_name in custom_list:
                interest = Interest.query.filter_by(name=interest_name).first()
                if not interest:
                    interest = Interest(name=interest_name, is_predefined=False)
                    db.session.add(interest)
                current_user.interests.append(interest)

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('main.profile'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.age.data = current_user.age
        form.gender.data = current_user.gender or ''
        form.nationality.data = current_user.nationality
        form.city.data = current_user.city or ''
        # Set selected interests
        form.interests.data = [i.name for i in current_user.interests if i.is_predefined]
        custom = [i.name for i in current_user.interests if not i.is_predefined]
        form.custom_interests.data = ', '.join(custom)

    return render_template('edit_profile.html', form=form)


@bp.route('/about')
def about():
    """About / community page"""
    return render_template('about.html')


@bp.route('/set-language', methods=['POST'])
def set_language():
    """Handle language switching"""
    locale = request.form.get('locale', 'en_IE')

    if locale in ['en_IE', 'uk_UA', 'pt_BR']:
        session['lang'] = locale

    return redirect(request.referrer or url_for('main.index'))
