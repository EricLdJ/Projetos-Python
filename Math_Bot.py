# Importa a classe ChatBot da biblioteca ChatterBot
from chatterbot import ChatBot

# Cria uma instância do ChatBot com o nome "Math_bot"
# Define o adaptador lógico para avaliações matemáticas
bot = ChatBot("Math_bot", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

# Loop principal do chatbot
while True:
    try:
        # Solicita que o usuário insira uma expressão matemática
        user_text = input("Digite a conta matemática que queira resolver: ")
        
        # Verifica se o usuário quer sair do programa
        if user_text.lower() == "sair":
            print("Foi ótimo calcular com você!")
            break
        
        # Gera uma resposta usando o bot (resolução da conta matemática)
        resposta = bot.get_response(user_text)
        
        # Verifica se a resposta foi válida e imprime
        if resposta:
            print("Math_bot: " + str(resposta))
        else:
            print("Math_bot: Desculpe, mas não consegui entender a conta.")
    
    # Captura interrupções como Ctrl+C ou Ctrl+D para encerrar o programa com elegância
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("Foi ótimo calcular com você!")
        break
