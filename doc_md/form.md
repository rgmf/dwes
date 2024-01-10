# Formularios en Python/WSGI
Para el manejo de los formularios vamos a usar la biblioteca de Python `multipart`. Así que instala dicha biblioteca en tu entorno virtual o añádelo al fichero `requirements.txt`.

Una vez instalada esta biblioteca, ya puedes continuar.

Los formularios los vamos a enviar siempre por `POST`, así pues, en el HTML, este sería siempre nuestro formulario:

```html
<form action="/" method="post">
   ...
   
   <input type="submit" value="Enviar">
</form>
```

Evidentemente tendrás que modificar el `action` según el caso.

Una vez hecho esto, en tu servidor (código Python) puedes saber si es la primera vez que se solicita el formulario o nos han enviado los datos del formulario por el método `GET` o `POST`:

```python
method: str = environ.get("REQUEST_METHOD", "").upper()

if method == "GET":
	# Nos han solicitado el formulario por primera vez
	pass
elif method == "POST":
	# Nos han enviado el formulario, tenemos que procesarlo y manejar los posibles errores
	pass
else:
	# Método desconocido
	pass
```

Para procesar el formulario tenemos que usar la biblioteca `multipart` y, con ella, obtener los datos que nos llegan a través del formulario:

```python
from multipart import parse_form_data


form, files = parse_form_data(environ)
```

En este código, el `form` es un diccionario que contiene los datos del formulario y donde cada clave de dicho diccionario se corresponde con el `name` que usaste en los campos del formulario.

En `files` tenemos los datos relacionados con los ficheros que se hayan enviado. En nuestro caso lo ignoramos.

## Ejemplo completo
Dado el siguiente formulario:

```html
<form action="/open/issue" method="post">
  <p>
    Descripción:<br>
    <textarea rows="4" cols="80" name="description">{description}</textarea><br>
	{description_error}
  </p>
  <p>
    Etiqueta:<br>
    <input type="text" name="label" value="{label}"><br>
	{label_error}
  </p>
  <p>
    <input type="submit" value="Enviar">
  </p>
</form>
```

Aquí tienes el marco general para el tratamiento del formulario en nuestro servidor Python/WSGI:

```python
from typing import Callable, Iterator

from multipart import parse_form_data


def app(environ: dict, start_response: Callable) -> Iterator:
    method: str = environ.get("REQUEST_METHOD", "").upper()
	context: dict[str, str] = {
		"description": "",
		"label": "",
		"description_error": "",
		"label_error": ""
	}

    if method != "POST":
	    data: str = render_template("src/views/issue_form.html", context)
	else:
	    form, files = parse_form_data(environ)
		# Maneja aquí el formulario, valídalo y en función de si es o no
		# válido envía página de información o devuelve el formulario con
		# los errores y los valores introducidos por el usuario.

    data_in_bytes: bytes = data.encode("utf-8")
    start_response("200 OK", [("Content-Type", "text/html")])

    return iter([data_in_bytes])
```
