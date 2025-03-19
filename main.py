from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Escribe en HTML al root el string "Hola Mundo"
    """
    return "Hola Mundo";


@app.route('/usuario/<user_id>')
def get_user(user_id):
    """
    Implementación de un GET con un código de éxito 200.
    """
    user = { "id": user_id,
             "name": "Santiago",
             "tel": "3884392243"}
    
    # /usuario/123?query=query_test
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route('/usuarios', methods=['POST'])
def create_user():
    """
    Crea un usuario y agrega a los campos usuario creado si es que fué exitoso.
    """
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201



if __name__ == '__main__':
    app.run(debug=True)

