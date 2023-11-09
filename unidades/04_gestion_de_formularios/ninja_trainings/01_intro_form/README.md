# Antes de empezar
ESTE NINJA TRAINING SE HARÁ EN CLASE CON EL ACOMPAÑAMIENTO DEL PROFESOR.

# Descripción
En este Ninja Training aprenderás a manejar formularios con Python y WSGI.

Para el procesamiento de formularios que nos llegan por **GET** lo tenemos fácil porque hay que usar todo lo que ya hemos aprendido. No llegaría como si de **Query Parameters** se tratara y hay que procesar los datos de la misma manera que hasta ahora:

``` python
from urllib.parse import parse_qs
data: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])
```

No obstante, lo normal es que los datos de los formularios nos lleguen por **POST**, y esta será la novedad en este Ninja Training.

Además, tenemos veremos cómo devolver el formulario al usuario con los datos que ya ha introducido y los errores que se hayan podido cometer.

# Directo al código
En la carpeta `web_done` hay gran parte del código que vamos a escribir hecho. Usaremos en clase la versión `web` donde tenemos lo mínimo para empezar el manejo de formularios en Python.
