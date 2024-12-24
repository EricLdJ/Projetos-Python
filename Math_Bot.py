from chatterbot import ChatBot

bot = ChatBot("Math_bot", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

while True:
    try:
        user_text = input("Digite a conta matemática que queira resolver: ")
        
        if user_text.lower() == "sair":
            print("Foi ótimo calcular com você!")
            break
        
        resposta = bot.get_response(user_text)
        
        if resposta:
            print("Math_bot: " + str(resposta))
        else:
            print("Math_bot: Desculpe, mas não consegui entender a conta.")
        
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("Foi ótimo calcular com você!")
        break
