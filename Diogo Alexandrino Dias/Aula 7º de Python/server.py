from flask import Flask, jsonify, request, render_template

# Criando aplicação em Flask!

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# GET > Buscar algo

@app.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Ola mundo como estaos voces teste!"
    })

# Lista de tarefas
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "feito": False },
    {"id": 2, "titulo": "Ler a doc", "feito": True }
]

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

#POST - Criar uma nova tarefa
""" 
Js -> (front) -> fetch
ReacJS (front) ->
insomia (Aplicativo)-> simular um front
Postman (Aplicativp) -> Simular um front

Back-end -> Modelos de API -> FULL REST
FULL-stack -> Arquiterura MVC (Model, View, Controller)
 """

@app.route('/tarefas', methods=['POSt'])
def add_tarefa():
    nova_tarefa = request.json
    nova_tarefa['id'] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa),

# Iniciar o servidor 
if __name__ == '__main__':
    app.run(debug=True)