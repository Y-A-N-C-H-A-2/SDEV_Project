"""
CrossPaths shared utilities
"""
from urllib.parse import urlparse

from app import db
from app.models import Interest


def normalize_custom_interests(raw_text):
    """Parse, strip, and capitalise a comma-separated list of custom interests.

    Returns a deduplicated list of normalised interest names.
    """
    if not raw_text:
        return []
    seen = set()
    result = []
    for item in raw_text.split(','):
        name = item.strip().capitalize()
        if name and name.lower() not in seen:
            seen.add(name.lower())
            result.append(name)
    return result


def sync_user_interests(user, predefined_names, custom_text):
    """Set a user's interests from predefined names and custom comma-separated text.

    Clears existing interests, then adds predefined (by name) and custom (creating
    Interest rows as needed). Does not commit; caller must commit the session.
    """
    user.interests.clear()

    if predefined_names:
        for interest_name in predefined_names:
            interest = Interest.query.filter_by(name=interest_name).first()
            if interest:
                user.interests.append(interest)

    for interest_name in normalize_custom_interests(custom_text or ''):
        interest = Interest.query.filter(
            db.func.lower(Interest.name) == interest_name.lower()
        ).first()
        if not interest:
            interest = Interest(name=interest_name, is_predefined=False)
            db.session.add(interest)
            db.session.flush()
        user.interests.append(interest)


def is_same_origin_referrer(request, referrer):
    """Return True if referrer is from the same host as the current request."""
    if not referrer or not referrer.strip():
        return False
    parsed = urlparse(referrer)
    if not parsed.netloc:
        return parsed.scheme == ''  # relative URL
    return parsed.netloc == request.host
