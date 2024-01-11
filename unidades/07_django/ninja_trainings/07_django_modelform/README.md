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

# Crear formularios desde los modelos: ModelForm
Si tienes formularios que se pueden mapear o están muy cerca de los modelos puedes usar en vez de un `Form` de Django, como hemos visto en el ninja training anterior, un `ModelForm`. Esta última opción te evitará duplicidades en el código: tener que definir los campos en el modelo y en el formulario.

## ModelForm para el formulario de notas o recordatorios
Este sería el `ModelForm` para nuestro fomulario:

``` python
from django.forms import ModelForm

from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["note", "category"]
```

En este caso, el `ModelForm` usará para los campos indicados un tipo u otro en función de lo que tengamos en el modelo.

En este caso:

- `note` será un `input` de tipo `text`.
- `category` será un `select` porque es un `ForeignKey` en el modelo.

Puedes modificar el `widget` por defecto.

Si quieres o necesitas más información acude a la [documentación oficial](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/).

## Ajustar los modelos
Con lo hecho hasta ahora ya puedes ver tu formulario. No obstante hay dos cosas molestas:

- Las etiquetas de los campos del formulario.
- Los valores del `select`.

Para resulver el primer punto y usar etiquetas personalizadas tienes que hacer uso del parámetro `verbose_name` de los modelos. Para que aparezcan en el select el valor del `name` del `Category` en vez de la referencia del objeto tendrás que sobreescribir el *dunder method* `__str__`. Aquí tienes el código de los modelos actualizado:

``` python
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

	def __str__(self):
        return self.name


class Note(models.Model):
    note = models.TextField(verbose_name="Nota o recordatorio")
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)
```

Ahora las etiquetas del formulario son las indicadas en el `verbose_name`.

## Modificar el view
Cuando usamos un `ModelForm` lo que hay que hacer en el *view* es muy fácil. LLamar al método `save` del objeto `ModelForm`:

``` python
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/memora/notes/")
    else:
        form = NoteForm()

    return render(request, "memora/note_form.html", {"form": form})
```

Pero, en este caso concreto, nos encontraríamos con un error porque falta el atribut `pub_date` que es obligatorio. Si tenemos que añadir valores a mano, entonces tenemos que guardar sin *commitear*, modificar el objeto añadiendo los atributos que falten y, entonces, guardar el objeto definitivamente.

Este sí es el código definitivo del `view`:

``` python
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.pub_date = timezone.now()
            note.save()
            return HttpResponseRedirect("/memora/notes/")
    else:
        form = NoteForm()

    return render(request, "memora/note_form.html", {"form": form})
```

# Ejercicio
Añade un `ModelForm` para poder crear categorías.
