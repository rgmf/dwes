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

# Detalle y eliminación de notas
Llegados a este Ninja Training tienes un listado de notas o recordatorios.

Añade, enlaces, junto a cada una de estas notas, para poder ir al detalle de cada nota y otro para borrarlo.

La vista para el detalle ya está hecho. Sin embargo, la vista para borrar una nota está sin hacer. Así pues, tendrás que:

- Diseñar/elegir una URL para el borrado de una nota que deberá incluir un *path parameter* con el identificador de la ruta a eliminar.
- Crear una vista para eliminar la nota (en el fichero `views.py`). La vista que elimina una nota podrá redirigir al usuario al listado de notas cuando se borre correctamente.

Recuerda que, si una **URL**, require de un *path parameter* entonces tendrás que indicar el valor en la etiqueta `url` de jinja: `{% url 'memora:detail' note.id %}`, por ejemplo. Si quieres resolver dicha ruta desde Python con la función `reverse`, entonces tendrás que indicar la URL y, además, pasar al parámetro `args` los parámetros necesarios: `reverse("memora:detail", args=(note.id,))`.

# Editar notas
Por último, faltaría la posibilida de editar notas.

Crea/diseña una URL para la edición de notas. En este caso:

- Vamos a necesitar el identificador de la nota.
- En la vista que tienes que crear (dentro de `views.py`) tendrás que obtener la nota y renderizar el formulario que creamos para añadir notas con los datos de dicha nota.
- Cuando llegue el formulario y sea válido tendrás que modificar la nota y no crear una nueva. Para ello: obtén la nota, modifica sus valores y usa el método `save`.

## ¿Cómo crear un formiulario para añadir y editar modelos en Django?
El formulario HTML/Jinja tendrías este aspecto:

``` html+django
<form action="{{ action }}" method="post">
  {% csrf_token %}
  {{ form }}
  <input type="submit" value="Enviar">
</form>
```

Como ves se usan dos *placeholders* de Jinja:

- `action`: URL al que se envía el formulario. Puede ser enviado a la ruta para añadir o a la ruta para editar, según el caso.
- `form`: el formulario en sí.

Imagina que tienes un modelo llamado `Dog` y un formulario `DogForm`. Aquí tienes la vista para añadir *dogs*:

``` python
def create(request).
    if request.method == "POST":
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("main:create_dog"))
    else:
        form = DogForm()

    return render(
        request,
        "main/dog_form.html",
        {"form": form, "action": reverse("main:create_dog")}
    )
```

Hasta aquí nada nuevo que no hayamos visto en clase. Ahora bien, podemos usar el midmo formulario para editar *dogs* pero cuando enviemos por primera vez el formulario tendremos que inicializarlo con los datos del *Dog* a editar y para ello se usa el parámetro `instance` de los `Form` o `ModelForm` de Django:

``` python
def edit(request, dog_id):
    try:
        dog = Dog.objects.get(id=dog_id)
    except Dog.DoesNotExist:
        raise Http404("El dog no existe")

    if request.method == "POST":
        form = DogForm(request.POST, instance=dog)
        if form.is_valid():
            form.save()
            return redirect(reverse("main:dogs"))
    else:
        form = DogForm(instance=dog)

    return render(
        request,
        "memora/dog_form.html",
        {"form": form, "action": reverse("main:edit_dog", args=(dog_id,))}
    )
```

## Un shortcut bastante útil
Llegados aquí habrás visto este código muchas veces (siguiendo con el ejemplo del modelo `Dog`):

``` python
try:
    dog = Dog.objects.get(id=dog_id)
except Dog.DoesNotExist:
    raise Http404("El dog no existe")
```

Básicamente, tratamos de obtener un objeto de un modelo y si no existe se lanza una excepción y enviamos al usuario a la página **404**.

Puedes usar el shortcut `get_object_or_404()` que hace eso mismo pero en una línea de código:

``` python
dog = get_object_or_404(Dog, id=dog_id)
```
