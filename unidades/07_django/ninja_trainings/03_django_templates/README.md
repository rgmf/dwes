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

# Templates - Jinja2
Django es un framework para la web por lo que necesita una manera conveniente de generar documentos HTML que devolver como respuesta. Hasta ahora hemos estado usando strings de Python donde inyectábamos el contenido dinámico. Esta es la idea de los motores de plantilla pero, como verás en un instante, estos motores de plantillas son mucho más poderosos.

En Django el motor de plantillas se llama **Jinja2** y es un proyecto separado de Django y que puede ser usado independientemente de Django. [Esta](https://jinja.palletsprojects.com/en/3.1.x/) es la web oficial con toda la documentación.

**Jinja2** tiene una serie de *placeholders* donde se pueden inyectar contenido e, incluso, algunos de estos se pueden usar para construir sentencias condicionales y bucles. Te resumo algunos de los *placeholders* de Jinja2. Pero antes, si quieres puedes leer más sobre Jinja2 en estos enlaces.

- [Documentación oficial de Django sobre templates](https://docs.djangoproject.com/en/5.0/topics/templates/)
- [En la propia página web de Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)

## Antes de empezar con la sintaxis de las plantillas
Como hemos hecho hata ahora con nuestro pequeño motor de plantillas, las plantillas de Django son documentos HTML donde se incluyen *placeholders*. Luego, desde nuestras vistas tendrás que cargar estas plantillas pasándole en un contexto toda la información requerida.

Los ficheros con estos *templates* tienen la misma extensión que los documentos HTML, es decir, `*.html`.

En los siguienes apartados te resumo algunos *placeholders* (sacados de la misma página web de Django).

## Proyectar valores de variables

``` html+django
My first name is {{ first_name }}. My last name is {{ last_name }}.

```

A esta plantilla le tendrás que pasar un contexto como este:

``` python
{"first_name": "John", "last_name": "Doe"}
```

## Estructura condicional

``` html+django
{% if user.is_authenticated %}
    Hello, {{ user.username }}.
{% endif %}
```

Para que esta plantilla se pueda renderizar se necesita un objeto llamado `user`. Algo así:

``` python
{"user": User.objects.first()}
```

Aquí, una cadena de `if-elif-...-else` completa:

``` html+django
{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny!  You bastard!!!
{% else %}
    Kenny looks okay --- so far
{% endif %}
```

## Bucles

``` html+django
<ul>
{% for user in users %}
    <li>{{ user.username }}</li>
{% endfor %}
</ul>
```

En el ejemplo de arriba puedes ver cómo construir una lista con el nombre de los usuarios.

Podríamos comprobar antes si hay o no usuarios:

``` html+django
{% if users %}
    <ul>
    {% for user in users %}
        <li>{{ user.username }}</li>
    {% endfor %}
    </ul>
{% else %}
    <li>No hay usuarios</li>
{% endif %}
```

O, aún mejor, el bucle for tiene una parte opcional llamada `empty` con el que podemos lograr lo mismo que antes pero de forma más elegante:

``` html+django
<ul>
{% for user in users %}
    <li>{{ user.username }}</li>
{% empty %}
    <li>No hay usuarios</li>
{% endfor %}
</ul>
```

## Filtros
Una de las opciones más usadas con las plantillas Jinja2 es la de poder usar filtros que modifican la forma en que se mostrará el valor de la variable u objetos dado.

Existen muchos filtros predefinidos que se pueden usar en Django y que pueden ser [consultados aquí](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#ref-templates-builtins-filters).

Un ejemplo simple. Imagina que inyectamos una lista con colores como esta: `{colors: ["red", "blue", "yellow"]}`. Puedes mostrar el primer color así:

``` html+django
{{ colors|first }}
```

Lo que viene a continuación del carácter `|` es el llamado filtro, que no es más que una función de Python que actúa sobre la variable que hay delante del carácter `|`.

Otro ejemplo podría ser el del filtro `last` que devuelve el último elemento:

``` html+django
{{ colors|last }}
```

O este otro filtro `length` que devuelve el número de elementos:

``` html+django
{{ colors|length }}
```

# Ninja Training: a trabajar
En este Ninja Training te propongo que construyas los *templates* para las dos vistas:

- La vista que muestra el detalle de una nota.
- La vista que muestra la lista de notas.

Las plantillas son ficheros HTML con *placeholders* de Jinja2 para poder inyectar contenido dinámico. Estos ficheros, en un proyecto de Django, se tienen que crear dentro de la aplicación, en una carpeta llamada `templates`. Así que, crea los ficheros dentro de `memora` como ves aquí:

``` shell
memora
 |
 |__ templates
      |
	  |__ memora
	       |
		   |__ detail.html
		   |
		   |__ list.html
```

Para renderizar y enviar el HTML usa en tus vistas (`views.py`) la función `render` de Django como ves en este ejemplo:

``` python
from django.shortcuts import render

from .models import Question


def index(request):
    question_list = Question.objects.order_by("-pub_date")
    context = {"question_list": question_list}
    return render(request, "polls/index.html", context)
```

La función `render` recibe, como ves:

- El objeto **request**
- La plantilla: se pone la ruta relativa desde la carpeta `templates` (en nuestro caso será `"memora/detail.html"` y `"memora/list.html"`)
- El contexto: un diccionario en el que inyectamos lo que necesita la plantilla (como hemos estado haciendo hasta ahora)
