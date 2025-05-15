# 🤖 Math_bot – Chatbot de Matemática com ChatterBot

Um chatbot simples construído em Python com a biblioteca [ChatterBot](https://github.com/gunthercox/ChatterBot), projetado para resolver expressões matemáticas informadas pelo usuário. Ideal para treinar conceitos de inteligência artificial e interações básicas com o terminal.

---

## 📌 Funcionalidades

- Resolve expressões matemáticas como somas, subtrações, multiplicações, divisões, potências e parênteses.
- Responde interativamente através do terminal.
- Detecta comandos para encerrar o programa.
- Captura interrupções como `Ctrl+C` ou `Ctrl+D` de forma segura.

---

## 🛠️ Tecnologias Usadas

- Python 3.13.2
- ChatterBot

---

## ▶️ Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/EricLdJ/Projetos-Python.git
   cd Projetos-Python
   ```

2. **Crie e ative um ambiente virtual (opcional mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install chatterbot
   ```

4. **Execute o chatbot**:
   ```bash
   python math_bot.py
   ```

---

## 💡 Exemplo de uso

```text
Digite a conta matemática que queira resolver: (5 + 3) * 2
Math_bot: 16

Digite a conta matemática que queira resolver: sair
Foi ótimo calcular com você!
```

---

## ❗ Observações

- A biblioteca `ChatterBot` pode apresentar problemas de compatibilidade com algumas versões do Python.
- Este projeto é educacional e ideal para quem está aprendendo lógica e IA básica com Python.

---

## 📚 Autor

Eric Lima de Jesus – [GitHub](https://github.com/EricLdJ)

---

## 📃 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
