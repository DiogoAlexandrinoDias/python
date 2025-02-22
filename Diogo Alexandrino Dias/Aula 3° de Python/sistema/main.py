from app.controllers.clienteController import clienteController

def exibir_menu():
    print("/n==== MENU ====")
    print("1 - Cadastrar clientes")
    print("2 - Listar clientes")
    print("3 - Cadastrar Produtos")
    print("4 - Listar Produtos")
    print("0 - Sair do Sistema")

def main():
    cntrlCliente = clienteController()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do cliente: ")
            email = input("E-mail: ")
            idade = int(input("Idade: "))
            # Salvariamos no Banco de dados
            cntrlCliente.criar_cliente(nome, email, idade)

        elif opc == "2":
            # listar do banco de dados clientes
            clientes = cntrlCliente.listar_clientes()

            for index, cliente in enumerate(clientes, 1):
                # index -> Posicao atual do cliente listado
                # __str__ -> Cliente => Cliente(nome="", email="", idade="")
                print(f"{index}. {cliente}")

            print("Listar")
        elif opc == "3":
            nome = input("Nome do produto: ")         
            preco = float(input("Preço: "))
        elif opc == "4":
            # listar do banco de dados os produtos
            print("listar")
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida. Tente novamente.")

if __name__ == "__main__":
    main()


