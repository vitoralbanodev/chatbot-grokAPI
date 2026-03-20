import os
from dataclasses import dataclass
from typing import Optional

DEFAULT_API_KEY = ''

CS2_MAPAS = ['Dust2', 'Mirage', 'Inferno', 'Cache', 'Overpass', 'Vertigo', 'Ancient', 'Nuke']
CS2_ARMAS_PRINCIPAIS = ['AK-47', 'M4A4', 'M4A1-S', 'AWP', 'Galil AR', 'FAMAS']
CS2_GRANADAS = ['HE Grenade', 'Smoke Grenade', 'Flashbang', 'Molotov', 'Incendiary']
CS2_ECONOMIA_TERMS = ['Buy round', 'Save round', 'Force buy', 'Eco round', 'Full buy']

CS2_QUICK_COMMANDS = {
    '/mapa': 'Estratégias e dicas para mapas',
    '/arma': 'Dicas sobre armas e controle de recuo',
    '/economia': 'Gerenciamento de economia do jogo',
    '/granada': 'Uso de granadas e utilidades',
    '/mira': 'Melhorias de mira e aim',
    '/equipe': 'Trabalho em equipe e comunicação'
}

class ConfiguracaoApp:
    nome_modelo: str = 'llama-3.3-70b-versatile'
    prompt_sistema: str = (
        'Você é um treinador especialista em Counter-Strike 2 (CS2) que fala com gírias brasileiras de forma amigável e descontraída. '
        'Seu objetivo é ajudar jogadores a melhorarem suas habilidades de forma objetiva e motivadora. '
        'Você deve: '
        '1. Dar dicas práticas sobre mira, movimento, granadas e estratégias de mapa '
        '2. Ensinar sobre economia do jogo (buy rounds, save rounds, force buys) '
        '3. Explicar padrões de recuo das armas principais (AK-47, M4A4, AWP) '
        '4. Compartilhar estratégias para mapas populares (Dust2, Mirage, Inferno, etc.) '
        '5. Dar conselhos sobre trabalho em equipe e comunicação '
        '6. Manter um tom amigável, encorajador e usar gírias naturais brasileiras '
        'Seja sempre breve, direto e termine suas respostas com uma palavra de motivação. '
        'Evite ser muito técnico sem explicar os termos básicos.'
    )

def configurar_chave_api(chave: Optional[str] = None) -> str:
    chave_resolvida = chave or os.environ.get('GROQ_API_KEY') or DEFAULT_API_KEY
    os.environ['GROQ_API_KEY'] = chave_resolvida
    return chave_resolvida