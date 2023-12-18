# Puesta en marcha del proyecto - deploying
Antes de comenzar te explico cómo poner en marcha el proyecto. Vamos a usar **Docker** con tres contenedores:

- `python` en el que estará la aplicación de Python.
- `db` en el que se encuentra **MySQL** como sistema gestor de base de datos.
- `adminer` con el programa **Adminer** para facilitar el acceso a los datos.

Aquí tienes los comandos de Docker que vas a necesitar. Todos **los comandos se ejecutan en el mismo directorio** en el que está el fichero `docker-compose.yml`.

- Levanta los contenedores (la primera vez tardará un poco porque tiene que descargar las imágenes y crear los contenedores):

``` shell
$ docker compose up -d
```

- Para los contenedores:

``` shell
$ docker compose stop
```

- Si quieres comprobar que los contenedores estén en marcha, al ejecutar el comando que ves debajo, deberías ver los dos contenedores en marcha y si no fuera así es que están "apagados":

``` shell
$ docker compose ps
```

# Acceso a MySQL a través de Adminer
Para acceder a Adminer abre tu navegador web y accede a la dirección `http://localhost:9000`.

Como ves en `docker-compose.yml` hemos configurado el contenedor de Adminer para que escuche en el puerto 8080. Si lo tienes ocupado por otra aplicación lo tendrás que cambiar.

Los datos de acceso a MySQL son los que hemos puesto en el fichero de configuración `docker-compose.yml` a saber:

- Servidor: `db`
- Usuario: `dwes`
- Contraseña: `dwes`
- Base de datos: `dwesdb`

# Carga el esquema de la base de datos
La primera vez que que pongas en marcha el proyecto tendrás que crear las tablas y añadir datos de prueba si quieres. Hazlo a través de Adminer. Tienes el esquema de la base de datos en el fichero `schema.sql` que se encuentra en la raíz del proyecto.

# Ejecutar el programa
El programa en Python está dockerizado, así que cada vez que quieras ejecutar el programa tendrás que ejecutar desde el directorio donde está `docker-compose.yml` el comando siguiente:

``` shell
$ docker compose run python
```

# Descripción del Ninja Training
Tienes que completar las funciones que ves en los ficheros `deletes.py`, `inserts.py`, `selects.py` y `updates.py` para que el programa quede completo.

Si lo ejecutas verás un menú para hacer diversas operaciones sobre la base de datos. Ahora mismo no se hace nada porque las funciones de las que te hablo están vacías.

# Si acabas... puedes seguir
Cuando termines, puedes completar el programa añadiendo las siguientes opcioens (son todo `selects` así que escribe el código necesario en `selects.py`).

En el documento `SELECTS.sql` puedes ver las *selects* que tendrías que usar en estos ejemplos. No los mires si no es estrictamente necesarios, trata de obtener las *selects* por ti mismo/a, revisa la documentación de **Bases de Datos**, repasa y tómate todo el tiempo necesario para ponerte al día con **SQL**.

## Valoraciones de un usuario
Añade la opción de poder ver las valoraciones que ha hecho un usuario ordenadas de mayor a menor ranking.

Para ello, pedirás el nombre de usuario y el programa mostrará un listado del nombre de las películas y las valoraciones que ha hecho dicho usuario. Ordénalas por ranking, de menor a mayor.

NO VAYAS DIRECTO A PROGRAMAR: en su lugar, **abre Adminer** y **prueba la select** que obtendría dicha información de la base de datos. Cuando tengas clara la *select* entonces pasa a la programación.

## Ranking de las películas
Añade la posibilidad de hacer un ranking de películas, en la que se muestre el nombre de la película y la media de valoraciones.

NO VAYAS DIRECTO A PROGRAMAR: en su lugar, **abre Adminer** y **prueba la select** que obtendría dicha información de la base de datos. Cuando tengas clara la *select* entonces pasa a la programación.

## Usuario más activo
Añade la opción de poder ver al usuario más activo, el que más películas ha valorado. Si hay varios con el mismo número que salga el primero sin más.

Aquí puedes, simplemente, obtener el listado de usuarios y número de valoraciones, ordenarlos de mayor a menor y obtener el primero.

NO VAYAS DIRECTO A PROGRAMAR: en su lugar, **abre Adminer** y **prueba la select** que obtendría dicha información de la base de datos. Cuando tengas clara la *select* entonces pasa a la programación.
