"""
CrossPaths Route Definitions
All application routes and view functions
"""
import os
import uuid
from datetime import timedelta

from flask import Blueprint, render_template, session, redirect, url_for, request, flash, current_app
from flask_babel import gettext as _
from flask_login import login_user, logout_user, login_required, current_user
from PIL import Image
from sqlalchemy import select, or_, and_
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response

from app import db, SUPPORTED_LOCALES
from app.models import User, Event, Community, Interest, community_events
from app.forms import RegistrationForm, LoginForm, ProfileForm, EventForm
from app.utils import sync_user_interests, is_same_origin_referrer, utcnow

bp = Blueprint('main', __name__)


@bp.route('/health')
def health():
    """Health check: DB connectivity and tables. Returns 200 if OK, 503 if not."""
    try:
        db.session.scalars(select(Event).limit(1)).first()
        return Response('ok', status=200, mimetype='text/plain')
    except SQLAlchemyError as e:
        current_app.logger.exception("Health check failed: %s", e)
        return Response('Service temporarily unavailable', status=503, mimetype='text/plain')


# Maximum characters for the original filename portion of an upload
_MAX_FILENAME_LEN = 200


def _is_user_attending_event(user, event):
    """Return True when user is attending or organizing an event."""
    if not user or not getattr(user, 'is_authenticated', False):
        return False
    if event.organizer_id == user.id:
        return True
    return event.attendees.filter(User.id == user.id).count() > 0


def _event_attendee_count(event):
    """Count attendees, ensuring organizer is counted once."""
    count = event.attendees.count()
    if event.organizer_id and event.attendees.filter(User.id == event.organizer_id).count() == 0:
        count += 1
    return count


def _event_is_full(event):
    """True when an event has a cap and the cap is reached."""
    if not event.attendee_cap:
        return False
    return _event_attendee_count(event) >= event.attendee_cap


def _event_seats_left(event):
    """Remaining capacity, or None when uncapped."""
    if not event.attendee_cap:
        return None
    return max(event.attendee_cap - _event_attendee_count(event), 0)


def _attending_avatars(event, limit=5):
    """Return up to *limit* attendees with names + initials, organizer first."""
    attendees = []
    seen = set()
    if event.organizer:
        attendees.append(event.organizer)
        seen.add(event.organizer.id)
    for u in event.attendees.limit(limit + 1).all():
        if u.id in seen:
            continue
        attendees.append(u)
        seen.add(u.id)
        if len(attendees) >= limit:
            break
    return attendees


def _apply_when_filter(stmt, when, now):
    """Filter an event query by quick time chip ('tonight' or 'weekend')."""
    if when == 'tonight':
        end = now.replace(hour=23, minute=59, second=59, microsecond=0)
        return stmt.where(and_(Event.date_time >= now, Event.date_time <= end))
    if when == 'weekend':
        # Saturday=5, Sunday=6 in Python's weekday()
        days_until_saturday = (5 - now.weekday()) % 7
        sat = (now + timedelta(days=days_until_saturday)).replace(hour=0, minute=0, second=0, microsecond=0)
        sun_end = (sat + timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        return stmt.where(and_(Event.date_time >= sat, Event.date_time <= sun_end))
    return stmt


def _is_safe_redirect_url(target):
    """Return True only when *target* is a safe, relative URL on this host."""
    if not target:
        return False
    from urllib.parse import urlparse
    parsed = urlparse(target)
    # Accept only relative paths (no scheme, no netloc)
    return parsed.scheme == '' and parsed.netloc == ''


def _validate_image(stream):
    """Verify that the uploaded file is a genuine image using Pillow."""
    try:
        img = Image.open(stream)
        img.verify()
        stream.seek(0)
        return True
    except Exception:
        stream.seek(0)
        return False


def _safe_truncate_filename(filename, max_len=_MAX_FILENAME_LEN):
    """Truncate a filename while preserving its extension."""
    name, dot, ext = filename.rpartition('.')
    if not name:
        return filename[:max_len]
    allowed = max_len - len(ext) - len(dot)
    return f"{name[:allowed]}{dot}{ext}" if allowed > 0 else filename[:max_len]


@bp.route('/')
@bp.route('/index')
def index():
    """Home page"""
    try:
        now = utcnow()
        events = db.session.scalars(
            select(Event).where(Event.date_time >= now).order_by(Event.date_time.asc()).limit(4)
        ).all()
        communities = db.session.scalars(select(Community).limit(4)).all()
        return render_template('index.html', events=events, communities=communities)
    except SQLAlchemyError as e:
        current_app.logger.exception("Index failed (database): %s", e)
        return Response('Service temporarily unavailable', status=503, mimetype='text/plain')


@bp.route('/events')
def events():
    """Events listing page with search, city, and time-window filters."""
    city = request.args.get('city', '')
    search = request.args.get('search', '')
    when = request.args.get('when', '')
    page = request.args.get('page', 1, type=int)

    now = utcnow()
    stmt = select(Event).where(Event.date_time >= now)
    if city:
        stmt = stmt.where(Event.city == city)
    if search:
        search_pattern = f'%{search}%'
        stmt = stmt.where(
            or_(
                Event.title.ilike(search_pattern),
                Event.description.ilike(search_pattern)
            )
        )
    if when in ('tonight', 'weekend'):
        stmt = _apply_when_filter(stmt, when, now)
    stmt = stmt.order_by(Event.date_time.asc())

    pagination = db.paginate(stmt, page=page, per_page=12, error_out=False)
    attendee_counts = {event.id: _event_attendee_count(event) for event in pagination.items}
    attendee_avatars = {event.id: _attending_avatars(event, limit=5) for event in pagination.items}
    attending_event_ids = set()
    saved_event_ids = set()
    if current_user.is_authenticated:
        attending_event_ids = {
            event.id for event in pagination.items if _is_user_attending_event(current_user, event)
        }
        saved_event_ids = {e.id for e in current_user.saved_events}
    return render_template(
        'events.html',
        events=pagination.items,
        pagination=pagination,
        selected_city=city,
        search_query=search,
        selected_when=when,
        attendee_counts=attendee_counts,
        attendee_avatars=attendee_avatars,
        attending_event_ids=attending_event_ids,
        saved_event_ids=saved_event_ids,
    )


@bp.route('/event/<int:event_id>')
def event_detail(event_id):
    """Single event detail page"""
    event = db.get_or_404(Event, event_id)
    is_past_event = event.date_time < utcnow()
    is_attending = _is_user_attending_event(current_user, event)
    is_organizer = current_user.is_authenticated and event.organizer_id == current_user.id
    is_saved = (
        current_user.is_authenticated
        and any(e.id == event.id for e in current_user.saved_events)
    )
    share_url = url_for('main.event_detail', event_id=event.id, _external=True)
    return render_template(
        'event_detail.html',
        event=event,
        is_past_event=is_past_event,
        is_attending=is_attending,
        is_organizer=is_organizer,
        is_saved=is_saved,
        attendee_count=_event_attendee_count(event),
        seats_left=_event_seats_left(event),
        is_full=_event_is_full(event),
        attendee_avatars=_attending_avatars(event, limit=8),
        share_url=share_url,
    )


@bp.route('/event/<int:event_id>/confirm', methods=['GET'])
@login_required
def confirm_event(event_id):
    """Two-step confirmation page before joining (high uncertainty-avoidance flow)."""
    event = db.get_or_404(Event, event_id)
    if event.date_time < utcnow():
        flash(_('This event has already happened.'), 'warning')
        return redirect(url_for('main.event_detail', event_id=event_id))
    if _is_user_attending_event(current_user, event):
        return redirect(url_for('main.event_detail', event_id=event_id))
    if _event_is_full(event):
        flash(_('This event is fully booked.'), 'warning')
        return redirect(url_for('main.event_detail', event_id=event_id))
    return render_template(
        'event_confirm.html',
        event=event,
        attendee_count=_event_attendee_count(event),
        seats_left=_event_seats_left(event),
    )


@bp.route('/event/<int:event_id>/signup', methods=['POST'])
@login_required
def signup_event(event_id):
    """Sign up current user for an event."""
    event = db.get_or_404(Event, event_id)

    if event.date_time < utcnow():
        flash(_('This event has already happened.'), 'warning')
        return redirect(url_for('main.event_detail', event_id=event_id))

    if _is_user_attending_event(current_user, event):
        flash(_('You are already signed up for this event.'), 'info')
        return redirect(url_for('main.event_detail', event_id=event_id))

    if _event_is_full(event):
        flash(_('This event is fully booked.'), 'warning')
        return redirect(url_for('main.event_detail', event_id=event_id))

    try:
        event.attendees.append(current_user)
        # Joining clears any prior "save for later".
        if event in current_user.saved_events:
            current_user.saved_events.remove(event)
        db.session.commit()
        flash(_('You are signed up for %(name)s!', name=event.title), 'success')
    except SQLAlchemyError:
        db.session.rollback()
        current_app.logger.exception("Event signup failed")
        flash(_('An error occurred. Please try again.'), 'danger')

    return redirect(url_for('main.event_detail', event_id=event_id))


@bp.route('/event/<int:event_id>/save', methods=['POST'])
@login_required
def save_event(event_id):
    """Save an event for later without committing to attend."""
    event = db.get_or_404(Event, event_id)
    if event.date_time < utcnow():
        flash(_('This event has already happened.'), 'warning')
        return redirect(url_for('main.event_detail', event_id=event_id))
    if event not in current_user.saved_events:
        try:
            current_user.saved_events.append(event)
            db.session.commit()
            flash(_('Saved for later. We will keep it in your profile.'), 'success')
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Save event failed")
            flash(_('An error occurred. Please try again.'), 'danger')
    return redirect(url_for('main.event_detail', event_id=event_id))


@bp.route('/event/<int:event_id>/unsave', methods=['POST'])
@login_required
def unsave_event(event_id):
    """Remove a saved event from the user's list."""
    event = db.get_or_404(Event, event_id)
    if event in current_user.saved_events:
        try:
            current_user.saved_events.remove(event)
            db.session.commit()
            flash(_('Removed from your saved list.'), 'info')
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Unsave event failed")
            flash(_('An error occurred. Please try again.'), 'danger')
    return redirect(url_for('main.event_detail', event_id=event_id))


@bp.route('/event/<int:event_id>/leave', methods=['POST'])
@login_required
def leave_event(event_id):
    """Cancel current user's event signup."""
    event = db.get_or_404(Event, event_id)

    if event.date_time < utcnow():
        flash(_('You can only cancel signup before the event starts.'), 'warning')
        return redirect(url_for('main.event_detail', event_id=event_id))

    if event.organizer_id == current_user.id:
        flash(_('As the organizer, you are automatically attending this event.'), 'info')
        return redirect(url_for('main.event_detail', event_id=event_id))

    if not _is_user_attending_event(current_user, event):
        flash(_('You are not signed up for this event.'), 'info')
        return redirect(url_for('main.event_detail', event_id=event_id))

    try:
        event.attendees.remove(current_user)
        db.session.commit()
        flash(_('You are no longer signed up for %(name)s.', name=event.title), 'info')
    except SQLAlchemyError:
        db.session.rollback()
        current_app.logger.exception("Leave event failed")
        flash(_('An error occurred. Please try again.'), 'danger')

    return redirect(url_for('main.event_detail', event_id=event_id))


@bp.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    """Create a new event"""
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            agenda=(form.agenda.data or '').strip() or None,
            city=form.city.data,
            venue=form.venue.data,
            date_time=form.date_time.data,
            category=form.category.data,
            attendee_cap=form.attendee_cap.data,
            is_recurring=bool(form.is_recurring.data),
            is_cooperative=bool(form.is_cooperative.data),
            organizer_id=current_user.id
        )
        # Organizers are always counted as attendees.
        event.attendees.append(current_user)

        # Handle photo upload with content validation
        if form.photo.data:
            photo = form.photo.data
            if not _validate_image(photo.stream):
                flash(_('Uploaded file is not a valid image.'), 'danger')
                return render_template('create_event.html', form=form)

            filename = _safe_truncate_filename(secure_filename(photo.filename))
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename))
            event.photo = unique_filename

        try:
            db.session.add(event)
            db.session.commit()
            flash(_('Event created successfully!'), 'success')
            return redirect(url_for('main.events'))
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Create event failed")
            flash(_('An error occurred while creating the event. Please try again.'), 'danger')

    return render_template('create_event.html', form=form)


@bp.route('/communities')
def communities():
    """Communities listing page"""
    page = request.args.get('page', 1, type=int)
    pagination = db.paginate(select(Community), page=page, per_page=12, error_out=False)
    return render_template('communities.html', communities=pagination.items, pagination=pagination)


@bp.route('/community/<int:community_id>')
def community_detail(community_id):
    """Single community detail page"""
    community = db.get_or_404(Community, community_id)
    now = utcnow()
    upcoming_events = db.session.scalars(
        select(Event)
        .join(community_events, Event.id == community_events.c.event_id)
        .where(
            community_events.c.community_id == community_id,
            Event.date_time >= now,
        )
        .order_by(Event.date_time.asc())
        .limit(5)
    ).all()
    return render_template('community_detail.html', community=community, events=upcoming_events)


@bp.route('/community/<int:community_id>/join', methods=['POST'])
@login_required
def join_community(community_id):
    """Join a community"""
    community = db.get_or_404(Community, community_id)
    if current_user not in community.members.all():
        try:
            community.members.append(current_user)
            db.session.commit()
            flash(_('You joined %(name)s!', name=community.name), 'success')
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Join community failed")
            flash(_('An error occurred. Please try again.'), 'danger')
    else:
        flash(_('You are already a member of this community.'), 'info')
    return redirect(url_for('main.community_detail', community_id=community_id))


@bp.route('/community/<int:community_id>/leave', methods=['POST'])
@login_required
def leave_community(community_id):
    """Leave a community"""
    community = db.get_or_404(Community, community_id)
    if current_user in community.members.all():
        try:
            community.members.remove(current_user)
            db.session.commit()
            flash(_('You left %(name)s.', name=community.name), 'info')
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Leave community failed")
            flash(_('An error occurred. Please try again.'), 'danger')
    return redirect(url_for('main.community_detail', community_id=community_id))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if email already exists
        existing_user = db.session.scalars(select(User).where(User.email == form.email.data)).first()
        if existing_user:
            flash(_('Email already registered. Please log in.'), 'danger')
            return redirect(url_for('main.login'))

        chosen_locale = form.locale.data if form.locale.data in SUPPORTED_LOCALES else None
        user = User(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            gender=form.gender.data or None,
            nationality=(form.nationality.data or '').strip() or None,
            phone=(form.phone.data or '').strip() or None,
            city=form.city.data or None,
            locale=chosen_locale,
        )
        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.flush()
            sync_user_interests(user, form.interests.data, form.custom_interests.data)
            db.session.commit()
            flash(_('Account created successfully! Please log in.'), 'success')
            return redirect(url_for('main.login'))
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Registration failed")
            flash(_('An error occurred during registration. Please try again.'), 'danger')

    return render_template('register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalars(select(User).where(User.email == form.email.data)).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            # Restore the user's saved language preference, if any.
            if user.locale and user.locale in SUPPORTED_LOCALES:
                session['lang'] = user.locale
            flash(_('Welcome back!'), 'success')
            next_page = request.args.get('next')
            if _is_safe_redirect_url(next_page):
                return redirect(next_page)
            return redirect(url_for('main.index'))
        else:
            flash(_('Invalid email or password.'), 'danger')

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash(_('You have been logged out.'), 'info')
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
        current_user.gender = form.gender.data or None
        current_user.nationality = (form.nationality.data or '').strip() or None
        current_user.phone = (form.phone.data or '').strip() or None
        current_user.city = form.city.data or None
        chosen_locale = form.locale.data if form.locale.data in SUPPORTED_LOCALES else None
        current_user.locale = chosen_locale
        if chosen_locale:
            session['lang'] = chosen_locale

        try:
            sync_user_interests(
                current_user, form.interests.data, form.custom_interests.data
            )
            db.session.commit()
            flash(_('Profile updated successfully!'), 'success')
            return redirect(url_for('main.profile'))
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception("Edit profile failed")
            flash(_('An error occurred while updating your profile. Please try again.'), 'danger')

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.age.data = current_user.age
        form.gender.data = current_user.gender or ''
        form.nationality.data = current_user.nationality
        form.phone.data = current_user.phone
        form.city.data = current_user.city or ''
        form.locale.data = current_user.locale or ''
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
    """Handle language switching. Redirect only to same-origin URLs to avoid open redirect."""
    locale = request.form.get('locale', 'en_IE')

    if locale in SUPPORTED_LOCALES:
        session['lang'] = locale
        # Persist the choice for logged-in users so it survives logout/login.
        if current_user.is_authenticated:
            try:
                current_user.locale = locale
                db.session.commit()
            except SQLAlchemyError:
                db.session.rollback()
                current_app.logger.exception("Persist user locale failed")

    if is_same_origin_referrer(request, request.referrer):
        return redirect(request.referrer)
    return redirect(url_for('main.index'))
