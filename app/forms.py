"""
CrossPaths Forms
"""
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField, PasswordField, IntegerField, SelectField, TextAreaField,
    DateTimeLocalField, SelectMultipleField, BooleanField, widgets,
)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange, Regexp, ValidationError

from app.utils import utcnow


def validate_future_date(_form, field):
    """Ensure date_time is in the future."""
    if field.data and field.data <= utcnow():
        raise ValidationError(_l('Event date and time must be in the future.'))


LOCALE_CHOICES = [
    ('', _l('Use browser language')),
    ('en_IE', _l('English (Ireland)')),
    ('uk_UA', _l('Ukrainian (interface language)')),
    ('pt_BR', _l('Portuguese (Brazil)')),
]

# Lenient international phone format: optional leading +, digits/spaces/dashes/parens
PHONE_REGEX = r'^\+?[0-9 \-\(\)]{6,20}$'


CITY_CHOICES = [
    ('', _l('Select a city...')),
    ('Dublin', _l('Dublin')),
    ('Galway', _l('Galway')),
    ('Cork', _l('Cork')),
    ('Limerick', _l('Limerick')),
    ('Waterford', _l('Waterford')),
]

GENDER_CHOICES = [
    ('', _l('Select...')),
    ('Male', _l('Male')),
    ('Female', _l('Female')),
    ('Non-binary', _l('Non-binary')),
    ('Prefer not to say', _l('Prefer not to say')),
]

CATEGORY_CHOICES = [
    ('', _l('Select a category...')),
    ('Social', _l('Social')),
    ('Cultural', _l('Cultural')),
    ('Outdoor', _l('Outdoor')),
    ('Language', _l('Language')),
    ('Food & Drink', _l('Food & Drink')),
    ('Art & Creative', _l('Art & Creative')),
    ('Tech', _l('Tech')),
    ('Sports', _l('Sports')),
    ('Music', _l('Music')),
    ('Travel', _l('Travel')),
    ('Nightlife', _l('Nightlife')),
    ('Photography', _l('Photography')),
]

PREDEFINED_INTEREST_CHOICES = [
    ('Language exchange', _l('Language exchange')),
    ('Travel', _l('Travel')),
    ('Hiking', _l('Hiking')),
    ('Photography', _l('Photography')),
    ('Music', _l('Music')),
    ('Art', _l('Art')),
    ('Tech', _l('Tech')),
    ('Sports', _l('Sports')),
    ('Food and coffee', _l('Food and coffee')),
    ('Nightlife', _l('Nightlife')),
    ('Cultural events', _l('Cultural events')),
]


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class RegistrationForm(FlaskForm):
    name = StringField(_l('Full name'), validators=[DataRequired(message=_l('Please enter your name.')), Length(min=2, max=100)])
    email = StringField(_l('Email'), validators=[DataRequired(message=_l('Please enter your email.')), Email(message=_l('Please enter a valid email address.'))])
    password = PasswordField(_l('Password'), validators=[DataRequired(message=_l('Please enter a password.')), Length(min=6, message=_l('Password must be at least 6 characters.'))])
    confirm_password = PasswordField(_l('Confirm Password'), validators=[DataRequired(message=_l('Please confirm your password.')), EqualTo('password', message=_l('Passwords must match'))])
    age = IntegerField(_l('Age'), validators=[Optional(), NumberRange(min=16, max=120, message=_l('Age must be between 16 and 120.'))])
    gender = SelectField(_l('Gender'), choices=GENDER_CHOICES, validators=[Optional()])
    nationality = StringField(_l('Nationality'), validators=[Optional(), Length(max=60)])
    phone = StringField(_l('Phone (optional, with country code)'), validators=[Optional(), Regexp(PHONE_REGEX, message=_l('Please enter a valid phone number.'))])
    city = SelectField(_l('City in Ireland'), choices=CITY_CHOICES, validators=[Optional()])
    locale = SelectField(_l('Preferred language'), choices=LOCALE_CHOICES, validators=[Optional()])
    interests = MultiCheckboxField(_l('Interests'), choices=PREDEFINED_INTEREST_CHOICES)
    custom_interests = StringField(_l('Custom Interests (comma-separated)'), validators=[Optional()])


class LoginForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(message=_l('Please enter your email.')), Email(message=_l('Please enter a valid email address.'))])
    password = PasswordField(_l('Password'), validators=[DataRequired(message=_l('Please enter your password.'))])


class ProfileForm(FlaskForm):
    name = StringField(_l('Full name'), validators=[DataRequired(message=_l('Please enter your name.')), Length(min=2, max=100)])
    age = IntegerField(_l('Age'), validators=[Optional(), NumberRange(min=16, max=120, message=_l('Age must be between 16 and 120.'))])
    gender = SelectField(_l('Gender'), choices=GENDER_CHOICES, validators=[Optional()])
    nationality = StringField(_l('Nationality'), validators=[Optional(), Length(max=60)])
    phone = StringField(_l('Phone (optional, with country code)'), validators=[Optional(), Regexp(PHONE_REGEX, message=_l('Please enter a valid phone number.'))])
    city = SelectField(_l('City in Ireland'), choices=CITY_CHOICES, validators=[Optional()])
    locale = SelectField(_l('Preferred language'), choices=LOCALE_CHOICES, validators=[Optional()])
    interests = MultiCheckboxField(_l('Interests'), choices=PREDEFINED_INTEREST_CHOICES)
    custom_interests = StringField(_l('Custom Interests (comma-separated)'), validators=[Optional()])


class EventForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired(message=_l('Please give your event a title.')), Length(max=200)])
    description = TextAreaField(_l('Description'), validators=[Optional()])
    agenda = TextAreaField(_l('Agenda (one item per line)'), validators=[Optional()],
                           description=_l('A clear schedule helps people decide whether to attend.'))
    city = SelectField(_l('City'), choices=CITY_CHOICES, validators=[DataRequired(message=_l('Please choose a city.'))])
    venue = StringField(_l('Location/Venue'), validators=[Optional(), Length(max=200)])
    date_time = DateTimeLocalField(_l('Date and Time'), format=['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S'], validators=[DataRequired(message=_l('Please choose a date and time.')), validate_future_date])
    category = SelectField(_l('Category'), choices=CATEGORY_CHOICES, validators=[Optional()])
    attendee_cap = IntegerField(_l('Attendee limit (optional)'), validators=[Optional(), NumberRange(min=1, max=10000, message=_l('Attendee limit must be a positive number.'))])
    is_recurring = BooleanField(_l('Recurring event (meets regularly)'))
    is_cooperative = BooleanField(_l('Cooperative event (no competition, everyone welcome)'), default=True)
    photo = FileField(_l('Event Photo'), validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], _l('Images only!'))])
