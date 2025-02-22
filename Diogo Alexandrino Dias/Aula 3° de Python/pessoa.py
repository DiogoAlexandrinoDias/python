
# Definição da Classe Pessoa
class Pessoa:   

     # Método construtor
     # é chamado quando criamos um objeto

    def __init__(self, nome, idade, altura):
        # Atribuir a entidade
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def aprensetar(self):
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos, e tenho {self.altura} tudo isso de altura')
           

p1 = Pessoa("Rafael", 34, "1.50")
p2 = Pessoa("Guilherme", 7, "1.35")
p3 = Pessoa("Alberto", 18, "1.95")

p1.aprensetar()
p2.aprensetar()
p3.aprensetar()
