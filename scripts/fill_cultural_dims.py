"""Fill translations for the cultural-dimensions improvements.

Run from repo root: ``python scripts/fill_cultural_dims.py``.
Updates only msgids whose msgstr is currently empty; keeps existing translations.
"""
from pathlib import Path

from babel.messages import pofile

BASE = Path(__file__).resolve().parent.parent / "translations"


UK_UA = {
    # forms.py — locale picker
    "Use browser language": "Використовувати мову браузера",
    # forms.py — validators
    "Please enter your name.": "Будь ласка, введіть ваше ім’я.",
    "Please enter your email.": "Будь ласка, введіть вашу електронну пошту.",
    "Please enter a valid email address.": "Будь ласка, введіть дійсну електронну адресу.",
    "Please enter a password.": "Будь ласка, введіть пароль.",
    "Password must be at least 6 characters.": "Пароль має містити щонайменше 6 символів.",
    "Please confirm your password.": "Будь ласка, підтвердіть ваш пароль.",
    "Please enter your password.": "Будь ласка, введіть ваш пароль.",
    "Age must be between 16 and 120.": "Вік має бути від 16 до 120.",
    "Phone (optional, with country code)": "Телефон (необов’язково, з кодом країни)",
    "Please enter a valid phone number.": "Введіть дійсний номер телефону.",
    "Preferred language": "Бажана мова",
    "Please give your event a title.": "Дайте вашій події назву.",
    "Please choose a city.": "Будь ласка, оберіть місто.",
    "Please choose a date and time.": "Будь ласка, оберіть дату та час.",
    "Agenda (one item per line)": "Програма (по одному пункту в рядку)",
    "A clear schedule helps people decide whether to attend.": (
        "Чітка програма допомагає людям вирішити, чи братимуть вони участь."
    ),
    "Attendee limit (optional)": "Обмеження кількості учасників (необов’язково)",
    "Attendee limit must be a positive number.": "Обмеження має бути додатним числом.",
    "Recurring event (meets regularly)": "Регулярна подія (відбувається регулярно)",
    "Cooperative event (no competition, everyone welcome)": (
        "Кооперативна подія (без змагань, відкрита для всіх)"
    ),
    "Full name": "Повне ім’я",
    # routes.py — flash messages
    "This event has already happened.": "Ця подія вже відбулася.",
    "This event is fully booked.": "На цю подію вже немає вільних місць.",
    "Saved for later. We will keep it in your profile.": (
        "Збережено. Ця подія з’явиться у вашому профілі."
    ),
    "Removed from your saved list.": "Видалено зі збережених.",
    # event_detail.html — new copy
    "Verified host": "Перевірений організатор",
    "limit %(cap)s": "макс. %(cap)s",
    "%(n)s seats left": "Залишилось місць: %(n)s",
    "Recurring event — meets regularly": "Регулярна подія — відбувається регулярно",
    "Cooperative — no competition, everyone welcome": (
        "Кооперативна — без змагань, відкрита для всіх"
    ),
    "Competitive — friendly contest": "Змагальна — дружній конкурс",
    "Who is going": "Хто йде",
    "Who's going": "Хто йде",
    "Agenda": "Програма",
    "Review &amp; Confirm": "Переглянути та підтвердити",
    "Fully booked": "Місць немає",
    "Saved ✓": "Збережено ✓",
    "Save for later": "Зберегти на потім",
    "Bring a friend": "Запросіть друга",
    "Share this event with someone who would enjoy it.": (
        "Поділіться цією подією з тим, кому вона сподобається."
    ),
    "Event link": "Посилання на подію",
    # event_confirm.html
    "Confirm – %(name)s": "Підтвердження – %(name)s",
    "Review and confirm": "Перевірте та підтвердіть",
    "Please review the details below before joining.": (
        "Будь ласка, перевірте дані нижче перед тим, як приєднатися."
    ),
    "When": "Коли",
    "Where": "Де",
    "Host": "Організатор",
    "Attending": "Учасники",
    "Style": "Формат",
    "By confirming, you agree to attend at the time and place above.": (
        "Підтверджуючи, ви погоджуєтесь бути присутніми у вказаний час і в указаному місці."
    ),
    "Yes, confirm my attendance": "Так, підтверджую участь",
    "Go back": "Повернутися",
    # events.html — time chips and empty state
    "Time filter": "Фільтр за часом",
    "All upcoming": "Всі майбутні",
    "Tonight": "Сьогодні ввечері",
    "This weekend": "Цих вихідних",
    "No verified events match your filters.": "Немає перевірених подій, що відповідають фільтрам.",
    "Adjust the filters or come back later — new events are reviewed and added regularly.": (
        "Змініть фільтри або поверніться пізніше — нові події перевіряються та додаються регулярно."
    ),
    "Nothing here yet — let’s change that ✨": "Тут поки що порожньо ✨",
    "Try a different city or come hang out tonight! Or start your own — your friends will follow.": (
        "Оберіть інше місто або проведіть вечір з нами! Або створіть свою подію."
    ),
    # create_event.html
    "19:00 – Welcome\n19:30 – Activity\n21:00 – Wrap up": (
        "19:00 – Вітання\n19:30 – Активність\n21:00 – Завершення"
    ),
    "Leave blank for no limit.": "Залиште порожнім, якщо без обмежень.",
    "e.g. 20": "напр. 20",
    "e.g. +353 87 123 4567": "напр. +353 87 123 4567",
    # profile.html
    "Saved for later": "Збережено на потім",
}


PT_BR = {
    # forms.py
    "Use browser language": "Usar idioma do navegador",
    "Please enter your name.": "Por favor, informe seu nome.",
    "Please enter your email.": "Por favor, informe seu e-mail.",
    "Please enter a valid email address.": "Informe um e-mail válido.",
    "Please enter a password.": "Por favor, informe uma senha.",
    "Password must be at least 6 characters.": "A senha deve ter pelo menos 6 caracteres.",
    "Please confirm your password.": "Confirme sua senha.",
    "Please enter your password.": "Informe sua senha.",
    "Age must be between 16 and 120.": "A idade deve estar entre 16 e 120.",
    "Phone (optional, with country code)": "Telefone (opcional, com código do país)",
    "Please enter a valid phone number.": "Informe um telefone válido.",
    "Preferred language": "Idioma preferido",
    "Please give your event a title.": "Dê um título ao seu evento.",
    "Please choose a city.": "Escolha uma cidade.",
    "Please choose a date and time.": "Escolha uma data e horário.",
    "Agenda (one item per line)": "Programação (um item por linha)",
    "A clear schedule helps people decide whether to attend.": (
        "Uma programação clara ajuda as pessoas a decidirem se vão participar."
    ),
    "Attendee limit (optional)": "Limite de participantes (opcional)",
    "Attendee limit must be a positive number.": "O limite deve ser um número positivo.",
    "Recurring event (meets regularly)": "Evento recorrente (acontece regularmente)",
    "Cooperative event (no competition, everyone welcome)": (
        "Evento cooperativo (sem competição, todos são bem-vindos)"
    ),
    "Full name": "Nome completo",
    # routes
    "This event has already happened.": "Este evento já aconteceu.",
    "This event is fully booked.": "Este evento está lotado.",
    "Saved for later. We will keep it in your profile.": (
        "Salvo para depois! Vai ficar guardado no seu perfil."
    ),
    "Removed from your saved list.": "Removido da sua lista.",
    # event_detail
    "Verified host": "Anfitrião verificado",
    "limit %(cap)s": "limite %(cap)s",
    "%(n)s seats left": "%(n)s vagas restantes",
    "Recurring event — meets regularly": "Evento recorrente — acontece regularmente",
    "Cooperative — no competition, everyone welcome": (
        "Cooperativo — sem competição, todos são bem-vindos"
    ),
    "Competitive — friendly contest": "Competitivo — competição amigável",
    "Who is going": "Quem vai",
    "Who's going": "Quem vai 🎉",
    "Agenda": "Programação",
    "Review &amp; Confirm": "Revisar e confirmar",
    "Fully booked": "Lotado",
    "Saved ✓": "Salvo ✓",
    "Save for later": "Salvar para depois",
    "Bring a friend": "Chame um amigo",
    "Share this event with someone who would enjoy it.": (
        "Compartilhe este evento com quem você acha que vai curtir."
    ),
    "Event link": "Link do evento",
    # event_confirm
    "Confirm – %(name)s": "Confirmar – %(name)s",
    "Review and confirm": "Revisar e confirmar",
    "Please review the details below before joining.": (
        "Confira os detalhes abaixo antes de participar."
    ),
    "When": "Quando",
    "Where": "Onde",
    "Host": "Anfitrião",
    "Attending": "Participantes",
    "Style": "Estilo",
    "By confirming, you agree to attend at the time and place above.": (
        "Ao confirmar, você concorda em participar no horário e local acima."
    ),
    "Yes, confirm my attendance": "Sim, confirmar minha participação",
    "Go back": "Voltar",
    # events.html
    "Time filter": "Filtro por horário",
    "All upcoming": "Todos os próximos",
    "Tonight": "Hoje à noite",
    "This weekend": "Neste fim de semana",
    "No verified events match your filters.": "Nenhum evento verificado para os filtros escolhidos.",
    "Adjust the filters or come back later — new events are reviewed and added regularly.": (
        "Ajuste os filtros ou volte depois — novos eventos chegam o tempo todo."
    ),
    "Nothing here yet — let’s change that ✨": "Nada por aqui ainda — vamos mudar isso ✨",
    "Try a different city or come hang out tonight! Or start your own — your friends will follow.": (
        "Tenta outra cidade ou vem curtir hoje à noite! Ou crie o seu próprio — a galera vai junto."
    ),
    # create_event
    "19:00 – Welcome\n19:30 – Activity\n21:00 – Wrap up": (
        "19:00 – Boas-vindas\n19:30 – Atividade\n21:00 – Encerramento"
    ),
    "Leave blank for no limit.": "Deixe em branco para não limitar.",
    "e.g. 20": "ex.: 20",
    "e.g. +353 87 123 4567": "ex.: +353 87 123 4567",
    # profile.html
    "Saved for later": "Salvos para depois",
}


def apply(locale: str, mapping: dict) -> int:
    po_path = BASE / locale / "LC_MESSAGES" / "messages.po"
    with po_path.open("rb") as fh:
        catalog = pofile.read_po(fh)
    filled = 0
    for msgid, msgstr in mapping.items():
        message = catalog.get(msgid)
        if message is not None and not message.string:
            message.string = msgstr
            filled += 1
    with po_path.open("wb") as fh:
        pofile.write_po(fh, catalog)
    return filled


if __name__ == "__main__":
    print("uk_UA filled:", apply("uk_UA", UK_UA))
    print("pt_BR filled:", apply("pt_BR", PT_BR))
