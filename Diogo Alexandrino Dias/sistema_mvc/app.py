from flask import Flask
from flask_mysqldb import MySQL # Biblioteca mysql flask
from controllers.produto_controller import produto_bp
import config

app = Flask(__name__) # Instanciar o Flask
app.config.from_object(config) # Configurando variaveis

mysql = MySQL(app)

# Passa a conexao para os controllers
app.mysql = mysql

# Registrar o controller
app.register_blueprint(produto_bp)

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)