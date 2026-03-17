"""
CrossPaths MVP (locale-prefixed) routes and in-memory seed data.

This module intentionally avoids auth/DB requirements so the culturally adaptive
pages work out-of-the-box.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from typing import Dict, List, Optional

from flask import Blueprint, abort, render_template, request, url_for
from flask_babel import gettext as _


SUPPORTED_LOCALES = ("en_IE", "uk_UA", "pt_BR")


def _next_saturday(today: Optional[date] = None) -> date:
    today = today or date.today()
    days_ahead = (5 - today.weekday()) % 7  # Mon=0 ... Sat=5
    if days_ahead == 0:
        days_ahead = 7
    return today + timedelta(days=days_ahead)


@dataclass(frozen=True)
class MVPEvent:
    id: int
    title: Dict[str, str]
    description: Dict[str, str]
    day: date
    start_time: time
    location: str
    host_name: str
    host_verified: bool
    attendee_count: int
    agenda: List[str]
    image_url: str
    pt_attendees_first_names: List[str]

    def datetime_start(self) -> datetime:
        return datetime.combine(self.day, self.start_time)


def get_mvp_events() -> List[MVPEvent]:
    sat = _next_saturday()
    wed = sat + timedelta(days=4)
    fri = sat + timedelta(days=6)
    sun = sat + timedelta(days=8)

    return [
        MVPEvent(
            id=1,
            title={
                "en_IE": "Dublin Coffee & Chat",
                "uk_UA": "Дублінська кава та спілкування",
                "pt_BR": "Café e Conversa em Dublin",
            },
            description={
                "en_IE": "A relaxed morning coffee to meet other newcomers and swap Dublin tips.",
                "uk_UA": "Невимушена ранкова зустріч за кавою для знайомства з іншими новоприбулими та обміну корисними порадами про Дублін.",
                "pt_BR": "Um café de manhã bem leve pra conhecer gente nova e trocar dicas de Dublin. ☕️❤️",
            },
            day=sat,
            start_time=time(10, 0),
            location="Bewley’s Café, Grafton Street",
            host_name="Sarah M.",
            host_verified=True,
            attendee_count=12,
            agenda=[
                "Introductions (10 min)",
                "Speed-friending rounds (30 min)",
                "Open chat (20 min)",
            ],
            image_url="https://placehold.co/800x500",
            pt_attendees_first_names=["Ana", "Rafa", "Lu", "Bruno", "Carla"],
        ),
        MVPEvent(
            id=2,
            title={
                "en_IE": "Walk & Talk at Phoenix Park",
                "uk_UA": "Прогулянка та розмова у Фенікс-парку",
                "pt_BR": "Caminhada e Papo no Phoenix Park 🌿",
            },
            description={
                "en_IE": "Easy stroll, small groups, and a quick coffee stop after.",
                "uk_UA": "Неспішна прогулянка, спілкування в малих групах та коротка перерва на каву після.",
                "pt_BR": "Caminhada tranquila, vibe de grupo e depois um cafezinho. 🙌☕️",
            },
            day=wed,
            start_time=time(18, 30),
            location="Phoenix Park (main gate meeting point)",
            host_name="Oleh K.",
            host_verified=True,
            attendee_count=18,
            agenda=[
                "Meet & greet (10 min)",
                "Guided group walk (40 min)",
                "Wrap-up + optional coffee (20 min)",
            ],
            image_url="https://placehold.co/800x500",
            pt_attendees_first_names=["Bia", "João", "Mari", "Felipe", "Nina"],
        ),
        MVPEvent(
            id=3,
            title={
                "en_IE": "After-Work Speed-Friending (City Centre)",
                "uk_UA": "Швидкі знайомства після роботи (центр міста)",
                "pt_BR": "Speed-Friending Pós-Trabalho 🎉",
            },
            description={
                "en_IE": "Short rounds, friendly prompts, and plenty of chances to connect.",
                "uk_UA": "Короткі раунди знайомства, зрозумілі запитання-підказки та багато можливостей для спілкування.",
                "pt_BR": "Rodadas rápidas, perguntas legais e energia de grupo! 😄✨",
            },
            day=fri,
            start_time=time(19, 0),
            location="Public lounge space, Dublin 2",
            host_name="Marina S.",
            host_verified=False,
            attendee_count=26,
            agenda=[
                "Welcome + house rules (5 min)",
                "Speed-friending rounds (45 min)",
                "Open mingle (30 min)",
            ],
            image_url="https://placehold.co/800x500",
            pt_attendees_first_names=["Paula", "Gui", "Léo", "Camila", "Dani"],
        ),
        MVPEvent(
            id=4,
            title={
                "en_IE": "Board Games & New Friends",
                "uk_UA": "Настільні ігри та нові друзі",
                "pt_BR": "Noite de Jogos + Novas Amizades 🎲",
            },
            description={
                "en_IE": "Pick a table, learn a game in minutes, and meet people naturally.",
                "uk_UA": "Оберіть столик, швидко вивчіть правила гри та знайомтеся природно й комфортно.",
                "pt_BR": "Escolhe uma mesa, aprende rapidinho e faz amizade jogando. 🎲❤️",
            },
            day=sun,
            start_time=time(17, 30),
            location="Board game café, Dublin 7",
            host_name="Kateryna P.",
            host_verified=True,
            attendee_count=20,
            agenda=[
                "Arrivals + table matching (15 min)",
                "Games (60 min)",
                "Group wrap-up (15 min)",
            ],
            image_url="https://placehold.co/800x500",
            pt_attendees_first_names=["Isa", "Pedro", "Clara", "Vini", "Sofia"],
        ),
        MVPEvent(
            id=5,
            title={
                "en_IE": "Museum Meetup: Art, Culture, Chat",
                "uk_UA": "Зустріч у музеї: мистецтво, культура, спілкування",
                "pt_BR": "Encontro no Museu: Arte & Bate-Papo 🖼️",
            },
            description={
                "en_IE": "A calm, easy way to meet people with conversation starters built in.",
                "uk_UA": "Спокійний та комфортний формат знайомства з готовими темами для розмови.",
                "pt_BR": "Um rolê calminho com assunto pronto (arte!) e gente legal. 🖼️✨",
            },
            day=sat + timedelta(days=14),
            start_time=time(14, 0),
            location="National Gallery of Ireland, Merrion Square",
            host_name="João R.",
            host_verified=False,
            attendee_count=14,
            agenda=[
                "Meet at entrance (10 min)",
                "Small-group gallery loop (45 min)",
                "Coffee / chat nearby (30 min)",
            ],
            image_url="https://placehold.co/800x500",
            pt_attendees_first_names=["Renata", "Caio", "Alice", "Heitor", "Gabi"],
        ),
    ]


def _require_locale(locale: str) -> str:
    if locale not in SUPPORTED_LOCALES:
        abort(404)
    return locale


def _event_by_id(event_id: int) -> MVPEvent:
    for e in get_mvp_events():
        if e.id == event_id:
            return e
    abort(404)


def _switch_locale_url(target_locale: str) -> str:
    """
    Build a URL for the current endpoint using a different locale.

    Works for endpoints inside this blueprint. Falls back to home for unknown endpoints.
    """
    if target_locale not in SUPPORTED_LOCALES:
        target_locale = "en_IE"

    if request.endpoint != "crosspaths.home" and (not request.endpoint or not request.endpoint.startswith("crosspaths.")):
        return url_for("crosspaths.home", locale=target_locale)

    view_args = dict(request.view_args or {})
    view_args["locale"] = target_locale
    query_args = dict(request.args or {})
    # Prevent url_for(**view_args, **query_args) collisions (e.g. ?locale=..., ?event_id=...).
    for k in list(query_args.keys()):
        if k in view_args:
            query_args.pop(k, None)
    return url_for(request.endpoint, **view_args, **query_args)


bp = Blueprint("crosspaths", __name__)


@bp.app_context_processor
def inject_crosspaths_helpers():
    return {
        "SUPPORTED_LOCALES": SUPPORTED_LOCALES,
        "switch_locale_url": _switch_locale_url,
    }


@bp.route("/<locale>/")
def home(locale: str):
    locale = _require_locale(locale)
    return render_template("home.html", locale=locale)


@bp.route("/<locale>/events")
def events(locale: str):
    locale = _require_locale(locale)
    events = get_mvp_events()
    return render_template("events.html", locale=locale, events=events)


@bp.route("/<locale>/events/<int:event_id>")
def event_detail(locale: str, event_id: int):
    locale = _require_locale(locale)
    event = _event_by_id(event_id)
    return render_template("event_detail.html", locale=locale, event=event)


@bp.route("/<locale>/about")
def about(locale: str):
    locale = _require_locale(locale)
    return render_template("about.html", locale=locale)

