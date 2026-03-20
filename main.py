from langchain_groq import ChatGroq
from config import ConfiguracaoApp, configurar_chave_api, CS2_QUICK_COMMANDS
from session import SessaoChat, fabrica_padrao

def roda_console(sessao: SessaoChat) -> None:
    print('🎮 Bem-vindo ao seu CS2 Coach! É nóis! 🎮\n')
    print('Sou seu treinador pessoal de Counter-Strike 2! Posso ajudar com:')
    print('• Mira e controle de recuo')
    print('• Estratégias de mapa (Dust2, Mirage, Inferno...)')
    print('• Economia e compras')
    print('• Granadas e utilidades')
    print('• Trabalho em equipe\n')
    print('Comandos rápidos:')
    for cmd, desc in CS2_QUICK_COMMANDS.items():
        print(f'• {cmd}: {desc}')
    print('\nDigite "x" para sair ou pergunte o que quiser sobre CS2!\n')
    
    while True:
        pergunta = input('Lança tua dúvida: ')
        if pergunta.strip().lower() == 'x':
            break
        
        if pergunta.strip().lower() in CS2_QUICK_COMMANDS:
            pergunta = f"Me dê dicas sobre {CS2_QUICK_COMMANDS[pergunta.strip().lower()].lower()}"
        
        resposta = sessao.enviar_mensagem_usuario(pergunta)
        print(f'🏆 CS2 Coach: {resposta}')

    print('\n💪 Valeu por treinar comigo! Continue focado e evolua sempre!')
    print(f'⏱️ Tempo de treino: {sessao.get_duracao_sessao()}')
    print(f'📊 {sessao.get_resumo_topicos()}')
    
    if sessao.historico:
        print('\n📋 Resumo do treino:')
        for papel, texto in sessao.historico:
            if papel == 'user':
                print(f'• Jogador: {texto}')
            else:
                print(f'• Coach: {texto[:50]}...' if len(texto) > 50 else f'• Coach: {texto}')

def main() -> None:
    configurar_chave_api()
    config = ConfiguracaoApp()
    cliente = ChatGroq(model=config.nome_modelo)
    sessao = SessaoChat(fabrica_padrao(cliente), config)
    roda_console(sessao)

if __name__ == '__main__':
    main()