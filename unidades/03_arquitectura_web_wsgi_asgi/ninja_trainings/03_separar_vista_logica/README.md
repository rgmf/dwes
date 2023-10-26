# Antes de empezar
ESTE NINJA TRAINING SE HARÁ EN CLASE CON EL ACOMPAÑAMIENTO DEL PROFESOR.

EL EJERCICIO ESTÁ EN LA CARPETA `web`, Y ESTÁ RESUELTO EN LA CARPETA `web_hecha`.

En este Ninja Training vas a desarrollar una aplicación web en Python usando WSGI donde aprenderás a separar vista de lógica.

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

# Para comenzar, cada cosa en su sitio
Escribe una aplicacion en Python que se llame `server.py` dentro de `web` que cargue la página o vista `views/spanish.html` inyectando una lista en HTML de tres lenguajes de programación: Python, Java y PHP.

Como ves la vista `views/spanish.html` está preparada para inyectar/interpolar contenido debajo del `h1`, en el *placeholder* que puedes ver.

Tu aplicación web tendrá que cargar la vista en un string y formatear dicho string añadiendo la lista en HTML de lenguajes en el *placeholder*.

# Multilenguaje
Modifica tu aplicación web para que sea capaz de cargar una vista u otra en función de lo que venga en las *Query Parameters*:

- Si llega el valor `en` para `lang` entonces cargará la vista `views/english.html`
- En otro caso cargará la vista `views/spanish.html`
