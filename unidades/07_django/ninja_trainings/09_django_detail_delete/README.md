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
- En la vista que tienes que crear (dentro de `views.py`) tendraś que obtener la nota y renderizar el formulario que creamos para añadir notas con los datos de dicha nota.
- Cuando llegue el formulario y sea válido tendrás que modificar la nota y no crear una nueva. Para ello: obtén la nota, modifica sus valores y usa el método `save`.
