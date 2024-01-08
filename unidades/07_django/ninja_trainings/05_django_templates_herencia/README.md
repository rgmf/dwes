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

# Reutilizando templates
Cuando usamos los templates en Django deberíamos usar una de las características más poderosas: *template inheritance*.

La idea consiste en crear un *template* genérico o base del que heredarán el resto de *templates*.

Ya te habrás dado cuenta que todos los *templates* de un sitio web tienen la misma estructura. Para no repetir código Jinja/HTML podemos crear un *template* base del que heredarán todos los demás.

## La base de los templates
Crea, dentro de `dwes/memora/templates`, un *template* llamado `base.html` como el siguiente:

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}DJourney{% endblock %}</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  <script src="{% static 'js/bootstrap.min.js' %}"></script>
</head>
<body>
  <div class="container-fluid">
    <div class="alert alert-primary" role="alert">
	  Memora
    </div>
  </div>
  <div class="container-fluid">
    {% block content %}{% endblock %}
  </div>
</body>
</html>
```

Esta va a ser la base de todos los HTML de nuestro sitio web. La novedad aquí está en la etiqueta `block` de Jinja. La idea es crear bloques en las posiciones adecuadas donde las plantillas "hijas" podrán inyectar contenido.

## Usando la base
Ahora, tu plantilla `memora/detail.html` será así:

```html
{% extends "base.html" %}

{% block content %}
<div class="container">
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Detalles de la nota</h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">{{ note.category }}</h6>
      <p class="card-text">{{ note.note }}</p>
    </div>
  </div>
</div>
{% endblock %}
```

Donde, como ves, hemos extendido de la base y hemos colocado el contenido dentro del bloque al que llamamos **content** en `base.html`.

Haz lo propio con `memora/list.html`.
