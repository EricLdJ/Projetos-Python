import random
from tkinter import *
from tkinter import filedialog

# listas

def gerar_senha():
    global aparecer_senha
    numeros = [0,1,2,3,4,5,6,7,8,9]
    caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Ç","", "',", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ",", "|", ";", ":", "'", "'", "<", ">", ",", ".", "/", "?", "°"]

    # Escolhas

    tamanho = int(entrada.get())

    # comandos
    senha = []
    for i in range(tamanho):
        if i % 2 == 0:
            senha.append(str(random.choice(numeros)))
        else:
            senha.append(random.choice(caracteres))

    aparecer_senha.insert(END, "".join(senha))
    aparecer_senha.configure(state="disabled")
    aparecer_senha.configure(state="normal")
    aparecer_senha.delete("1.0", END)
    aparecer_senha.insert(END, "".join(senha))

def copiar():
    janela.clipboard_clear()
    janela.clipboard_append(aparecer_senha.get("1.0", END))

def salvar_arquivo():
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("text files", "*.txt"), ("All Files", "*.*")])
    if arquivo:
        with open(arquivo, "w") as file:
            file.write(aparecer_senha.get("1.0", END))

# janela gráfica

janela = Tk()
janela.title("Gerenciador de Senhas")

# textos

texto_boasvindas = Label(janela, text="Seja bem vindo ao seu gerenciador de senhas!")
texto_boasvindas.grid(column=0, row=0)

texto_orientação = Label(janela, text="Digite a quantidade de caracteres que deseja e clique no botão para gerar.")
texto_orientação.grid(column=0, row=1)

# caixas de perguntas

entrada = Entry(janela)
entrada.grid(column=0, row=2)

# botões

botao = Button(janela, text="Gerar", command=gerar_senha)
botao.grid(column=0, row=3)

botao_copiar = Button(janela, text="Copiar", command=copiar)
botao_copiar.grid(column=0, row=5)

botao_salvar = Button(janela, text="Salvar Senha", command=salvar_arquivo)
botao_salvar.grid(column=0, row=6)

# prints

aparecer_senha = Text(janela, height=1, state="disabled")
aparecer_senha.grid(column=0, row=4)

janela.mainloop()
