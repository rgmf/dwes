# Antes de empezar
ESTE NINJA TRAINING SE HARÁ EN CLASE CON EL ACOMPAÑAMIENTO DEL PROFESOR.

En este Ninja Training estudiarás cómo funciona WSGI realizando tu primera aplicación web con Python usando Gunicorn como middleware WSGI.

# De vueltas con los "Hola Mundo"
El fichero `a_server.py` contiene un servidor **WSGI** mínimo que podemos servir usando **Gunicorn**. Analízalo. El poco código que contiene está explicado. En el siguiente apartado te explico cómo ponerlo en marcha.

# ¿Cómo poner en marcha todo esto?
Lo vamos a hacer con **Gunicorn** (una de las implementaciones, sino la implementación, más populares de **WSGI**). Sigue estos pasos:

1. Crea un entorno virtual con Python: `python -m venv venv`
2. Activa el entorno virtual, que en GNU/Linux sería así: `. venv/bin/activate` y en Windows así: `. venv/Scripts/activate`
3. Instala **Gunicorn** en tu entorno virtual: `pip install gunicorn`

Arranca **Gunicorn** para servir tu aplicación Python: `gunicorn a_server:app -b localhost:8000`, donde:

- `a_server` hace referencia al fichero de Python donde está tu programa
- `app` es la función que será llamada por **Gunicorn** cada vez que se hagan peticiones
- `localhost:8000` es donde va a escuchar **Gunicorn**

Así, ya solo tienes que abrir tu navegador web y escribir en la barra de direcciones la dirección web [http://localhost:8000](http://localhost:8000).

# Lo típico es enviar como respuesta un HTML
La versión `b_server.py` es similar a `a_server.py` en el que el único cambio ha sido que enviamos en el cuerpo de la respuesta código HTML en vez de texto plano.

Para ponerlo en marcha: `gunicorn b_server:app -b localhost:8000`.

# Los "query parameters"
En la versión `c_server.py` puedes ver cómo obtenemos los **query parameters** que los clientes web envían.

Estas **query parameters** nos llegan a través del parámetro `environ` de la aplicación. En el código está documentado.

Por cierto, si quieres "printear cosas" para ver/depurar partes del código en la terminal tendrás que ejecutar **Gunicorn** con la opción `--capture-output`:

``` shell
$ gunicorn --capture-output -b localhost:8000 c_server:app
```

¡Qué pesadilla!, ¡cada vez que hago cambios tengo que parar y arrancar Gunicorn! Sí, pero puedes usar la opción `--reload` si quieres que lo haga él automáticamente. Esta es una opción que **no debes usar en producción**, solo en el entorno de desarrollo.

``` shell
$ gunicorn --capture-output -b localhost:8000 c_server:app
```

# Parseando y tratando los "query parameters"
En `d_server.py` tienes una aplicación web que espera dos números por **query parameters** llamados `num1` y `num2` y los suma, mostrando el resultado en una página web.

# Bad Request
En el `d_server.py` anterior hay que retocar el código para comprobar que llegan, efectivamente, dos números. Así, pueden pasar dos cosas:

1. Llegan los números, así que enviamos la respuesta con código 200 porque todo fue bien.
2. Hay errores en los "query parameters" y, como no llega lo que esperamos, significa que la petición es incorrecta. Tendemos que enviar una respuesta con un 401 de "Bad Request".

Lo tienes hecho en el `e_server.py`. Lee el código y trata de entenderlo.

# Tus primeras horas de vuelo
Escribe un nuevo programa llamado `f_my_server.py` que reciba un nombre en un "query parameter" llamado `name` y te salude.

Si no llegara el `name` en el "query parameter" entonces devuelve un **Bad Request** (con código 401).

En el *script* `f_server.py` tienes la solución.
