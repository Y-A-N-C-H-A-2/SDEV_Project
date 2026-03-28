"""
Strings that appear only in dynamic profile fields; listed here so Babel can
extract them (see `pybabel extract … -k _l`).
"""
from flask_babel import lazy_gettext as _l

PROFILE_VALUES_FOR_EXTRACTION = (
    _l('Ukrainian'),
)
