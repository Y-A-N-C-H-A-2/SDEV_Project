"""
CrossPaths Forms
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, IntegerField, SelectField, TextAreaField, DateTimeLocalField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange, ValidationError


CITY_CHOICES = [
    ('', 'Select a city...'),
    ('Dublin', 'Dublin'),
    ('Galway', 'Galway'),
    ('Cork', 'Cork'),
    ('Limerick', 'Limerick'),
    ('Waterford', 'Waterford'),
]

GENDER_CHOICES = [
    ('', 'Select...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Non-binary', 'Non-binary'),
    ('Prefer not to say', 'Prefer not to say'),
]

CATEGORY_CHOICES = [
    ('', 'Select a category...'),
    ('Social', 'Social'),
    ('Cultural', 'Cultural'),
    ('Outdoor', 'Outdoor'),
    ('Language', 'Language'),
    ('Food & Drink', 'Food & Drink'),
    ('Art & Creative', 'Art & Creative'),
    ('Tech', 'Tech'),
    ('Sports', 'Sports'),
    ('Music', 'Music'),
    ('Travel', 'Travel'),
    ('Nightlife', 'Nightlife'),
    ('Photography', 'Photography'),
]

PREDEFINED_INTERESTS = [
    'Language exchange', 'Travel', 'Hiking', 'Photography', 'Music',
    'Art', 'Tech', 'Sports', 'Food and coffee', 'Nightlife', 'Cultural events'
]


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=16, max=120)])
    gender = SelectField('Gender', choices=GENDER_CHOICES, validators=[Optional()])
    nationality = StringField('Nationality', validators=[Optional(), Length(max=60)])
    city = SelectField('City in Ireland', choices=CITY_CHOICES, validators=[Optional()])
    interests = MultiCheckboxField('Interests', choices=[(i, i) for i in PREDEFINED_INTERESTS])
    custom_interests = StringField('Custom Interests (comma-separated)', validators=[Optional()])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=16, max=120)])
    gender = SelectField('Gender', choices=GENDER_CHOICES, validators=[Optional()])
    nationality = StringField('Nationality', validators=[Optional(), Length(max=60)])
    city = SelectField('City in Ireland', choices=CITY_CHOICES, validators=[Optional()])
    interests = MultiCheckboxField('Interests', choices=[(i, i) for i in PREDEFINED_INTERESTS])
    custom_interests = StringField('Custom Interests (comma-separated)', validators=[Optional()])


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[Optional()])
    city = SelectField('City', choices=CITY_CHOICES, validators=[DataRequired()])
    venue = StringField('Location/Venue', validators=[Optional(), Length(max=200)])
    date_time = DateTimeLocalField('Date and Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    category = SelectField('Category', choices=CATEGORY_CHOICES, validators=[Optional()])
    photo = FileField('Event Photo', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
