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

# Sistema de autenticación de Django
Antes de comenzar, toda la documentación sobre la autenticación en Django la puedes encontrar [en la página web oficial de Django](https://docs.djangoproject.com/en/5.0/topics/auth/).

Cuando creamos un proyecto de Django, este viene con el sistema de autenticación por defecto del propio Django. Verás que, entre las aplicaciones instaladas, tenemos estas tres:

- `django.contrib.auth`
- `django.contrib.contenttypes`
- `django.contrib.sessions`

Y cuando lanzaste las migraciones se crearon tablas en la base de datos, entre las que tenemos una tabla de usuarios, cuyo modelo es `User` que encontrarás en el módulo de Django `django.contrib.auth.models`. Los principales atributos de este modelo son:

- `username`
- `password`
- `email`
- `first_name`
- `last_name`

Que, en la mayoría de los casos, será suficiente.

> Puedes personalizar este modelo pero, como digo, en la mayoría de los casos no será necesario.

## Autenticación en peticiones web (web requests)
Django usa sesiones para la autenticación de los usuarios.

Básicamente, el objeto `request`, que reciben todos los `views`, tiene un atributo llamado `user` que representa el usuario actual. Aquí podemos encontrarnos en dos escenarios posibles:

- El usuario actual, el que ha hecho el request, no está *logeado*. En este caso `request.user` será una intancia de `AnonymousUser`.
- En otro caso (SÍ está logeado) `request.user` será una instancia de la clase `User`.

En tus vistas podrás comprobar si un usario está logeado tal que así:

``` python
if request.user.is_authenticated:
    # Sí está autenticado: logeado
    pass
else:
    # No está autenticado: no sabemos quién es
    pass
```

En las plantillas, Django inyecta por ti el objeto `user`. Por tanto, puedes comprobar si el usuario está o no logedo para mostrar unas cosas u otras en los *templates*:

``` html+django
{% if user.is_authenticated %}
    <p>Estás logeado. Tu nombre de usaurio es {{ user.username }}</p>
{% else %}
    <p>No estás logeado</p>
{% endif %}
```

## Necesidades mínimas para añadir autenticación a nuestros sitios web
Entendido el sistema de autentiación de Django, pasamos a implementar lo necesario para tener un sistema de autenticación en Django:

- Un sistema de registro: formulario para que un usuario se pueda registrar: signup.
- Un formulario de acceso: login.
- La posibilidad de cerrar sesión: logout.
 
Te sugiero que crees un aplicación para la gestión de la autenticación. Yo la voy a llamar `accounts`.

``` shell
python manage.py startapp accounts
```

Añádela al `settings.py` de tu proyecto. ¿No recuerdas cómo hacerlo? Normal: ves al primer Ninja Training.

Una vez añadida tu aplicación nueva. Incluye las rutas de la nueva aplicación al fichero `urls.py` del proyecto. Por ejemplo:

``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts"))
    # ...
]

```

Ya podemos ir completando la aplicación `accounts`.

### Registro
Crea en la aplicación `accounts` el fichero `urls.py` para añadir tus rutas. De momento una ruta para el registro:

``` python
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
]
```

Ahora tendrás que crear un formulario que gestionarás en la vista `views.user_signup`. Esto supone:

- Crear la vista `user_signup` para la gestión del formulario.
- Crear el formulario que podemos llamar `SignupForm`.
- Crear el template con el formulario HTML.

Lo que se hace en el registro es, básicamente, **añadir usuarios a la base de datos**.

### Login
Añade la ruta para el login al fichero `views.py`. Por ejemplo:

``` python
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
]
```

Tienes que hacer lo mismo que antes:

- Crear la la vista `user_login`.
- Crear el formulario que podríamos llamar `LoginForm`.
- Crear el template con el formulario HTML.

Pero, ahora, tienes que autenticar al usuario en la vista, llamando a la función `authenticate` del módulo de Django `django.contrib.auth` que recibe:

- El `request`.
- El `username`.
- El `password`.

Por último, ten en cuenta que si el usuario no se puede autenticar habrá que mostrar un mensaje en la página del formulario. Por ese motivo, verás en la vista cómo paso un `message`.

Te dejo aquí la vista:

``` python
def user_login(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse("main:index"))
            else:
                message = "Nombre y/o contraseña no válidos"

    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form, "message": message})
```

Como ves, la función `authenticate` devolverá el usuario si dicho usuario existe en la base de datos.

Si existe entonces lo podemos *logear* en el sistema llamando a la función `login` del mismo módulo de Django `django.contrib.auth`.

La función `login` recibe:

- El objeto `request`.
- El objeto `user`.

### Logout
Por último, necesitamos una vista que cierre la sesión del usuario.

Basta con añadir un ruta, que llame a una vista y, en dicha vista, se llame la función `logout` del módulo de Django `django.contrib.auth`.

Aquí tienes las rutas de `accounts` completadas:

``` python
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout")
]

```

Y la vista `user_logout`:

``` python
def user_logout(request):
    logout(request)
    return render(request, "accounts/logout.html")
```

Por útlimo, solo falta añadir la plantilla `logout.html` que podría ser tan simple como esta (te muestro lo mínimo):

``` html+django
<p class="alert alert-info">Has cerrado tu sesión... ¡hasta pronto!</p>
<a href="{% url 'memora:index' %}">Volver</a>
```

## Proteger vistas o vistas privadas
Cuando creas un sistema de autenticación es porque quieres proteger diferentes vistas de manera que solo los usuarios logeados puedan acceder a ellas.

Por ejemplo, vamos a imagina que queremos proteger la vista que permite añadir notas o recordatorios. Hay varias formas de hacerlo. Yo te voy a enseñar una: el decorador de Django `login_required` del modulo de Django `django.contrib.auth.decorators`. En la vista `create_note` de la aplicación `memora`:

``` python
from django.contrib.auth.decorators import login_required


@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.pub_date = timezone.now()
            note.save()
            return redirect(reverse("memora:notes"))
    else:
        form = NoteForm()

    return render(
        request,
        "memora/note_form.html",
        {"form": form, "action": reverse("memora:create_note")}
    )

```

Ahora, cuando no estés logeado, sin intentas acceder a esta vista, Djagno te redirigirá automáticamente a la página de login.

> Django espera el login en la ruta **/accounts/login**, de ahí que hayamos elegido esta ruta, para que Djagno pueda hacer *su magia*

> Por cierto, la vista del **logout debería estar protegida**.

## Completar plantillas
Faltan dos detalles relativos a las plantillas:

1. No tiene sentido que el usuario pueda ver los enlaces a rutas privadas. Ocúltalas usando el objeto `user` disponible en todos los **templates**.

2. Añade al menú las opciones de registro, login y logout, según el caso (si está o no logeado el usuario).
