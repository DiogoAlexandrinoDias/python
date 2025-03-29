def menu():
    print('Menu da Calculadora')
    print('1 - somar')
    print('2 - subtrair')
    print('9 - sair')

def somar (n1, n2):
     return n1 + n2 

def subtrair (n1, n2):
     return n1 - n2 

def vereificarOpcao (opcao):
    if opcao == 1 :
          num1 = float(input('Digite o numero 1'))
          num2 = float(input('Digite o numero 2'))
          print(somar(num1,num2))
    elif opcao == 2 :
          num1 = float(input('Digite o numero 1'))
          num2 = float(input('Digite o numero 2'))
          print(subtrair(num1,num2))
def calculadora() :
     while True :
          menu()
          opcao = int(input('escolher uma opcao'))
          vereificarOpcao(opcao)

calculadora
















    