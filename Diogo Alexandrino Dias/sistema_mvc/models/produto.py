class Produto:
    # POO -> Construtor
    def __init__(self, id=None, nome=None, preco=None):
        self.id = id
        self.nome = nome
        self.preco = preco


    @staticmethod # Permite varios acessos
    def listar(mysql):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, nome, preco FROM produtos")
        resultados = cursor.fetchall() # Executar
        cursor.close()
        # [Produto{id, nome, preco}]
        # [ ] -> Array -> Lista
        # Produto{id, nome, preco}
        # r -> row -> linha
        return [Produto(id=r[0], nome=r[1], preco=r[2]) for r in resultados]        
    
    def salvar(self, mysql):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco) values (%s, %s)", (self.nome, self.preco))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def buscar_por_id(mysql, id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, nome, preco FROM produtos WHERE id = %s", (id,))        
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            return Produto(id=resultado[0], nome=resultado[1], preco=resultado[2])
        return None


    def atualizar(self, mysql):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE produtos SET nome = %s, preco = %s WHERE id = %s", (self.nome, self.preco, self.id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def deletar(mysql, id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
        mysql.connection.commit()
        cursor.close()
        
                        