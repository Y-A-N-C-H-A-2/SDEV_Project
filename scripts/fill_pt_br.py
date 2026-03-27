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
