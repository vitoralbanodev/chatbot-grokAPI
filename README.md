# CS2 Coach - Seu Treinador Pessoal de Counter-Strike 2

Um chatbot especialista em CS2 que te ajuda a evoluir no jogo com dicas práticas e uma vibe amigável brasileira!

## 🎮 Sobre o Coach

O CS2 Coach é um treinador virtual que utiliza inteligência artificial (Groq API + LangChain) para fornecer:
- **Dicas de mira e controle de recuo**
- **Estratégias para todos os mapas principais**
- **Gerenciamento de economia**
- **Uso de granadas e utilidades**
- **Conselhos de trabalho em equipe**

## 🚀 Como Usar

1. Instale as dependências:
```bash
pip install langchain langchain-groq
```

2. Configure sua API key da Groq (opcional - já vem com uma padrão):
```bash
export GROQ_API_KEY="sua_chave_aqui"
```

3. Execute o coach:
```bash
python main.py
```

## 💡 Comandos Rápidos

Use estes comandos para dicas específicas:
- `/mapa` - Estratégias e dicas para mapas
- `/arma` - Dicas sobre armas e controle de recuo
- `/economia` - Gerenciamento de economia do jogo
- `/granada` - Uso de granadas e utilidades
- `/mira` - Melhorias de mira e aim
- `/equipe` - Trabalho em equipe e comunicação

## 🏆 Funcionalidades

### Interface Amigável
- Mensagens motivacionais
- Acompanhamento de tempo de treino
- Resumo dos tópicos abordados
- Histórico da conversa

### Inteligência de Coaching
- Análise automática de tópicos
- Dicas personalizadas baseadas nas perguntas
- Linguagem brasileira descontraída
- Foco em melhoria prática

## 📋 Exemplo de Uso

```
🎮 Bem-vindo ao seu CS2 Coach! É nóis! 🎮

Sou seu treinador pessoal de Counter-Strike 2! Posso ajudar com:
• Mira e controle de recuo
• Estratégias de mapa (Dust2, Mirage, Inferno...)
• Economia e compras
• Granadas e utilidades
• Trabalho em equipe

Comandos rápidos:
• /mapa: Estratégias e dicas para mapas
• /arma: Dicas sobre armas e controle de recuo
• /economia: Gerenciamento de economia do jogo

Digite "x" para sair ou pergunte o que quiser sobre CS2!

Você manda a braba: /arma
🏆 CS2 Coach: E aí campeão! Pra dominar a AK-47, lembra que o recuo vai sempre pra cima e um pouco pra direita. Puxa o mouse suave pra baixo enquanto atira, nos primeiros 10 tiros. Depois disso, é melhor fazer burst de 2-3 tiros. Vai praticando no mapa de aim que você pega o jeito! Força nesse treino! 💪

💪 Valeu por treinar comigo! Continue focado e evolua sempre!
⏱️ Tempo de treino: 5 minutos
📊 Tópicos abordados: arma
```

## 🛠️ Tecnologias

- **Python 3.7+**
- **LangChain** - Framework para aplicações de LLM
- **Groq API** - Modelo Llama 3.3 70B
- **Dataclasses** - Estrutura de dados moderna

## 📂 Estrutura do Projeto

```
chatbot-grokAPI/
├── config.py          # Configurações e knowledge base de CS2
├── main.py            # Interface principal e loop de conversa
├── session.py         # Gerenciamento de sessão e análise de tópicos
└── README.md          # Este arquivo
```

---
