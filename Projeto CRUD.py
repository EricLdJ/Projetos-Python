class Pessoa:
    def __init__(self, nome, cpf, identificador):
        self.nome = nome 
        self.cpf = cpf
        self.identificador = identificador

    def exibir(self):
        print(self.nome, self.cpf, self.identificador)

class Repositorio:
    def __init__(self):
        self.lista = []

    def add(self,pessoa):
        self.lista.append(pessoa)

    def remove(self,cpf):
        self.lista = [p for p in self.lista if p.cpf != cpf]

    def salvar(self, arquivo):
        with open(f"{arquivo}.csv", "w") as f:
            f.write("cpf, nome, identificador\n")
            for p in self.lista:
                f.write(f"{p.cpf}, {p.nome}, {p.identificador}\n")

    def recuperar(self, arquivo):
        try:
            with open(arquivo, "r") as f:
                self.lista = [
                    Pessoa(*linha.strip().split(",")) for linha in f.readlines()
                ]
        except FileNotFoundError:
            print("Arquivo não encontrado.")
###################Menu###################

    @staticmethod
    def menu():
        while True:  # Loop para garantir que o usuário insira um número válido
            try:
                print("=" * 15)
                print("Opções: \n1-Listar  \n2-Inserir  \n3-Salvar  \n4-Excluir  \n5-Recuperar  \n0-Sair")
                print("=" * 15)
                opcao = int(input("Digite sua opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:  # Verifica se a opção é válida
                    return opcao
                else:
                    print("Opção inválida! Escolha um número entre 0 e 5.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

    
    @staticmethod
    def recopessoa():
        nome = input("Digite o Nome: ")
        cpf = input("Digite o CPF: ")
        identificador = input("Digite o Identificador: ")
        return Pessoa(nome, cpf, identificador)    


if __name__ == "__main__":
    rep = Repositorio()
    opt= -1
    while opt != 0:
        opt = rep.menu()
        if opt == 1:
            for p in rep.lista:
                p.exibir()
        elif opt == 2:
            rep.add(rep.recopessoa())
        elif opt == 3:
            arquivo = input("Nome do arquivo: ")
            rep.salvar(arquivo)
        elif opt == 4:
            cpf = input("Digite o CPF: ")
            rep.remove(cpf)
        elif opt == 5:
            arquivo = input("Nome do arquivo: ")
            rep.recuperar(arquivo)
