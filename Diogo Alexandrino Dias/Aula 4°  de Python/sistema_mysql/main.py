from src.controller import produto_controller
from src.controller import usuario_controller

def exibir_menu():
    print("\nMAREA TOCA TUDO LTDA!")
    print("\n==== MENU ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - Buscar produto unico")
    print("6 - Cadastrar Usuario")
    print("7 - Listar Usuario")
    print("8 - Atualizar Usuario")
    print("9 - Deletar Usurio")
    print("10 - Buscar Usuario unico")
    print("0 - Sair")

def listar_produtos():
    print("\n --- Lista de Produtos --- ")  
    produtos = produto_controller.listar_produtos()  
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Não existe produtos cadastrados")                

def cadastrar_produto():
    print("\n --- Cadastrar produto --- ")
    nome = input("Digite o nome: ")
    preco = input("Digite o preco")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID")    

def opcao_atualizar():
    print ('\nAtualizando produuto')
    produto_id = input('Digite o ID do produto')
    nome =  input('digite o nome do produto')
    preco = input('Digite o preco do produto')

    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
    if linhas > 0: #quantidade de linhas modificadas
        print('produto atualizado com sucesso!')
    else:
        print('nenhum produto foi atualizado')
        
""" def deletar_produto():
    print ('\nDeletando produuto')
    produto_id = input('Digite o ID do produto')
    nome =  input('digite o nome do produto')
    preco = input('Digite o preco do produto')

    linhas = produto_controller.remover_produto(produto_id, nome, preco)
    if linhas > 0: #quantidade de linhas modificadas
        print('produto deletado com sucesso!')   
    else:
        print('nenhum produto foi deletado ')   """

def listar_usuario():
    print("\n --- Lista de Usuario --- ")  
    usuarios = usuario_controller.listar_usuarios()  
    if usuarios:
        for usuario in usuarios:
            print(f"usuario_id: {usuario['usuario_id']}, usuario_nome : {usuario['usuario_nome']}, idade: {usuario['idade']}")
    else:
        print("Não existe Usuario cadastrados")

def US_opcao_atualizar():
    print ('\nAtualizando produuto')
    usuario_id = input('Digite o ID do produto')
    USnome =  input('digite o nome do produto')
    idade = input('Digite o preco do produto')

    linhas = produto_controller.atualizar_produto(usuario_id, USnome, idade)
    if linhas > 0: #quantidade de linhas modificadas
        print('produto atualizado com sucesso!')
    else:
        print('nenhum produto foi atualizado')

def cadastrar_usuario():
    print("\n --- Cadastrar produto --- ")
    USnome = input("Digite seu nome: ")
    idade = input("Digite sua idade")
    usuario_id = usuario_controller.cadastrar_usuario(USnome, idade)
    print(f"Usuario cadastrado com sucesso com o novo ID")     

# mian -> inicializar o projeto 
def main ():
# while True para repetir mesmo que a opção digitada esteja errada
    while True:

        exibir_menu()
        opc = input ('escolha uma opção: ')  

        if opc == '1' :
            cadastrar_produto()
        elif opc == '2':
            listar_produtos()
        elif opc == '3':
            opcao_atualizar()     
        #elif opc == '4' :
            #pass
        elif opc == '6':
            cadastrar_usuario()
        elif opc == '7':
            listar_usuario()     
        elif opc == '8' :
            US_opcao_atualizar()
        elif opc == '0' :
            print('saindo do sistema....')
            # sys.exit(0) 
        else:
            print('Opção invalida, tente novamente...')

if __name__ == '__main__':
    main()                    