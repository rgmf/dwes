# Subir ficheros en Django
Todo lo que vamos a comentar y hacer en este Ninja Trainin lo puedes encontrar, como siempre, en la [página web oficial de Django](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/).

Dicho esto, te resumo lo más importante.

## El formulario HTML y el proceso de subida
Antes de entrar de lleno en cómo subir los ficheros en el caso concreto de Django conviene que sepas cómo se suben ficheros a través del protocolo HTTP/HTTPS usando formularios HTML. Los pasos son los siguientes:

1. El formulario HTML tiene que incluir el atributo `enctype` con el valor `multipart/form-data`. Si no lo indicas, los ficheros del formulario no se enviarán en el *request*.

``` html
<form method="post" enctype="multipart/form-data">
	<!-- Campos del formulario -->
</form>

```

2. Dentro del formulario añade un `input` de tipo `file` que es el campo a través del cual incluir un fichero.

``` html
<form method="post" enctype="multipart/form-data">
	<!-- Campos del formulario -->
	
	<input type="file" name="avatar">
</form>

```

3. Al enviar el formulario se manda, en el *request*, el fichero indicado. El servidor web tomará este fichero y lo guardará en algún sitio de forma temporal (en memoria o disco).

4. Nuestro programa del servidor tendrá que copiar dicho fichero en algún sitio de la jerarquía de directorios de nuestro propio programa en el servidor.

## Configurar Django
De la misma manera que tenemos una carpeta para el almacenamiento de los recursos estáticos (los JavaScript, los CSS, etc), ahora necesitaremos un lugar donde almacenar todos los ficheros que permitamos a los usuarios subir al servidor (como las imágenes).

Esto último se suele hacer en una carpeta que se llama `media` y que se deja en la raíz del proyecto.

Lo llames como lo llames tendrás que indicarle a Django dónde van a estar y esto se hace añadiendo dos constantes en el fichero `settings.py` del proyecto. Por ejemplo:

``` python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "uploads"
```

Como en el caso de los recursos estáticos indicamos la URL y la carpeta de los *media* (ficheros).

## Para poder servidor los media...
... tendrás que configurar rutas para los mismos.

Para el entorno de desarrollo bastaría con poner al final del fichero `urls.py` del proyecto estas líneas:

``` python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> Fíjate que lo que hacemos es añadir nuevas URLs a `urlpatterns` pero solo si tenemos el *flag* `DEBUG` a True o, dicho de otro modo, estamos en la etapa de desarrollo. Si desplegamos dicha aplicación en produccion, entonces tendríamos que configurar los recurso estáticos y los media pero esto se escapa de los objetivos de este módulo.

FIN: ya tenemos Django listo para poder trabajar con los ficheros que subamos.

## Manejar formularios con ficheros
Por no escribir lo que ya está escrito te sugiero, nuevamente, que leas la documentación oficial de Django a este respecto.

Lo único que voy subrayar es que, de la misma manera que los formularios los recibimos, en las vistas de Django, en el objeto `request` (en concreto en `request.POST`), los ficheros que subimos están en `request.FILES`. Y, si quieres considerar estos ficheros tendrás que pasarle, como segundo argumento, esto último a los formularios:

``` python
form = ExampleForm(request.POST, request.FILES)
```

Y, una vez valides el formulario, tendrás el objeto fichero en `request.FILES["file_name"]` donde `file_name` será el valor del `name` del formulario (que se corresponde con el nombre del campo del formulario `ExampleForm`).

### Mover los ficheros subidos a la carpeta media
Esta parte siempre va a ser igual y consiste en mover los ficheros subidos al servidor a nuestra capeta `medias` configurada en `settings.py`:

> Es un ejemplo. Si lo entiendes lo podrás adaptar/modificar según los requerimientos.

``` python
from os.path import join

from django.conf import settings


def handle_upload_file(name, f):
    extension = f.name.split(".")[-1]
    name_and_ext = name + "." + extension

    image_folder = join(settings.MEDIA_ROOT, "img")

    complete_path = join(image_folder, name_and_ext)

    with open(complete_path, "wb+") as fd:
        for chunk in f.chunks():
            fd.write(chunk)
```
