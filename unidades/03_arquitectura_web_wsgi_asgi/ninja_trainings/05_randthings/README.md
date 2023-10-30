# Antes de empezar
EL EJERCICIO ESTÁ EN LA CARPETA `web`, Y ESTÁ RESUELTO EN LA CARPETA `web_hecha`.

En este Ninja Training vas a desarrollar una aplicación web en Python usando WSGI donde pondrás en práctica la programación de un router a diferentes *scripts* de Python, para lo cual tendrás que analizar el **Path Parameter**. Además, también tendrás que analizar los **Query Parameters** que puedan venir.

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

Por último, si usas Windows, no podrás usar **Gunicorn**. Una opción es **Waitress**. Además, a la hora de activar el entorno virtual, tendrás que ejecutar este otro comando desde la *Power Shell*:

``` shell
$ . venv/Scripts/activate
```

E instalar a mano **Waitress**.

# Enunciado
En este Ninja Training tienes que crear una aplicación con tres páginas web:

## Página 1: home
En esta página se dará una bienvenida al sitio web y se mostrará un menú con tres enlaces a las tres páginas web.

## Página 2: números aleatorios
Esta página mostrará números aleatorios entre 1 y 1 000 000. Además, esta página web podrá recibir dos parámetros por **GET**:

- from: con un número inicial.
- to: con un número final.

En ese caso, en vez de generar un número entre 1 y 1 000 000, generará un número entre los indicados `from` y `to`.

## Página 3: frase al azar
En esta página se cargará, al azar, una de las frases que puedes ver en el fichero de texto `assets/sentences.txt`.
