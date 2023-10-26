# Antes de empezar
ESTE NINJA TRAINING SE HARÁ EN CLASE CON EL ACOMPAÑAMIENTO DEL PROFESOR.

EL EJERCICIO ESTÁ EN LA CARPETA `web`, Y ESTÁ RESUELTO EN LA CARPETA `web_hecha`.

En este Ninja Training vas a desarrollar una aplicación web en Python usando WSGI donde aprenderás a enrutar las peticiones a diferentes *scripts* de Python, para lo cual tendrás que analizar el **Path Parameter**.

Antes de empezar, dentro de la carpeta `web`, crea un entorno virtual e instala las dependencias o requirimientos:

``` shell
$ python -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Recuerda que para probar tu aplicacion web basta con arrancar **Gunicorn** dentro de la carpeta `web`, una vez has activado el entorno virtual:

``` shell
(venv) $ gunicorn -b localhost:8000 server:app --reload
```

Por último, si usas Windows, no podrás usar **Gunicorn** y, a la hora de activar el entorno virtual, tendrás que ejecutar este otro comando desde la *Power Shell*:

``` shell
$ . venv/Scripts/activate
```

# Un Path Param por aquí y un Path Param por allá
En este caso, tenemos un *script* llamado `router.py` porque es este *script* el que tiene la función que **Gunicorn** va a ejecutar y es el encargado de:

1. Analizar el *Path Parameter* y, en función de su valor, ejecutar una función u otra
2. Cada una de esas funciones será la encargada de renderizar una vista y enviarla como resultado

El programa en sí ya está hecho, analízalo y trata de comprenderlo.

# Añade una nueva ruta
Te toca volar a ti sol@: añade una nueva página para el lenguaje de programación `PHP`.
