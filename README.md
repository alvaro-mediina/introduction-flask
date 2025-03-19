# 🔥 Introducción a Flask 🐍

Este repositorio está 100% pensado para realizar el tutorial al Framework de Python, Flask y aprender a utilizar algunas de sus funcionalidades.

# Básicos

- @ es el decorado de invocación para las rutas.

```python
# Decorador de invocación para la ruta raíz
@app.route('/')
```

- Van por encima de las funciones que se van a ejecutar cuando se invoque la ruta.

- Ejemplo simple de cómo insertar un texto en una web a través de una función.

```python
@app.route('/')
def hello_world():
    return "Hola Mundo"
```

> [!TIP]
> Algo que noté que no se puede hacer
> es que si ponés un @app.route('/') y una función, luego si volvés a repetir la función la que se ejecutará será la primera que figura en el código estático.

- El protocolo que utiliza `Flask` para la comunicación por internet es **HTTP**. Dado que `Flask` es un framework utilizado para el manejo de APIs web

## Utilización del método GET

```python
@app.route('/usuario/<user_id>')
def get_user(user_id):
    """
    Implementación de un GET con un código de éxito 200.
    """
    # Definimos un diccionario para representar a un usuario
    user = { "id": user_id,
             "name": "Santiago",
             "tel": "3884392243"}

    # /usuario/123?query=query_test
    #Agrego a los argumentos la clave "query"
    query = request.args.get("query")

    #Si la clave existe entonces al usuario en la clave 'query' asigno la variable query
    if query:
        user["query"] = query

    #Devuelvo los datos de la variable usuario y un código de éxito 200
    return jsonify(user), 200
```

## Utilización del método POST

```python
#En el decorado se indica que el método HTTP será POST
@app.route('/usuarios', methods=['POST'])
def create_user():
    """
    Crea un usuario y agrega a los campos usuario creado si es que fué exitoso.
    """
    #Obtener JSON
    data = request.get_json()
    #Creo un nuevo dato en data llamado "status" y le asigno el string "usuario creado"
    data["status"] = "user created"

    #Devuelvo la data y un código de éxito para usuario creado
    return jsonify(data), 201
```

# Definiciones importantes

- **Endpoint**: es una URL (Uniform Resource Locator) o ruta dentro de una API que permite interactuar con un servidor para realizar una operación específica, como obtener datos, enviarlos o actualizarlos

# 4 Grandes métodos que utiliza una API web | Métodos HTTP

- **GET**: obtener información.
- **POST**: enviar información.
- **PUT**: actualizar información.
- **DELETE**: eliminar información.
