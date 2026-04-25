"""
CrossPaths Database Models
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

# Association tables
user_interests = db.Table('user_interests',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
)

user_communities = db.Table('user_communities',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('community_id', db.Integer, db.ForeignKey('communities.id'), primary_key=True),
)

event_attendees = db.Table('event_attendees',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
)

saved_events = db.Table('saved_events',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
)

community_events = db.Table('community_events',
    db.Column('community_id', db.Integer, db.ForeignKey('communities.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
)


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    nationality = db.Column(db.String(60))
    city = db.Column(db.String(50))
    phone = db.Column(db.String(32))
    locale = db.Column(db.String(8))
    verified_host = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships
    interests = db.relationship('Interest', secondary=user_interests, backref=db.backref('users', lazy='dynamic'))
    communities = db.relationship('Community', secondary=user_communities, backref=db.backref('members', lazy='dynamic'))
    attending_events = db.relationship('Event', secondary=event_attendees, backref=db.backref('attendees', lazy='dynamic'))
    saved_events = db.relationship('Event', secondary=saved_events, backref=db.backref('saved_by', lazy='dynamic'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.name}>'


class Interest(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    is_predefined = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Interest {self.name}>'


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    agenda = db.Column(db.Text)
    date_time = db.Column(db.DateTime, nullable=False, index=True)
    city = db.Column(db.String(50), nullable=False, index=True)
    venue = db.Column(db.String(200))
    category = db.Column(db.String(60))
    photo = db.Column(db.String(300))
    attendee_cap = db.Column(db.Integer)
    is_recurring = db.Column(db.Boolean, default=False, nullable=False)
    is_cooperative = db.Column(db.Boolean, default=True, nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    organizer = db.relationship(
        'User',
        foreign_keys=[organizer_id],
        backref=db.backref('organized_events', lazy='dynamic'),
    )

    def __repr__(self):
        return f'<Event {self.title}>'


class Community(db.Model):
    __tablename__ = 'communities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(300))

    # Relationships
    events = db.relationship('Event', secondary=community_events, backref=db.backref('communities', lazy='dynamic'))
