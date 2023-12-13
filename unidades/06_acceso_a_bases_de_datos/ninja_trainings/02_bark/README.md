# Primero lo divertido: Docker
Todo los comandos que se indican en estos subapartados se tienen que realizar en la misma carpeta donde está el fichero `docker-compose.yml`.

## Información básica de los contenedores
En esta práctica tenemos tres contenedores:

- `python` donde tenemos **Gunicorn** ejecutando nuestra aplicación **Python**.
- `db` donde tenemos a **MariaDB**, la base de datos.
- `adminer` donde tenemos la aplicación o GUI para la gestión de la base de datos **MariaDB**.

Cuando los contenedores estén levantados puedes acceder a la aplicación y a Adminer:

- La aplicación/servidor de **Gunicorn** está escuahando en la dirección `localhost:8888`.
- Si quieres gestionar o ver la base de datos, **Adminer** está escuchando en la dirección `localhost:9000`.

## Levantarlos
Arranca los contenedores, levántalos, con la siguiente orden:

``` shell
$ docker compose up -d
```

## Pararlos
Con la orden:

``` shell
$ docker compose stop
```

## Reiniciarlos
Con la orden:

``` shell
$ docker compose restart
```

## Ver los logs
Vas a necesitar ver los logs de la aplicación de **Gunicorn** cuando estés desarrollando porque es ahí donde verás los errores que has cometido los `print` que metas en tu código para depurar "cosas". Te recomiendo que tengas siempre abierto una terminal (¡ES LA MEJOR APLICACIÓN QUE SE HA INVENTADO! :heart_eyes:) y ejecutes en ella la siguiente orden:

``` shell
$ docker compose logs python --follow
```

El `--follow` es para mantener los logs en vivo.

## Ver el estado de los contenedores
¿Estás intentando acceder a `localhost:8888` o `localhost:9000` y no aparece nada? ¡Qué no cunda el pánico!

Comprueba que los contenedores estén levantados (tienen que aparecer tres):

``` shell
$ docker compose ps
```

¿No aparece nada? Tu fiel compañero son los... **logs**. Arriba te explico cómo ver los logs para el contenedor **python**.

## Apaga las luces
En realidad tendrás instalado en tu equipo (seguramente) **Docker Desktop**, sobre todo si usas Windows.

Desde ahí,

si indigas un poco,

(yo no lo voy a hacer,

prefiero la terminal)

podrás hacer todo lo que te he comentado en los pasos anteriores,

digo yo,

que no lo sé.

# Descripción del Ninja Training
En este Ninja Training tienes que completar la aplicación web con la parte de accesso a la base de datos. La práctica te sonará: la hicimos usando *Cookies*, un follón. Por fin hemos llegado a **bases de datos** para hacerla bien.

Además, vamos a añadir la posibilidad de dar *likes* a *los ladridos*.
