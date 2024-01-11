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

# Formularios 
En este Ninja Training vamos a añdir un formulario para poder añadir notas o recordatorios.

El núcleo del sistema de formularios en Django lo compone la clase `Form`, que se encuentra en el módulo `django.forms`. Esta clase funciona de manera parecida a la clase `Model` en la que indicaremos los campos del formulario, tipos de datos, validaciones, etc.

> Para profundizar puedes acceder a la documentación ofical de Django [sobre formularios](https://docs.djangoproject.com/en/5.0/topics/forms/).

## Crear la clase del formulario
Los formularios en Django, por tanto, van a ser clases que heredan de `Form`. Estas clases se escriben en el fichero `forms.py` de la aplicación. Dicho fichero lo tendrás que crear, si no existe, dentro de `memora`.

Esta podría ser la clase que defina nuestro formulario para añadir notas o recordatorios:

```python
from django import forms


class NoteForm(forms.Form):
    note = forms.CharField(
        label="Escribe la nota o recordatorio",
        widget=forms.Textarea(attrs={"rows": "5"})
    )
    label = forms.CharField(label="Etiqueta", max_length=20)
```

Los atributos del formulario tienen una serie de propiedades que usará Django para construir el formario HTML. Fíjate, por ejemplo, en el parámetro `widget` del `forms.CharField` que nos permite indicar a Django cómo tiene que renderizar dicho campo en el formario HTML (como un `textarea` en vez de como un `input`).

Por defecto todos los atributos son requeridos.

## Crear el template
Crea, en la carpeta `memora/templates/memora` el *template* `note_form.html`:

```html+django
{% extends "base.html" %}

{% block content %}
<form action="/memora/notes/create/" method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Añadir nota">
</form>
{% endblock %}
```

Observa varias cosas:

- Nosotros solo añadimos la etiqueta `<form>` y el `<input>` con el submit.
- Django añade los campos HTML del objeto `form`.
- En todo formulario, como primer elemento, debajo de la etiqueta `<form>`, añade siempre `{% csrf_token %}` con el que Django proporciona protección contra los ataques *Cross Site Request Forgeries* (más información [aquí](https://owasp.org/www-community/attacks/csrf#overview)).

## Añadir la ruta y la vista
En el fichero `urls.py` de la aplicación `memora` añade la ruta a `/memora/notes/create/`:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("<int:note_id>/", views.detail, name="detail"),
    path("notes/create/", views.create_note, name="create_note")
]
```

Y, por último, añade la vista `views.create_note`:

```python
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .models import Note, Category
from .forms import NoteForm


def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data["note"]
            label = form.cleaned_data["label"]
            category = Category.objects.filter(name=label).first()
            if not category:
                category = Category(name=label)
                category.save()
            note_object = Note(note=note, category=category, pub_date=timezone.now())
            note_object.save()
            return HttpResponseRedirect("/memora/notes/")
    else:
        form = NoteForm()

    return render(request, "memora/note_form.html", {"form": form})
```

Lo primero que notarás es que en esta vista se trata el formulario cuando llega una petición `POST` y se envía el formulario vacío en otro caso. Como hemos estado haciendo hasta ahora, antes de estudiar Django.

Si el formulario llega por POST y es válido añadimos lo necesario en la base de datos y redirigimos la petición a la lista de notas, por ejemplo. Si no fuera válido se vuelve a cargar el formulario y, esta vez, con la información de errores y valores de los campos (que gestiona automáticamente Django).

Por último, **y algo que es muy importante**, una vez validado el formulario puedo acceder a los valores que ha escrito el usuario a través del atributo `cleaned_data` del objeto `form`. Este atributo es un diccionario con los valores de los campos del formulario limpios y listos para ser usados.

# Ejercicio
Añade a la aplicación `memora` un formulario para poder añadir categorías.
