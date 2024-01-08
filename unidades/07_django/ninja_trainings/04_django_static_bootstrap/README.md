# Antes de empezar
El proyecto por hacer, que tienes en la carpeta `todo`, contiene el código completo del ninja training anterior. A efectos prácticos es como si hubiéramos descargado el código fuente de un repositorio de Git y, por tanto, tenemos que ponerlo en marcha.

¿Cómo ponemos en marcha un proyecto de Django a partir del código? Ten en cuenta que hay que configurar la base de datos, crear las migraciones, lanzarlas, etc.

## Desplegar e iniciar proyecto de Django
1. Crea un *Virtual Environment* justo en la carpeta donde encuentras el directorio raíz del proyecto de Django ejecuta: `python -m venv venv`
2. Actívalo e instala las dependencias (este comando funciona en GNU/Linux y MacOS pero es fácil transformarlo para que funcione en la *Power Shell* de Windows): `. venv/bin/activate && pip install -r requirements.txt`
3. Entra en la carpeta raíz del proyecto llamada `dwes` en este caso
3. Crea las migraciones: `python manage.py makemigrations`
4. Lanza dichas migraciones: `python manage.py migrate`
5. Arranca el servidor de desarrollo y prueba que todo funciona: `python manage.py runserver`

# Recursos estáticos (static)
Los sitios web suelen incluir contenido estático como son:

- Imágenes
- Vídeos
- Estilos CSS
- Scripts JavaScript

En los HTML podemos incrustar este contenido estático a través de las etiquetas `img`, `video`, `script` o `link`. Cada vez que el cliente recibe un HTML, a su vez, tiene que recibir esos contenidos estáticos para poder renderizar correctamente dicho HTML.

En este Ninja Training vamos a ver cómo gestionar el contenido estático modificando el anterior para añadir **Bootstrap**.

En los siguientes puntos te explico cómo hacerlo.

## Preparando carpeta static
En la raíz del proyecto crea una carpeta llamada **static** (recuerda: la raíz del proyecto es la carpeta donde está el fichero `manage.py`).

Abre el fichero `dwes/settings.py` y busca la línea en la que aparece `STATIC 'static/'`. Debajo tienes que añadir:

``` python
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

que configura la carpeta `static` que acabamos de crear en la raíz del proyecto como la carpeta que contendrá los recursos estáticos.

## Descarga Bootstrap
Descarga Bootstrap desde su [página web]('https://getbootstrap.com/docs/5.3/getting-started/download/').

Añade las carpetas `css/` y `js/` dentro de la carpeta `static/` que creaste en el apartado anterior.

# Añade Bootstrap a tus páginas web HTML
Para añadir en tus HTML Bootstrap tienes que cargar, en primer lugar, la etiqueta `static` de Jinja. En la primera línea de tus HTML añade:

``` html
{% load static %}
```

Ahora ya puedes añadir, dentro del head, Bootstrap (tanto el CSS como JS). Aquí tienes un ejemplo:

``` html
{% load static %}
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
  </head>
  <body>
	...
  </body>
</html>

```

Aquí, la etiqueta `{% static %}` hace alusión a la carpeta `static` que hemos creado anteriormente.

En el `body` ya puedes usar Bootstrap. Hazlo para las páginas `detail.html` y `list.html` de `memora`.
