"""
CrossPaths Database Seed Data
"""
from datetime import datetime, timedelta
from app import db
from app.models import Interest, Event, Community, User, community_events

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
        'photo': 'placeholder_galway.jpg',
    },
    {
        'title': 'Wicklow Mountains Hiking Trip',
        'description': 'Experience the breathtaking beauty of the Wicklow Mountains. This moderate-level hike takes us through Glendalough valley with stunning views of the upper and lower lakes.',
        'date_time': datetime.utcnow() + timedelta(days=7),
        'city': 'Dublin',
        'venue': 'Glendalough, Co. Wicklow',
        'category': 'Outdoor',
        'photo': 'placeholder_wicklow.jpg',
    },
    {
        'title': 'Wednesday Filming Locations Tour in Wicklow',
        'description': 'Explore the magical filming locations of the Wednesday series in County Wicklow. Visit the stunning landscapes that served as the backdrop for Nevermore Academy.',
        'date_time': datetime.utcnow() + timedelta(days=21),
        'city': 'Dublin',
        'venue': 'Killruddery House, Bray, Co. Wicklow',
        'category': 'Cultural',
        'photo': 'placeholder_wednesday.jpg',
    },
    {
        'title': 'International Meetup in Dublin',
        'description': 'Meet people from all over the world living in Dublin! This casual meetup is perfect for newcomers and anyone looking to expand their social circle in the city.',
        'date_time': datetime.utcnow() + timedelta(days=3),
        'city': 'Dublin',
        'venue': 'The Bernard Shaw, Dublin 8',
        'category': 'Social',
        'photo': 'placeholder_meetup.jpg',
    },
    {
        'title': 'Language Exchange Night',
        'description': 'Practice languages while making new friends! Bring your enthusiasm for learning and share your native language. All levels welcome.',
        'date_time': datetime.utcnow() + timedelta(days=5),
        'city': 'Dublin',
        'venue': 'Cafe en Seine, Dawson Street',
        'category': 'Language',
        'photo': 'placeholder_language.jpg',
    },
    {
        'title': 'Photography Walk',
        'description': "Join fellow photography enthusiasts for a guided walk through Dublin's most photogenic spots. Bring any camera — phone cameras are welcome too!",
        'date_time': datetime.utcnow() + timedelta(days=10),
        'city': 'Dublin',
        'venue': "Meeting at Ha'penny Bridge, Dublin",
        'category': 'Photography',
        'photo': 'placeholder_photo.jpg',
    },
    {
        'title': 'Coffee Meetup for Newcomers in Ireland',
        'description': 'New to Ireland? Come for a relaxed coffee meetup and meet other newcomers. Share tips, stories, and make lasting connections over great coffee.',
        'date_time': datetime.utcnow() + timedelta(days=2),
        'city': 'Cork',
        'venue': "Filter Coffee, George's Quay, Cork",
        'category': 'Food & Drink',
        'photo': 'placeholder_coffee.jpg',
    },
    {
        'title': 'Pub Social Night',
        'description': 'Experience the famous Irish pub culture! Join us for a fun night of live music, great craic, and the best Guinness in town.',
        'date_time': datetime.utcnow() + timedelta(days=4),
        'city': 'Limerick',
        'venue': "Dolan's Pub, Limerick",
        'category': 'Nightlife',
        'photo': 'placeholder_pub.jpg',
    },
    {
        'title': 'Art and Creativity Workshop',
        'description': 'Unleash your creative side in this hands-on art workshop. No experience needed — just bring your curiosity and willingness to try something new!',
        'date_time': datetime.utcnow() + timedelta(days=12),
        'city': 'Waterford',
        'venue': 'Garter Lane Arts Centre, Waterford',
        'category': 'Art & Creative',
        'photo': 'placeholder_art.jpg',
    },
]

SAMPLE_COMMUNITIES = [
    {
        'name': 'Language Exchange Community',
        'description': 'Connect with language learners and native speakers. Practice your target language in a friendly, supportive environment through regular meetups and events.',
        'image': 'placeholder_community_language.jpg',
    },
    {
        'name': 'Hiking Ireland',
        'description': "Explore Ireland's stunning trails and mountains together. From gentle coastal walks to challenging mountain hikes, there's something for everyone.",
        'image': 'placeholder_community_hiking.jpg',
    },
    {
        'name': 'International Friends in Dublin',
        'description': 'A welcoming community for internationals living in Dublin. Meet people from around the world, share experiences, and build lasting friendships.',
        'image': 'placeholder_community_international.jpg',
    },
    {
        'name': 'Photography Club',
        'description': "For photographers of all levels! Share your work, learn new techniques, and join photo walks around Ireland's most beautiful locations.",
        'image': 'placeholder_community_photography.jpg',
    },
    {
        'name': 'Tech and Startups Ireland',
        'description': 'Connect with tech professionals, startup founders, and anyone interested in the Irish tech scene. Networking events, talks, and hackathons.',
        'image': 'placeholder_community_tech.jpg',
    },
    {
        'name': 'Art and Creativity',
        'description': 'A space for artists, creatives, and art enthusiasts. From painting workshops to gallery visits, let creativity bring us together.',
        'image': 'placeholder_community_art.jpg',
    },
    {
        'name': 'Travel Buddies',
        'description': 'Find travel companions for adventures around Ireland and beyond. Share travel tips, plan group trips, and explore new destinations together.',
        'image': 'placeholder_community_travel.jpg',
    },
]


def seed_database():
    """Seed the database with initial data."""
    # Add predefined interests
    for interest_name in PREDEFINED_INTERESTS:
        existing = Interest.query.filter_by(name=interest_name).first()
        if not existing:
            interest = Interest(name=interest_name, is_predefined=True)
            db.session.add(interest)

    db.session.commit()

    # Add sample events (without organizer - they're system events)
    for event_data in SAMPLE_EVENTS:
        existing = Event.query.filter_by(title=event_data['title']).first()
        if not existing:
            event = Event(**event_data)
            db.session.add(event)

    db.session.commit()

    # Add sample communities
    for community_data in SAMPLE_COMMUNITIES:
        existing = Community.query.filter_by(name=community_data['name']).first()
        if not existing:
            community = Community(**community_data)
            db.session.add(community)

    db.session.commit()
    print("Database seeded successfully!")
