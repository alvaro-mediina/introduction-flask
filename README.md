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

# 4 Grandes métodos que utiliza una API web

- **GET**: obtener información.
- **POST**: enviar información.
- **PUT**: actualizar información.
- **DELETE**: eliminar información.
