# Gunicorn
**Gunicorn** es un servidor que implementa la especificación **WSGI** como hemos visto en clase. Aquí, te resumo todo lo explicado en clase.

Este servidor es el que recibe las peticiones o *requests* HTTP y, por cada petición, llama a una función que estará dentro de un fichero `.py` que tenemos que desarrollar nosotros.

¿Cómo sabe Gunicorn dónde está la función que tiene que invocar por cada petición? Porque se lo indicamos nosotros cuando arrancamos el servidor:

```shell
$ gunicorn src.server:app
```

En el comando de arriba arrancamos el servidor Gunicorn y le decimos dónde está la función. En este caso la función se llama `app` y está dentro del módulo `src.server`, es decir, dentro del fichero de Python `src/server.py`.

# Nuestra aplicación WSGI
Así que, nuestra aplicación tiene que implementar la función que llamará el servidor. Esta función:

- Recibe dos parámetros:
  - Un diccionario que contiene variables CGI, y
  - Un *callback* que será utilizada por nuestra aplicación para enviar información HTTP (cabeceras HTTP) al servidor Gunicorn.
- Devuelve el cuerpo que el servidor enviará como *HTTP body*. Este valor devuelto debe ser un `Iterator` de un `str` codificado en `bytes`.

## Los parámetros de la función
El **primer parámetro** lo hemos estado llamando `environ` aunque le puedes dar el nombre que quieras. Esta variable tiene un diccionario como el siguiente (los valores son inventados y solo te muestor un pequeño conjunto de claves-valor):

```python
environ: dict[str, any] = {
	"REQUEST_METHOD": "GET",
	"QUERY_STRING": "",
	"SERVER_PROTOCOL": "HTTP/1.1",
	"HTTP_HOST": "localhost:8000",
	"PATH_INFO": "/"
}
```

El **segundo parámetro** es un *callback*, es decir, una función que podemos y debemos usar para comunicar "cosas" al servidor. Este *callback* necesita que le pasemos dos argumentos:

- En el primero le pasamos un `str` con el código de respuesta como `"200 OK"` o `"404 NOT FOUND"`, por ejemplo.
- En el segundo le pasamos una lista de tuplas, donde cada tupla define una cabecera:
  - El primer elemento de la tupla es el nombre de la cabecera, y
  - El segundo elmeento de la tupla es el valor para esa cabecera.
  
## El valor de retorno de la función
Como te he comentado arriba, lo que vas devolver es el cuerpo de la respuesta (*HTTP Response Body*) del protocolo HTTP. Será un `str` codificado en `bytes`. Es decir, en última instancia será un objeto `bytes` de Python. Eso sí, tendrás que crear un `Iterator` con este `bytes`. ¿Cómo? En el apartado siguiente lo puedes ver.

## Esqueleto de la función
Aquí tienes el esqueleto de la función documentada:

```python
from typing import Callable, Iterator


def app(environ: dict, start_response: Callable) -> Iterator:
    """Aplicación de ejemplo.

    La versión más simple con respuesta en texto plano.

    :environ dict: diccionario que contiene las variables de entorno CGI así
                   como otros parámetros y metadatos.
    :start_response Callable: es una función ("Callable") que recibe dos
                              parámetros: el estado (status) y las cabeceras
                              de la respuesta (header response).

    :return: devuelve el cuerpo de la respuesta como un "Iterator" de bytes.
             Así, se devuelve el cuerpo como "byte" y no como "str".
    """

    # Los datos que voy a enviar en el cuerpo de la respuesta. Se trata de una
	# página web en un string de Python.
    data: str = """
	<!doctype html>
	<html>
	<head>
	  <title>Título</title>
	  <meta charset="utf-8">
	</head>
	<body>
	  <h1>Hola Mundo</h1>
	</body>
	</html>
	"""

    # Lo que vamos devolver tiene que estar codificado en bytes
    data_in_bytes: bytes = data.encode("utf-8")

    # Uso el Callable que me pasa WSGI para preparar el cuerpo de la respuesta:
    # - Código de estado 200 (HTTP)
    # - Cabeceras:
    #   - El tipo de contenido (el mime/type) es texto plano
    #   - La longitud de los datos que vienen en el cuerpo
    start_response(
        "200 OK",
        [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data_in_bytes)))
        ]
    )

    # El cuerpo de la respuesta la envío como un Iterator
    return iter([data_in_bytes])
```
