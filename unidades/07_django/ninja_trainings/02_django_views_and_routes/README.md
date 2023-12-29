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

# Vistas y Rutas
Vamos a añadir nuevas vistas y, por tanto, nuevas rutas.

Como ya sabes, las rutas a la aplicación **memora** empiezan por `/memora/`. A partir de ahí, vamos a crear vistas para estas rutas:

- `/memora/` nos llevará a la vista `views.index` que vamos a llamar **index** y que muestra la página principal de la aplicación.
- `/memora/notes/` esta ruta nos llevará a la vista `views.notes` que vamos a llamar **notes** y que mostrará el listado de todas las notas.
- `/memora/<int>/` esta ruta nos llevará a la vista `views.detail` que vamos a llamar **detail** y que mostrará la nota identificada por el número indicado en la ruta.

A continuación te muestro cómo debería quedar el fichero `memora/urls.py`:

``` python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/notes/", views.notes, name="notes"),
    path("<int:note_id>/", views.detail, name="detail")
]
```

La función `path` de Django recibe dos parámetros obligatorios (el tercero es opcional):
- Primer parámetro es un string que corresponde con la ruta
- Segundo parámetro es la función que Djagno llamará cuando se solicite la ruta (nuestras funciones están en el módulo `view`)
- Tercer parámetro es un nombre que se le da a esa ruta (más adelante entenderás por qué es útil y siempre debemos dar un nombre a cada ruta)

Aquí tienes las vistas `memora/views.py` (como ves cada vista es una función):

``` python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola Mundo! Estás en Memora, la aplicación definitiva.")


def notes(request):
    return HttpResponse("Estás viendo la lista de notas")


def detail(request, note_id):
    response = f"Estás viendo la nota con id: {note_id}"
    return HttpResponse(response)
```

Hagamos aquí una parada para analizar la relación entre rutas y vistas:

- **El nombre de las funciones** en la vista se corresponde con **el nombre que le damos en el fichero de rutas**
- Cuando en la ruta hay datos (indicado entre paréntesis angulares) las funciones en la **vista reciben esos datos en los parámetros** cuyos nombre coinciden con los indicados en las rutas

# De vuelta con los modelos
Las vistas que hemos creado son estúpidas porque no muestran más que textos.

El `index` de momento lo dejamos como está. Pero vamos a completar las vistas `notes` y `detail` para mostrar lo que realmente deberíamos mostrar.

Aquí tienes la función `notes`:

``` python
def notes(request):
    html = """
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Listado de notas</h1>
        <ul>
            {ul_list}
        </ul>
    </body>
    </html>
    """

    notes = Note.objects.all()
    note_list_html = ""
    if notes:
        for note in notes:
            note_list_html += "<li>" + note.note + "</li>"
    else:
        note_list_html = "No hay notas"

    return HttpResponse(html.format(ul_list=note_list_html))
```

Y aquí la función `detail`. Verás en este código una novedad: si no existe el objeto solicitado en la base de datos debemos lanzar un error 404 y, aquí, puedes ver cómo se hace tal cosa en Django (tendrás que importar `Http404` del módulo de Django `django.http`).

``` python
def detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")

    html = """
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Detalles de la nota</h1>
        <p>{note}</p>
        <small>{category></small>
    </body>
    </html>
    """
    return HttpResponse(html.format(note=note.note, category=note.category.name))
```

Para probar estas vistas puedes ir al Ninja Training anterior y ver cómo se puede entrar a la **Shell de Django** e insertar datos de prueba en la base de datos.
