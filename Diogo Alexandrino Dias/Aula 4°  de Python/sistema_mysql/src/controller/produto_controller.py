from ..model.produto_model import ProdutoModel

def listar_produtos():
    """ Retorna a lista de todos os produtos (dict) """
    model = ProdutoModel()
    produtos = model.get_all_products()
    model.close_connection()
    return produtos

def cadastrar_produto(nome, preco):
    """ Cadastrar produtos no banco """
    model = ProdutoModel()
    novo_id = model.insert_product(nome,preco)
    model.close_connection()
    return novo_id

def atualizar_produto(produto_id, nome, preco):
    model = ProdutoModel()
    linhas_afetadas = model.update_product_by_id(produto_id, nome, preco)
    model.close_connection()
    return linhas_afetadas

def remover_produto(produto_id):
    model = ProdutoModel()
    linhas_afetadas = model.delete_product_by_id(produto_id)
    model.close_connection()
    return linhas_afetadas

def obter_produto(produto_id):
    model = ProdutoModel()
    produto = model.get_product_by_id(produto_id)
    model.close_connection()
    return produto  