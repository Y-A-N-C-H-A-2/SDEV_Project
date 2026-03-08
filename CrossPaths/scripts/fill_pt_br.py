"""Fill all pt_BR translations."""
from pathlib import Path
from babel.messages import pofile

BASE = Path(__file__).resolve().parent.parent / "translations"

PT_BR = {
    # ---- Flash messages / routes.py ----
    "Uploaded file is not a valid image.": "O arquivo enviado não é uma imagem válida.",
    "Event created successfully!": "Evento criado com sucesso!",
    "An error occurred while creating the event. Please try again.": "Ocorreu um erro ao criar o evento. Tente novamente.",
    "You joined %(name)s!": "Você entrou em %(name)s!",
    "An error occurred. Please try again.": "Ocorreu um erro. Tente novamente.",
    "You are already a member of this community.": "Você já é membro desta comunidade.",
    "You left %(name)s.": "Você saiu de %(name)s.",
    "Email already registered. Please log in.": "E-mail já cadastrado. Por favor, faça login.",
    "Account created successfully! Please log in.": "Conta criada com sucesso! Por favor, faça login.",
    "An error occurred during registration. Please try again.": "Ocorreu um erro durante o cadastro. Tente novamente.",
    "Welcome back!": "Bem-vindo(a) de volta!",
    "Invalid email or password.": "E-mail ou senha inválidos.",
    "You have been logged out.": "Você saiu da sua conta.",
    "Profile updated successfully!": "Perfil atualizado com sucesso!",
    "An error occurred while updating your profile. Please try again.": "Ocorreu um erro ao atualizar seu perfil. Tente novamente.",

    # ---- about.html ----
    "About – CrossPaths": "Sobre – CrossPaths",
    "About CrossPaths": "Sobre o CrossPaths",
    "Where cultures meet and friendships begin": "Onde culturas se encontram e amizades começam",
    "Get in Touch": "Entre em Contato",
    "Questions or feedback? We'd love to hear from you!": "Dúvidas ou sugestões? Adoraríamos ouvir você!",
    "Email:": "E-mail:",
    "Based in:": "Localizado em:",

    # ---- base.html ----
    "CrossPaths – Where cultures meet and friendships begin": "CrossPaths – Onde culturas se encontram e amizades começam",
    "CrossPaths logo": "Logo do CrossPaths",
    "CrossPaths": "CrossPaths",
    "Toggle navigation": "Alternar navegação",
    "Home": "Início",
    "Events": "Eventos",
    "Communities": "Comunidades",
    "Create Event": "Criar Evento",
    "Profile": "Perfil",
    "Logout": "Sair",
    "Login": "Entrar",
    "Register": "Cadastrar",
    "English (Ireland)": "Inglês (Irlanda)",
    "Ukrainian": "Ucraniano",
    "Portuguese (Brazil)": "Português (Brasil)",
    "Where cultures meet and friendships begin.": "Onde culturas se encontram e amizades começam.",
    "A culturally adaptive platform for international newcomers in Dublin": "Uma plataforma culturalmente adaptável para recém-chegados internacionais em Dublin",

    # ---- communities.html ----
    "Communities – CrossPaths": "Comunidades – CrossPaths",
    "Browse and join interest-based communities": "Explore e participe de comunidades baseadas em interesses",
    "members": "membros",
    "No communities yet": "Nenhuma comunidade ainda",
    "Communities are coming soon!": "Comunidades em breve!",
    "Previous": "Anterior",
    "Next": "Próximo",

    # ---- community_detail.html ----
    "%(name)s – CrossPaths": "%(name)s – CrossPaths",
    "About this community": "Sobre esta comunidade",
    "Leave Community": "Sair da Comunidade",
    "Join Community": "Entrar na Comunidade",
    "Login to Join": "Faça Login para Participar",
    "← Back to Communities": "← Voltar para Comunidades",
    "Members": "Membros",

    # ---- create_event.html ----
    "Upcoming Events": "Próximos Eventos",
    "Create Event – CrossPaths": "Criar Evento – CrossPaths",
    "Organize an event for the community": "Organize um evento para a comunidade",
    "Event title": "Título do evento",
    "Describe your event...": "Descreva seu evento...",
    "Venue name and address": "Nome e endereço do local",
    "Accepted formats: JPG, PNG, GIF. Max 16MB.": "Formatos aceitos: JPG, PNG, GIF. Máximo 16MB.",

    # ---- edit_profile.html ----
    "Edit Profile – CrossPaths": "Editar Perfil – CrossPaths",
    "Edit Profile": "Editar Perfil",
    "Interests": "Interesses",
    "e.g. Yoga, Cooking, Board games": "ex.: Yoga, Culinária, Jogos de tabuleiro",
    "Save Changes": "Salvar Alterações",
    "Cancel": "Cancelar",

    # ---- event_detail.html ----
    "Organized by": "Organizado por",
    "people attending": "pessoas participando",
    "About this event": "Sobre este evento",
    "← Back to Events": "← Voltar para Eventos",

    # ---- events.html ----
    "Events – CrossPaths": "Eventos – CrossPaths",
    "Find events happening across Ireland": "Encontre eventos acontecendo pela Irlanda",
    "Search events...": "Buscar eventos...",
    "All Cities": "Todas as Cidades",
    "Dublin": "Dublin",
    "Galway": "Galway",
    "Cork": "Cork",
    "Limerick": "Limerick",
    "Waterford": "Waterford",
    "Search": "Buscar",
    "Clear": "Limpar",
    "attending": "participando",
    "No events found": "Nenhum evento encontrado",
    "Try adjusting your search or filter, or check back soon for new events!": "Tente ajustar sua busca ou filtro, ou volte em breve para novos eventos!",
    "Create an Event": "Criar um Evento",

    # ---- index.html ----
    "CrossPaths – Home": "CrossPaths – Início",
    "Meet People. Attend Events. Explore Ireland.": "Conheça Pessoas. Participe de Eventos. Explore a Irlanda.",
    "A community platform for locals, expats, and travelers to connect through events across Ireland": "Uma plataforma comunitária para habitantes locais, expatriados e viajantes se conectarem através de eventos pela Irlanda",
    "Browse Events": "Explorar Eventos",
    "Join Now": "Participe Agora",
    "View All →": "Ver Todos →",
    "Featured Communities": "Comunidades em Destaque",
    "Discover Ireland Experiences": "Descubra Experiências na Irlanda",
    "Outdoor Adventures": "Aventuras ao Ar Livre",
    "Explore mountains, coastlines, and stunning landscapes across Ireland": "Explore montanhas, costas e paisagens deslumbrantes pela Irlanda",
    "City Life": "Vida na Cidade",
    "Discover vibrant cities from Dublin to Galway, Cork to Limerick": "Descubra cidades vibrantes de Dublin a Galway, Cork a Limerick",
    "Culture & Social": "Cultura e Social",
    "Experience traditional music, arts, festivals and Irish hospitality": "Viva a música tradicional, artes, festivais e hospitalidade irlandesa",
    "Ready to Meet New Friends?": "Pronto para Conhecer Novos Amigos?",
    "Join thousands of people connecting through events across Ireland": "Junte-se a milhares de pessoas se conectando através de eventos pela Irlanda",
    "View Upcoming Events": "Ver Próximos Eventos",

    # ---- login.html ----
    "Login – CrossPaths": "Entrar – CrossPaths",
    "Welcome Back": "Bem-vindo(a) de volta",
    "Log in to your CrossPaths account": "Faça login na sua conta CrossPaths",
    "your@email.com": "seu@email.com",
    "Your password": "Sua senha",
    "Log In": "Entrar",
    "Don't have an account?": "Não tem uma conta?",

    # ---- profile.html ----
    "Profile – CrossPaths": "Perfil – CrossPaths",
    "Your Profile": "Seu Perfil",
    "%(city)s, Ireland": "%(city)s, Irlanda",
    "Age": "Idade",
    "Gender": "Gênero",
    "Nationality": "Nacionalidade",
    "City": "Cidade",
    "Your Communities": "Suas Comunidades",
    "Events Attended": "Eventos Participados",
    "No events yet. Browse upcoming events to get started!": "Nenhum evento ainda. Explore os próximos eventos para começar!",

    # ---- register.html ----
    "Register – CrossPaths": "Cadastro – CrossPaths",
    "Create Account": "Criar Conta",
    "Join CrossPaths and start meeting people in Ireland": "Junte-se ao CrossPaths e comece a conhecer pessoas na Irlanda",
    "Your full name": "Seu nome completo",
    "Min 6 characters": "Mínimo 6 caracteres",
    "Confirm password": "Confirmar senha",
    "Your nationality": "Sua nacionalidade",
    "Already have an account?": "Já tem uma conta?",
    "Log in": "Entrar",

    # ---- partials/about/content_pt_BR.html ----
    "What is CrossPaths?": "O que é o CrossPaths?",
    "CrossPaths is a platform for international newcomers in Dublin to meet new people through speed-friending events.": "CrossPaths é uma plataforma para recém-chegados internacionais em Dublin conhecerem novas pessoas através de eventos de amizade rápida.",
    "How It Works": "Como Funciona",
    "Browse upcoming events": "Explore os próximos eventos",
    "RSVP to events that interest you": "Confirme presença nos eventos que te interessam",
    "Attend and meet new people": "Participe e conheça novas pessoas",
    "Build your social network": "Construa sua rede social",
    "Who Can Join?": "Quem Pode Participar?",
    "CrossPaths is open to anyone living in Dublin who wants to expand their social circle. Our events are particularly popular with international students, professionals, and migrants.": "O CrossPaths está aberto a qualquer pessoa em Dublin que queira expandir seu círculo social. Nossos eventos são especialmente populares entre estudantes internacionais, profissionais e migrantes.",
    "Get Started": "Começar",
    "Ready to meet new friends? Browse our upcoming events or create your profile to get started.": "Pronto para conhecer novos amigos? Explore nossos próximos eventos ou crie seu perfil para começar.",
    "View Events": "Ver Eventos",
    "Create Profile": "Criar Perfil",

    # ---- partials/about/content_uk_UA.html ----
    "Our Mission": "Nossa Missão",
    "CrossPaths is a verified platform designed to support the social integration of international newcomers in Dublin through structured, safe speed-friending events.": "CrossPaths é uma plataforma verificada projetada para apoiar a integração social de recém-chegados internacionais em Dublin através de eventos estruturados e seguros de amizade rápida.",
    "Safety & Verification": "Segurança e Verificação",
    "All event hosts are verified by our team. Events take place in public venues with clear agendas and structured activities. Your safety is our priority.": "Todos os anfitriões de eventos são verificados pela nossa equipe. Os eventos acontecem em locais públicos com agendas claras e atividades estruturadas. Sua segurança é nossa prioridade.",
    "Verified Hosts": "Anfitriões Verificados",
    "All hosts undergo background verification": "Todos os anfitriões passam por verificação de antecedentes",
    "Public Venues": "Locais Públicos",
    "Events are held in established public locations": "Os eventos são realizados em locais públicos estabelecidos",
    "Clear Agendas": "Agendas Claras",
    "Know exactly what to expect before attending": "Saiba exatamente o que esperar antes de participar",
    "How We Protect Your Privacy": "Como Protegemos Sua Privacidade",
    "Your personal information is never shared publicly. Profile details are only visible to confirmed event attendees. We comply with GDPR regulations.": "Suas informações pessoais nunca são compartilhadas publicamente. Os detalhes do perfil são visíveis apenas para participantes confirmados do evento. Cumprimos as regulamentações do GDPR.",
    "Community Guidelines": "Diretrizes da Comunidade",
    "We maintain a respectful, inclusive community. All members must follow our code of conduct. Harassment or inappropriate behaviour results in immediate account suspension.": "Mantemos uma comunidade respeitosa e inclusiva. Todos os membros devem seguir nosso código de conduta. Assédio ou comportamento inadequado resulta em suspensão imediata da conta.",

    # ---- partials/events/card_en_IE.html ----
    "When:": "Quando:",
    "Where:": "Onde:",
    "Host:": "Anfitrião:",
    "Attendees:": "Participantes:",
    "View Details": "Ver Detalhes",
    "RSVP": "Confirmar Presença",

    # ---- partials/events/card_pt_BR.html ----
    "people going": "pessoas confirmadas",
    "Hosted by": "Organizado por",
    "Join us for a fun evening! Chat, laugh, and make new friends!": "Junte-se a nós para uma noite divertida! Converse, ria e faça novos amigos!",
    "I'm Going!": "Eu Vou!",
    "See Who's Attending": "Veja Quem Vai",

    # ---- partials/events/card_uk_UA.html ----
    "Verified Host": "Anfitrião Verificado",
    "Date:": "Data:",
    "Time:": "Hora:",
    "Location:": "Local:",
    "Capacity:": "Capacidade:",
    "registered": "registrados",
    "View Full Details & Agenda": "Ver Detalhes Completos e Agenda",
    "View Safety Information": "Ver Informações de Segurança",

    # ---- partials/events/header_en_IE.html ----
    "Speed-friending events in Dublin": "Eventos de amizade rápida em Dublin",

    # ---- partials/events/header_pt_BR.html ----
    "Find your next adventure and see who's going!": "Encontre sua próxima aventura e veja quem vai!",

    # ---- partials/events/header_uk_UA.html ----
    "All events are verified and hosted in safe public locations": "Todos os eventos são verificados e realizados em locais públicos seguros",

    # ---- partials/index/features_en_IE.html ----
    "Find speed-friending events near you.": "Encontre eventos de amizade rápida perto de você.",
    "Register for events that interest you.": "Cadastre-se em eventos que te interessam.",
    "Attend": "Participe",
    "Meet new people in structured settings.": "Conheça novas pessoas em ambientes organizados.",
    "Connect": "Conecte",
    "Build your social network in Dublin.": "Construa sua rede social em Dublin.",

    # ---- partials/index/features_pt_BR.html ----
    "Discover Fun Events": "Descubra Eventos Divertidos",
    "Browse exciting meetups and see who else is going!": "Explore encontros empolgantes e veja quem mais vai!",
    "Chat Before You Meet": "Converse Antes de Conhecer",
    "Join event group chats and break the ice online first.": "Participe de chats em grupo do evento e quebre o gelo online primeiro.",
    "Make Real Connections": "Faça Conexões Reais",
    "Meet face-to-face in fun, relaxed settings around Dublin.": "Encontre-se pessoalmente em ambientes divertidos e descontraídos em Dublin.",
    "Find Your Tribe": "Encontre Sua Turma",
    "Build your social circle and never feel alone in a new city!": "Construa seu círculo social e nunca se sinta sozinho em uma cidade nova!",

    # ---- partials/index/features_uk_UA.html ----
    "Browse Verified Events": "Explore Eventos Verificados",
    "Review detailed event information including agenda, host credentials, and safety details.": "Revise informações detalhadas dos eventos, incluindo agenda, credenciais do anfitrião e detalhes de segurança.",
    "Register Securely": "Cadastre-se com Segurança",
    "RSVP with confirmed details. Receive event reminders and location information.": "Confirme presença com detalhes verificados. Receba lembretes de eventos e informações de localização.",
    "Follow Structured Ice-Breakers": "Siga Dinâmicas Estruturadas",
    "Participate in timed conversation rounds with prepared topics and prompts.": "Participe de rodadas cronometradas de conversa com temas e sugestões preparados.",
    "Build Your Network": "Construa Sua Rede",
    "Connect with people you met and attend future events with your new friends.": "Conecte-se com pessoas que conheceu e participe de eventos futuros com seus novos amigos.",

    # ---- partials/index/hero_en_IE.html ----
    "Connect with international newcomers in Dublin through speed-friending events.": "Conecte-se com recém-chegados internacionais em Dublin através de eventos de amizade rápida.",
    "Learn More": "Saiba Mais",

    # ---- partials/index/hero_pt_BR.html ----
    "Make new friends in Dublin! Join fun speed-friending events and meet amazing people from around the world.": "Faça novos amigos em Dublin! Participe de eventos divertidos de amizade rápida e conheça pessoas incríveis de todo o mundo.",
    "See who's going, chat before you meet, and find your tribe! 🎉": "Veja quem vai, converse antes de conhecer e encontre sua turma! 🎉",
    "See Events & People": "Ver Eventos e Pessoas",
    "Create Your Profile": "Crie Seu Perfil",

    # ---- partials/index/hero_uk_UA.html ----
    "CrossPaths is a verified platform for meeting new friends in Dublin through structured speed-friending events.": "CrossPaths é uma plataforma verificada para conhecer novos amigos em Dublin através de eventos estruturados de amizade rápida.",
    "All events are hosted by verified organizers in safe, public locations.": "Todos os eventos são realizados por organizadores verificados em locais públicos e seguros.",
    "Learn More About Safety": "Saiba Mais Sobre Segurança",

    # ---- partials/profile/details_en_IE.html ----
    "Age:": "Idade:",
    "From:": "De:",
    "Languages:": "Idiomas:",
    "Interests:": "Interesses:",
    "About:": "Sobre:",

    # ---- partials/profile/details_pt_BR.html ----
    "Hey, I'm": "Oi, eu sou",
    "years old": "anos de idade",
    "My Interests": "Meus Interesses",
    "I speak": "Eu falo",

    # ---- partials/profile/details_uk_UA.html ----
    "Edit My Profile": "Editar Meu Perfil",
    "Share Profile": "Compartilhar Perfil",
    "Member since": "Membro desde",
    "March 2026": "Março de 2026",
    "Country of Origin:": "País de Origem:",
    "Privacy Settings": "Configurações de Privacidade",
    "Manage your profile information": "Gerencie suas informações de perfil",

    # ---- partials/profile/header_en_IE.html ----
    # (no unique strings)

    # ---- partials/profile/header_pt_BR.html ----
    "Show your personality and let people know the real you!": "Mostre sua personalidade e deixe as pessoas conhecerem o verdadeiro você!",

    # ---- partials/profile/header_uk_UA.html ----
    "Your information is private and only shared with event attendees": "Suas informações são privadas e compartilhadas apenas com participantes do evento",

    # ---- partials/about/content_en_IE.html ----
    "Welcome to Our Community!": "Bem-vindo à Nossa Comunidade!",
    "CrossPaths connects international newcomers in Dublin through fun, friendly speed-friending events. We're all about bringing people together and building a vibrant, diverse community!": "CrossPaths conecta recém-chegados internacionais em Dublin através de eventos divertidos e amigáveis de amizade rápida. Estamos aqui para unir pessoas e construir uma comunidade vibrante e diversa!",
    "Why CrossPaths?": "Por que CrossPaths?",
    "Celebrate Diversity": "Celebre a Diversidade",
    "Meet people from all over the world!": "Conheça pessoas de todo o mundo!",
    "Make Real Friends": "Faça Amigos de Verdade",
    "Not just networking — genuine connections!": "Não é apenas networking — conexões genuínas!",
    "Have Fun!": "Divirta-se!",
    "No boring meetings — just good times!": "Sem reuniões chatas — só bons momentos!",
    "Join the Fun!": "Participe da Diversão!",
    "Whether you just arrived in Dublin or have been here for years, CrossPaths is your gateway to an amazing social circle. Come as you are, meet incredible people, and build friendships that last!": "Se você acabou de chegar em Dublin ou mora aqui há anos, CrossPaths é sua porta de entrada para um círculo social incrível. Venha como você é, conheça pessoas incríveis e construa amizades duradouras!",
    "Countries": "Países",
}


def fill_locale(locale, translations):
    po_path = BASE / locale / "LC_MESSAGES" / "messages.po"
    with po_path.open("rb") as f:
        cat = pofile.read_po(f)

    updated = 0
    for msg in cat:
        if msg.id and msg.id in translations:
            if not msg.string or msg.string != translations[msg.id]:
                msg.string = translations[msg.id]
                if "fuzzy" in msg.flags:
                    msg.flags.discard("fuzzy")
                updated += 1

    with po_path.open("wb") as f:
        pofile.write_po(f, cat)

    print(f"{locale} updated: {updated}")


if __name__ == "__main__":
    fill_locale("pt_BR", PT_BR)
