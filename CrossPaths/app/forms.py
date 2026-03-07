"""
CrossPaths Forms
"""
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, IntegerField, SelectField, TextAreaField, DateTimeLocalField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange, ValidationError


CITY_CHOICES = [
    ('', _l('Select a city...')),
    ('Dublin', 'Dublin'),
    ('Galway', 'Galway'),
    ('Cork', 'Cork'),
    ('Limerick', 'Limerick'),
    ('Waterford', 'Waterford'),
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

PREDEFINED_INTERESTS = [
    'Language exchange', 'Travel', 'Hiking', 'Photography', 'Music',
    'Art', 'Tech', 'Sports', 'Food and coffee', 'Nightlife', 'Cultural events'
]


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class RegistrationForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(_l('Confirm Password'), validators=[DataRequired(), EqualTo('password', message=_l('Passwords must match'))])
    age = IntegerField(_l('Age'), validators=[Optional(), NumberRange(min=16, max=120)])
    gender = SelectField(_l('Gender'), choices=GENDER_CHOICES, validators=[Optional()])
    nationality = StringField(_l('Nationality'), validators=[Optional(), Length(max=60)])
    city = SelectField(_l('City in Ireland'), choices=CITY_CHOICES, validators=[Optional()])
    interests = MultiCheckboxField(_l('Interests'), choices=[(i, i) for i in PREDEFINED_INTERESTS])
    custom_interests = StringField(_l('Custom Interests (comma-separated)'), validators=[Optional()])


class LoginForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])


class ProfileForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired(), Length(min=2, max=100)])
    age = IntegerField(_l('Age'), validators=[Optional(), NumberRange(min=16, max=120)])
    gender = SelectField(_l('Gender'), choices=GENDER_CHOICES, validators=[Optional()])
    nationality = StringField(_l('Nationality'), validators=[Optional(), Length(max=60)])
    city = SelectField(_l('City in Ireland'), choices=CITY_CHOICES, validators=[Optional()])
    interests = MultiCheckboxField(_l('Interests'), choices=[(i, i) for i in PREDEFINED_INTERESTS])
    custom_interests = StringField(_l('Custom Interests (comma-separated)'), validators=[Optional()])


class EventForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired(), Length(max=200)])
    description = TextAreaField(_l('Description'), validators=[Optional()])
    city = SelectField(_l('City'), choices=CITY_CHOICES, validators=[DataRequired()])
    venue = StringField(_l('Location/Venue'), validators=[Optional(), Length(max=200)])
    date_time = DateTimeLocalField(_l('Date and Time'), format=['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S'], validators=[DataRequired()])
    category = SelectField(_l('Category'), choices=CATEGORY_CHOICES, validators=[Optional()])
    photo = FileField(_l('Event Photo'), validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], _l('Images only!'))])
