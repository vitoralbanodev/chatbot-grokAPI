from dataclasses import dataclass, field
from typing import Any, Callable, List, Sequence, Tuple
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import ConfiguracaoApp

MessagePair = Tuple[str, str]
ChainFactory = Callable[[Sequence[MessagePair]], Any]

@dataclass
class SessaoChat:
    chain_factory: ChainFactory
    config: ConfiguracaoApp
    historico: List[MessagePair] = field(default_factory=list)
    topicos_cobertos: List[str] = field(default_factory=list)
    inicio_sessao: datetime = field(default_factory=datetime.now)

    def enviar_mensagem_usuario(self, texto: str) -> str:
        self.historico.append(('user', texto))
        self._analisar_topico(texto)
        cadeia = self.chain_factory(self._mensagens_para_prompt())
        resposta = cadeia.invoke({})
        self.historico.append(('assistant', resposta.content))
        return resposta.content

    def resetar(self) -> None:
        self.historico.clear()
        self.topicos_cobertos.clear()
        self.inicio_sessao = datetime.now()

    def get_duracao_sessao(self) -> str:
        duracao = datetime.now() - self.inicio_sessao
        minutos = int(duracao.total_seconds() // 60)
        return f"{minutos} minutos"

    def get_resumo_topicos(self) -> str:
        if not self.topicos_cobertos:
            return "Nenhum tópico específico coberto ainda."
        topicos_unicos = list(set(self.topicos_cobertos))
        return f"Tópicos abordados: {', '.join(topicos_unicos[:5])}"

    def _analisar_topico(self, texto: str) -> None:
        texto_lower = texto.lower()
        topicos_keywords = {
            'mira': ['mira', 'aim', 'crosshair', 'precisão', 'atirar'],
            'mapa': ['mapa', 'dust2', 'mirage', 'inferno', 'posição', 'lugar'],
            'economia': ['economia', 'comprar', 'dinheiro', 'save', 'buy', 'eco'],
            'granada': ['granada', 'smoke', 'flash', 'molotov', 'utilidade'],
            'arma': ['arma', 'ak', 'm4', 'awp', 'recuo', 'spray'],
            'equipe': ['equipe', 'time', 'comunicação', 'junto', 'coordenação']
        }
        for topico, keywords in topicos_keywords.items():
            if any(keyword in texto_lower for keyword in keywords):
                self.topicos_cobertos.append(topico)
                break

    def _mensagens_para_prompt(self) -> List[MessagePair]:
        return [('system', self.config.prompt_sistema)] + self.historico

def fabrica_padrao(chat_client: ChatGroq) -> ChainFactory:
    def _fabrica(mensagens: Sequence[MessagePair]) -> Any:
        template = ChatPromptTemplate.from_messages(mensagens)
        return template | chat_client

    return _fabrica