# Antes de empezar: MUY IMPORTANTE
He añadido en el fichero `requirements.txt` la dependencia/librerías de Python `Pillow` que es una librería para imágenes para Python. Django la necesita si usas el *field* `ImageField` como va a ser el caso en este Ninja Training.

# Descripción
En este Ninja Training tienes que añadir una mejora en la apliación **Memora**: añadir la posibilidad (opcional) de acompañar con una imagen las notas o recordatorios que creamos.

> Te recomiendo la lectura de [esta parte de la documentación oficial de Django](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#handling-uploaded-files-with-a-model) en la que se describe cómo manejar ficheros a través de los `ModelForm`.

¿Qué pasos tendrás que dar?

1. Añadir al modelo `Note` un nuevo **campo opcional** llamado `image` del tipo `ImageField` (que es una clase derivada de `FileField` pero que valida que el fichero sea una imagen).

2. Lee, en la documentación oficial, [cómo usar el campo FileField](https://docs.djangoproject.com/en/5.0/ref/models/fields/#filefield) porque vas a ver que tienes la posibilidad de indicar dónde se guardará el fichero que se sube cuando se haga el `save` del `ModelForm`, para hacer que la imagen se suba a la carpeta `MEDIA_ROOT/notes/user_<id>/<filename>`.

3. Crear migración y lanzarla.

4. Añadir en el `ModelForm` (fichero `forms.py`) el campo `image` para que se renderice en el template.

5. Modificar el template con el formulario para crear notas porque necesitas añadir el atributo `enctype` con el valor `multipart/form-data` a la etiqueta `form`.

6. Modificar el template del detalle de las notas para mostrar la imagen que acompaña dicha nota si la hubiera. Para obtener la URL de la imagen y poder incluirla en la etiqueta *anchor element* de HTML (`a`). La URL de los `ImageField` o `FileField` está en el atributo `url` de dicho objeto: `<img src="{{ note.image.url }}">`.

7. Por último, pero muy importante, en la vista para añadir/editar notas tendrás que pasar al formulario, además del `request.POST`, el `request.FILES` como segundo argumento.
