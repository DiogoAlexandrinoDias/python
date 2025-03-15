import mysql.connector
from config import Config  

class usuariomodel:
    
    def __init__(self):
        # Iniciando a configuração 
        self.config = Config()

        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )

        # Faz o cursor trazer o resultado em dicionarios
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_user(self) :
         """ Retonar a lista de todos os usuarios """
         query = 'SELECT usuario_id, usuario_nome, idade FROM usuarios'
         self.cursor.execute(query)
         return self.cursor.fetchall()
     
    def insert_user(self, usuario_nome, idade):
         """ Inserir um nome na tabela de usuarios """
         query = 'INSERT INTO usuarios (usuario_nome, idade) VALUES (%s, %s)'
         self.cursor.execute(query,(usuario_nome,idade))
         self.connection.commit() #confirma a transação
         return self.cursor.lastrowid
     
    def   get_user_by_id(self, usuario_id):
         """ Busca usuario pelo ID """ 
         query  = "SELECT usuario_id, usuario_nome, idade FROM usuario WHERE usuario_id  = %s"
         self.cursor.execute(query, usuario_id)
         return self.cursor.fetchone()

    def delete_user_by_id(self, usuario_id) :
         """ Deletar um usuario pelo id  """
         query = 'DELETE FROM usuarios WHERE usuario_id = %s'
         self.cursor.execute(query, usuario_id)
         self.connection.commit()
         return self.cursor.rowcount
    
    def update_user_by_id (self, usuario_id, usuario_nome, idade):
         """ Atualizar um usuario pelo id """
         query = 'UPDATE usuarios SET usuario_nome = %s, idade = %s WHERE usuario_id = %s'
         self.cursor.execute(query,(usuario_nome,idade,usuario_id))
         self.connection.commit()
         return self.cursor.rowcount
    
    def close_connection_user(self):
        self.cursor.close()
        self.connection.close()
         
    

