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
Para acceder a Adminer abre tu navegador web y accede a la dirección `http://localhost:8080`.

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
