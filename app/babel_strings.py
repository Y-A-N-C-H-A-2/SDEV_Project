"""
Strings that appear only in dynamic profile fields and database-seeded
content (event titles/descriptions, community names/descriptions, etc.);
listed here so Babel can extract them (see `pybabel extract … -k _l`).

The seed pipeline stores the English text in the database, and templates
render it via `_(community.name)` etc. Without these `_l(...)` references,
`pybabel extract` would not see the strings as translatable, and the
matching entries in the .po catalogs would be marked obsolete (`#~`),
which excludes them from the compiled .mo file — meaning the rendered
page would always show English regardless of the active locale.
"""
from flask_babel import lazy_gettext as _l

PROFILE_VALUES_FOR_EXTRACTION = (
    _l('Ukrainian'),
)

# --- Seed: predefined interests (see app/seed.py PREDEFINED_INTERESTS) ---
SEED_INTERESTS_FOR_EXTRACTION = (
    _l('Language exchange'),
    _l('Travel'),
    _l('Hiking'),
    _l('Photography'),
    _l('Music'),
    _l('Art'),
    _l('Tech'),
    _l('Sports'),
    _l('Food and coffee'),
    _l('Nightlife'),
    _l('Cultural events'),
)

# --- Seed: event titles and descriptions (see app/seed.py SAMPLE_EVENTS) ---
SEED_EVENTS_FOR_EXTRACTION = (
    _l('Trip to Galway with a Castle Visit'),
    _l('Join us for an amazing day trip to Galway! We will visit the historic Dunguaire Castle, explore the colorful streets of Galway city, and enjoy traditional Irish music in a local pub.'),
    _l('Wicklow Mountains Hiking Trip'),
    _l('Experience the breathtaking beauty of the Wicklow Mountains. This moderate-level hike takes us through Glendalough valley with stunning views of the upper and lower lakes.'),
    _l('Wednesday Filming Locations Tour in Wicklow'),
    _l('Explore the magical filming locations of the Wednesday series in County Wicklow. Visit the stunning landscapes that served as the backdrop for Nevermore Academy.'),
    _l('International Meetup in Dublin'),
    _l('Meet people from all over the world living in Dublin! This casual meetup is perfect for newcomers and anyone looking to expand their social circle in the city.'),
    _l('Language Exchange Night'),
    _l('Practice languages while making new friends! Bring your enthusiasm for learning and share your native language. All levels welcome.'),
    _l('Photography Walk'),
    _l("Join fellow photography enthusiasts for a guided walk through Dublin's most photogenic spots. Bring any camera — phone cameras are welcome too!"),
    _l('Coffee Meetup for Newcomers in Ireland'),
    _l('New to Ireland? Come for a relaxed coffee meetup and meet other newcomers. Share tips, stories, and make lasting connections over great coffee.'),
    _l('Pub Social Night'),
    _l('Experience the famous Irish pub culture! Join us for a fun night of live music, great craic, and the best Guinness in town.'),
    _l('Art and Creativity Workshop'),
    _l('Unleash your creative side in this hands-on art workshop. No experience needed — just bring your curiosity and willingness to try something new!'),
)

# --- Seed: event categories (used by `_(event.category)` in templates) ---
SEED_EVENT_CATEGORIES_FOR_EXTRACTION = (
    _l('Travel'),
    _l('Outdoor'),
    _l('Cultural'),
    _l('Social'),
    _l('Language'),
    _l('Photography'),
    _l('Food & Drink'),
    _l('Nightlife'),
    _l('Art & Creative'),
)

# --- Seed: community names and descriptions (see app/seed.py SAMPLE_COMMUNITIES) ---
SEED_COMMUNITIES_FOR_EXTRACTION = (
    _l('Language Exchange Community'),
    _l('Connect with language learners and native speakers. Practice your target language in a friendly, supportive environment through regular meetups and events.'),
    _l('Hiking Ireland'),
    _l("Explore Ireland's stunning trails and mountains together. From gentle coastal walks to challenging mountain hikes, there's something for everyone."),
    _l('International Friends in Dublin'),
    _l('A welcoming community for internationals living in Dublin. Meet people from around the world, share experiences, and build lasting friendships.'),
    _l('Photography Club'),
    _l("For photographers of all levels! Share your work, learn new techniques, and join photo walks around Ireland's most beautiful locations."),
    _l('Tech and Startups Ireland'),
    _l('Connect with tech professionals, startup founders, and anyone interested in the Irish tech scene. Networking events, talks, and hackathons.'),
    _l('Art and Creativity'),
    _l('A space for artists, creatives, and art enthusiasts. From painting workshops to gallery visits, let creativity bring us together.'),
    _l('Travel Buddies'),
    _l('Find travel companions for adventures around Ireland and beyond. Share travel tips, plan group trips, and explore new destinations together.'),
)
