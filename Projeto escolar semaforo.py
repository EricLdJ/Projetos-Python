from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtCore import Qt, QTimer
import sys

app= QApplication([])
app.setApplicationName("Semáforo Interativo")
label= QLabel("Verde", alignment= Qt.AlignCenter)

palavras= {"Verde": 5000, 
           "Amarelo": 3000, 
           "Vermelho":7000}

timer= QTimer() # declarar a variável timer antes de utilizar em qualquer função

def atualizar_palavra():
    palavra_atual = label.text()
    tempo_atual = palavras[palavra_atual]

    proxima_palavra = list(palavras.keys())[(list(palavras.keys()).index(palavra_atual) + 1) % len(palavras)]
    proximo_tempo = palavras[proxima_palavra]

    label.setText(proxima_palavra)
    timer.start(proximo_tempo)

def pular_para_Verde():
    timer.stop()
    label.setText("Verde")
    timer.start(palavras["Verde"])

def pular_para_Vermelho():
    timer.stop()
    label.setText("Vermelho")
    timer.start(palavras["Vermelho"])

def alterar_tempo():
    valor = int(caixa_tempo.text())
    palavras["Verde"] = valor
    palavras["Amarelo"] = int(valor / 2)
    palavras["Vermelho"] = valor * 2
    timer.start(palavras["Verde"])


timer.timeout.connect(atualizar_palavra)
timer.start(palavras["Verde"])

botao_verde= QPushButton("Verde")
botao_verde.clicked.connect(pular_para_Verde)

botao_vermelho= QPushButton("Vermelho")
botao_vermelho.clicked.connect(pular_para_Vermelho)

caixa_tempo= QLineEdit()
caixa_tempo.setText(str(palavras["Verde"]))
caixa_tempo.editingFinished.connect(alterar_tempo)

widget= QWidget()
layout= QVBoxLayout()

layout.addWidget(QLabel("Tempo (ms)"))
layout.addWidget(caixa_tempo)
layout.addWidget(botao_verde)
layout.addWidget(botao_vermelho)

widget.setLayout(layout)

janela_principal = QMainWindow()
janela_principal.setCentralWidget(widget)

label.show()
janela_principal.show()

sys.exit(app.exec_())
