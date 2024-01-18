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

# Resolución inversa de URLs
Primero: puedes leer la documentación relativa a esta parte en la [página web oficial de Django](https://docs.djangoproject.com/en/5.0/topics/http/urls/#reverse-resolution-of-urls).

Con lo visto hasta ahora podríamos poner en nuestros *templates* enlaces a nuestras rutas. Por ejemplo:

```html+django
<a href="/memora/notes/">Ver las notas y recordatorios</a>
```

Pero, como ves, hemos tenido que escribir en el `href` la ruta literalmente, lo cual no es aconsejable porque el diseño de las rutas podría variar, y si varían tenemos que recorrer todos los *templates* en busca de las rutas que hemos cambiado.

Para resolver estos inconvenientes debemos usar lo que se denomina como *Reverse Resolution of URLs*: es decir, usar los identificadores de esas rutas en vez de las rutas en sí.

En Django lo podemos usar:

- En las *plantillas* con la etiqueta `url` (`{% url ... %}`).
- En el código de Python con la función `reverse` (que puedes importar del módulo `django.urls`).
- También en el código relacionado con las URLs de Django, a través de las instancias de los modelos con el método `get_absolute_url()`.

Llegados aquí, ¿qué es el identificador de un ruta? El valor que le damos al parámetro `name` en la función `path`:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("notes/<int:note_id>/", views.detail, name="detail"),
    path("notes/create/", views.create_note, name="create_note")
]
```

Ahora sí, podemos ver el código HTML del enlace usando el identificador de la ruta en vez de la ruta:

```html+django
<a href="{% url 'notes' %}">Ver las notas y recordatorios</a>
<a href="{% url 'detail' 1 %}>Ver la nota identificada por el número 1</a>
<a href="{% url 'create_note' %}>Añadir una nueva nota</a>
```

Un ejemplo para que veas cómo hacer una redirección en un vista para que veas cómo usar la función `reverse`:

```python
from django.http import HttpResponseRedirect
from django.urls import reverse


def redirect_to_note(request, note_id):
    return HttpResponseRedirect(reverse("detail", args=(note_id,)))
```

## Nombres de espacio
Los proyectos de Django, insisto, suelen ser grandes y puede que esta manera de identificar rutas sea insuficiente y tengamos colisiones. Para evitarlo es aconsejable usar **namespaces**.

Lo primero que hay que hacer es añadir en el fichero `urls.py` de la aplicación una variable llamada `app_name` con el valor del *namespace* que consideremos (usaremos el nombre de la aplicación).

Así, en el fichero `memora.urls.py` añadiremos dicha variable:

```python
from django.urls import path

from . import views

app_name = "memora"

urlpatterns = [
	path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("notes/<int:note_id>/", views.detail, name="detail"),
    path("notes/create/", views.create_note, name="create_note")
]
```

Para terminar, en el fichero `urls.py` del proyecto, done incluimos una conjunto de rutas, con `include`, tendremos que indicar el **namespace**:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("memora/", include("memora.urls", namespace="memora")),
]
```

Y, ahora, los enlaces inversos necesitan el prefijo `memora:` como ves aquí:

```html+django
<a href="{% url 'memora:notes' %}">Ver las notas y recordatorios</a>
<a href="{% url 'memora:detail' 1 %}>Ver la nota identificada por el número 1</a>
<a href="{% url 'memora:create_note' %}>Añadir una nueva nota</a>
```

Si necesitas hacer lo propio en el código Python con `reverse`:

```python
reverse("memora:detail", args=(note_id,)
```

# Ejercicio
Incluye un menú en el *template* `base.html` de la aplicación `memora` con un enlace a la lista de recordatorios y un enlace para acceder al formulario para añadir un recordatorio nuevo.

Por último, en el listado de recordatorios, incluye un enlace al lado para poder ver los detalles.
