# Manejo de cookies con Python y WSGI
Las cookies se manejan vía cabeceras HTTP.

Resumiendo: los servidores envían cookies al cliente. El cliente las guarda y cada vez que hace una petición a dicho servidor envía las cookies en las cabeceras del *request*.

Objetivo básico de las cookies: las cookies permiten a los servidores web reconocer quién está haciendo las peticiones.

Las cookies siguen este formato: `<nombre de la cookie>=<valor de la cookie>`. Por ejemplo: `course=dwes` es una cookie llamada *course* con valor *dwes*.

## Enviar cookies
Para enviar una cookie al cliente lo harás por medio de las cabeceras HTTP que puedes enviar en el `callback` de la función que implementamos.

> Recuerda que el callback es el parámetro al que estamos llamando normalmente `start_response`

Por ejemplo, si queremos enviar una cookie al cliente llamada `name` y con valor `Alice` tendremos que añadir esta tupla en la lista de cabeceras del segundo argumento del `callback`:

```python
("Set-Cookie": "name=Alice")
```

- `Set-Cookie` es la cabecera HTTP, y
- `name=Alice` es la cookie en sí (la cookie se llama `name` y su valor es `Alice`).

Aquí tienes la función completa en la que se envía, junto a la respuesta, dos cookies:

```python
from typing import Callable, Iterator


def app(environ: dict, start_response: Callable) -> Iterator:
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

	start_response(
        "200 OK",
        [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data_in_bytes))),
			("Set-Cookie", "name=Alice"),
			("Set-Cookie", "age=20")
        ]
    )

    return iter([data_in_bytes])
```

## Recibir cookies
Las cookies son enviadas por los clientes (navegadores web) y el middleware WSGI nos las envía por medio del primer parámetro de la funición que implementamos: el parámetro al que normalmente estamos llamando `environ` que, te recuerdo, no es más que un diccionario cuyas claves son `str`.

La clave de este diccionario donde vamos a encontrar las cookies es `"HTTP_COOKIE"`. No siempre va a llegar esta clave, así que tendrás que comprobar si está. Tienes dos opciones:

```python
# OPCIÓN 1:
name_op1: str = environ["HTTP_COOKIE"] if "HTTP_COOKIE" in environ else ""

# equivale a:
if "HTTP_COOKIE" in environ:
	name_op1: str = environ["HTTP_COOKIE"]
else:
	name_op1: str = ""
	
# OPCIÓN 2:
name_op2: str = environ.get("HTTP_COOKIE", "")
```

La dificultad está en que las cookies nos llegan en crudo y las tenemos que *parsear*. Por ejemplo, si nos llegan dos cookies: `name=Alice` y `age=20` en `environ["HTTP_COOKIE"]` las vamos a recibir en un único `str` tal que así:

```python
"name=Alice; age=20"
```

Así pues, en clase, estamos usando la clase `SimpleCookie` del módulo de Python `http.cookies`. Con esta clase, recuperar el nombre y la edad sería más fácil:

```python
from http.cookies import SimpleCookie


# Desde aquí damos por sentado que llega "HTTP_COOKIE" en environ.
name: str = ""
age: int = 0

cookies: SimpleCookie = SimpleCookie()
cookies.load(environ["HTTP_COOKIE"])

if "name" in cookies:
	name = cookies["name"].value

if "age" in cookies and cookies["age"].value.isdigit():
	age = int(cookies["age"].value)
```

## Solucionando los problemas con los caracteres especiales
Los nombres de las cookies no pueden tener espacios. Lo mejor es que sean nombre cortos y en minúsculas. En cuanto a los valores tampoco pueden tener espacios, ni acentos, entre otras cosas. A veces vas a tener que añadir como valor de una cookie algún carácter no válido.

No pasa nada. Hay solución.

Esta solución pasa por usar las funciones `quote` para enviar cookies y `unquote` para cuando las recibamos.

Estas dos funciones forman parte del módulo de Python `urllib.parse`.

Veamos todo esto en código.

Imagina que tienes el valor de una cookie que quieres enviar en una variable llamada `cookieValue`. Ese valor lo quieres poner en una cookie a la que vamos a llamar `"ejemplo"`. Verás en el código que estoy *codificando* el valor que le asigno a esa cookie con `quote`:

```python
from urllib.parse import quote


cookieValueEncoded: str = quote(cookieValue)

start_response(
	"200 OK",
	[
		"Set-Cookie": f"ejemplo={cookieValueEncoded}"
	]
)
```

Ahora, cuando recibas cookies tendrás que *decodificar* los valores con `unquote`:

```python
from http.cookies import SimpleCookie
from urllib.parse import unquote


# En este ejemplo damos por sentado que tenemos "HTTP_COOKIE" en environ
# y que llega la cookie llamada "ejemplo".
cookies: SimpleCookie = SimpleCookie()
cookies.load(environ["HTTP_COOKIE"])

ejemploEncoded: str = cookies["ejemplo"].value
ejemplo: str = unquote(ejemploEncoded)
```

## El objeto Morsel
En el ejemplo anterior puedes ver esta asignación: `ejemploEncoded: str = cookies["ejemplo"].value`. Nos vamos a quedar con esta parte: `cookies["ejemplo"].value` y la vamos a analizar:

1. `cookies` es un objeto del tipo `SimpleCookie`.
2. Esta clase es como un diccionario, por eso podemos acceder a una cookie como si de un diccionario se tratara: `cookies["ejemplo"]`.
3. Cada elemento en dicho diccionario tiene un objeto del tipo `Morsel` (ahora entramos en él). Así `cookies["ejemplo"]` devuelve un `Morsel`.
4. Este objeto `Morsel` tiene un atributo llamado `value`, entre otras cosas, por eso usamos `cookies["ejemplo"].value` para obtener el valor de la cookie `"ejemplo"`.

## Recorrer el diccionario SimpleCookie
Cuando sabes cómo se llama la cookie puedes hacer lo que hemos hecho hasta ahora. El ejemplo anterior nos sirve. Sabemos que tenemos una cookie llamada `"ejemplo"` y podemos obtener su valor con `cookies["ejemplo"].value`.

Aquí te muestro un ejemplo en el que vamos a recorrer todas las cookies que tenemos en un `SimpleCookie` llamado `cookies`. Uso nombres de las variables en castellano para que puedas entender mejor el código:


```python
from http.cookies import SimpleCookie


for nombre_cookie, objeto_morsel in cookies.items():
	print(objeto_morsel.value)
```
