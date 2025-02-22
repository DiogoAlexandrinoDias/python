class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto(nome={self.nome}, preco={self.preco})"