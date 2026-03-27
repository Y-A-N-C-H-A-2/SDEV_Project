"""
CrossPaths Database Seed Data
"""
from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.exc import ProgrammingError

from app import db
from app.models import Interest, Event, Community

PREDEFINED_INTERESTS = [
    'Language exchange', 'Travel', 'Hiking', 'Photography', 'Music',
    'Art', 'Tech', 'Sports', 'Food and coffee', 'Nightlife', 'Cultural events'
]

SAMPLE_EVENTS = [
    {
        'title': 'Trip to Galway with a Castle Visit',
        'description': 'Join us for an amazing day trip to Galway! We will visit the historic Dunguaire Castle, explore the colorful streets of Galway city, and enjoy traditional Irish music in a local pub.',
        'date_time': datetime.utcnow() + timedelta(days=14),
        'city': 'Galway',
        'venue': 'Dunguaire Castle, Kinvara',
        'category': 'Travel',
        'photo': 'event_galway.png',
    },
    {
        'title': 'Wicklow Mountains Hiking Trip',
        'description': 'Experience the breathtaking beauty of the Wicklow Mountains. This moderate-level hike takes us through Glendalough valley with stunning views of the upper and lower lakes.',
        'date_time': datetime.utcnow() + timedelta(days=7),
        'city': 'Dublin',
        'venue': 'Glendalough, Co. Wicklow',
        'category': 'Outdoor',
        'photo': 'event_wicklow_hike.png',
    },
    {
        'title': 'Wednesday Filming Locations Tour in Wicklow',
        'description': 'Explore the magical filming locations of the Wednesday series in County Wicklow. Visit the stunning landscapes that served as the backdrop for Nevermore Academy.',
        'date_time': datetime.utcnow() + timedelta(days=21),
        'city': 'Dublin',
        'venue': 'Killruddery House, Bray, Co. Wicklow',
        'category': 'Cultural',
        'photo': 'event_wednesday_wicklow.png',
    },
    {
        'title': 'International Meetup in Dublin',
        'description': 'Meet people from all over the world living in Dublin! This casual meetup is perfect for newcomers and anyone looking to expand their social circle in the city.',
        'date_time': datetime.utcnow() + timedelta(days=3),
        'city': 'Dublin',
        'venue': 'The Bernard Shaw, Dublin 8',
        'category': 'Social',
        'photo': 'event_galway.png',
    },
    {
        'title': 'Language Exchange Night',
        'description': 'Practice languages while making new friends! Bring your enthusiasm for learning and share your native language. All levels welcome.',
        'date_time': datetime.utcnow() + timedelta(days=5),
        'city': 'Dublin',
        'venue': 'Cafe en Seine, Dawson Street',
        'category': 'Language',
        'photo': 'event_wicklow.png',
    },
    {
        'title': 'Photography Walk',
        'description': "Join fellow photography enthusiasts for a guided walk through Dublin's most photogenic spots. Bring any camera — phone cameras are welcome too!",
        'date_time': datetime.utcnow() + timedelta(days=10),
        'city': 'Dublin',
        'venue': "Meeting at Ha'penny Bridge, Dublin",
        'category': 'Photography',
        'photo': 'event_photography.png',
    },
    {
        'title': 'Coffee Meetup for Newcomers in Ireland',
        'description': 'New to Ireland? Come for a relaxed coffee meetup and meet other newcomers. Share tips, stories, and make lasting connections over great coffee.',
        'date_time': datetime.utcnow() + timedelta(days=2),
        'city': 'Cork',
        'venue': "Filter Coffee, George's Quay, Cork",
        'category': 'Food & Drink',
        'photo': 'event_meetup.png',
    },
    {
        'title': 'Pub Social Night',
        'description': 'Experience the famous Irish pub culture! Join us for a fun night of live music, great craic, and the best Guinness in town.',
        'date_time': datetime.utcnow() + timedelta(days=4),
        'city': 'Limerick',
        'venue': "Dolan's Pub, Limerick",
        'category': 'Nightlife',
        'photo': 'event_pub.png',
    },
    {
        'title': 'Art and Creativity Workshop',
        'description': 'Unleash your creative side in this hands-on art workshop. No experience needed — just bring your curiosity and willingness to try something new!',
        'date_time': datetime.utcnow() + timedelta(days=12),
        'city': 'Waterford',
        'venue': 'Garter Lane Arts Centre, Waterford',
        'category': 'Art & Creative',
        'photo': 'event_art.png',
    },
]

SAMPLE_COMMUNITIES = [
    {
        'name': 'Language Exchange Community',
        'description': 'Connect with language learners and native speakers. Practice your target language in a friendly, supportive environment through regular meetups and events.',
        'image': 'event_language_exchange.png',
    },
    {
        'name': 'Hiking Ireland',
        'description': "Explore Ireland's stunning trails and mountains together. From gentle coastal walks to challenging mountain hikes, there's something for everyone.",
        'image': 'event_wicklow.png',
    },
    {
        'name': 'International Friends in Dublin',
        'description': 'A welcoming community for internationals living in Dublin. Meet people from around the world, share experiences, and build lasting friendships.',
        'image': 'event_pub.png',
    },
    {
        'name': 'Photography Club',
        'description': "For photographers of all levels! Share your work, learn new techniques, and join photo walks around Ireland's most beautiful locations.",
        'image': 'event_photography_club.png',
    },
    {
        'name': 'Tech and Startups Ireland',
        'description': 'Connect with tech professionals, startup founders, and anyone interested in the Irish tech scene. Networking events, talks, and hackathons.',
        'image': 'event_tech_startups.png',
    },
    {
        'name': 'Art and Creativity',
        'description': 'A space for artists, creatives, and art enthusiasts. From painting workshops to gallery visits, let creativity bring us together.',
        'image': 'event_art.png',
    },
    {
        'name': 'Travel Buddies',
        'description': 'Find travel companions for adventures around Ireland and beyond. Share travel tips, plan group trips, and explore new destinations together.',
        'image': 'event_galway.png',
    },
]


def seed_database():
    """Seed the database with initial data. Only runs if the database is empty."""
    # Ensure tables exist (e.g. init-db may have run against SQLite when Postgres wasn't ready yet)
    try:
        if db.session.scalars(select(Interest).limit(1)).first() is not None:
            return
    except ProgrammingError as e:
        msg = str(e).lower()
        if "does not exist" in msg or "undefinedtable" in msg:
            db.session.rollback()
            from app import models  # noqa: F401 - ensure all models registered
            db.create_all()
        else:
            raise

    # Add predefined interests
    for interest_name in PREDEFINED_INTERESTS:
        interest = Interest(name=interest_name, is_predefined=True)
        db.session.add(interest)

    db.session.commit()

    # Add sample events (without organizer - they're system events)
    for event_data in SAMPLE_EVENTS:
        event = Event(**event_data)
        db.session.add(event)

    db.session.commit()

    # Add sample communities
    for community_data in SAMPLE_COMMUNITIES:
        community = Community(**community_data)
        db.session.add(community)

    db.session.commit()
    print("Database seeded successfully!")
