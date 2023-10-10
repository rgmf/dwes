# Importante
ESTE ES UN EJERCICIO PENSADO PARA HACERLO TODOS JUNTOS EN CLASE: CON EL ACOMPAÑAMIENTO DEL PROFESOR.

# Antes de comenzar
En este Ninja Training vas a desarrollar y "cacharrear" con un sitio web. Aprenderás y entenderás cómo se acceden a los recursos de un sitio web así como a programar páginas dinámica y cómo funcionan las páginas dinámicas.

También verás de forma práctica toda la teoría que hemos visto en clase sobre el modelo cliente servidor de la web y, sobre todo, el funcionamiento práctico del protocolo HTTP.

Dentro de la carpeta `web` está el sitio web del que te hablo, preparado para ser desplegado y probado con **Docker**. Para arrancar los contenedores de **Docker** basta con que ejecutes el comando `docker compose up -d` desde la carpeta `web`. Para detener los contenedores, también desde la carpeta `web`, tan solo tienes que ejecutar el comando **docker compose stop**.

Para poder trabajar con **Docker** necesitas tenerlo instalado junto a **docker compose**.

Sigue los pasos que te propongo a continuación.

# Hola Web... Hola HTTP... Hola cliente... Hola servidor
Arranca los contenedores y accede por medio del navegador web al sitio web: [http://localhost:8080](http://localhost:8080). Lo que estás viendo es el fichero `index.html` que está dentro de la carpeta `src`.

Así funciona la web: desde un cliente pides un recurso indicando su URL y el método (en este caso `GET`) y, el servidor, responde con una respuesta donde está incluido el recurso que, en este caso, es la página web `index.html`.

# Inspeccionando lo que está pasando
Usa **cURL** para hacer la misma petición del paso anterior:

``` shell
$ curl -v http://localhost:8080
```

Observa la petición y la respuesta.

# Más recursos en el sitio web
Crea una carpeta llamada `lenguajes` y dentro dos más llamadas `es` y `en`. Crea dos páginas web dentro de `es` y `en`. ¿Cómo accederías a dichas páginas web desde el navegador web?

# Query parameters
Pasa parámetros (arbitrarios) en las URL al pedir los recursos. ¿Qué sucede?

# PHP: un lenguaje más (lo que faltaba)
Los ficheros de **PHP** usan extensión `.php`. Estos son ficheros interpretados por el servidor web (**nginx** en este caso). Estos *scripts* tienen que devolver un "valor" que es el que va a recoger el servidor web para mandarlo en el cuerpo de la respusta o **response**.

Crea un fichero **PHP** en la raíz del sitio web llamado `hola.php` con el siguinete contenido:

``` php
<?php
echo "Hola Mundo";
```

Se acabó: guárdalo y solicita el recurso al servidor vía navegador web para que veas lo que pasa.

Lo que ha sucedido es:

1. El servidor web recibe la petición o **request**
2. Ejecuta el script
3. Recoge la salida
4. Devuelve en el **response** la salida del script como contenido de la respuesta

# Query parameters: esta vez sí que sí
Para tratar y manejar los **query parameters** lo tenemos que hacer desde un lenguaje como **PHP** o **Python**.

Veamos cómo se manejan los **query parameters** desde el servidor. Esto depende del lenguaje y tecnología usada. Te lo explico en PHP (pero no te hagas ilusciones, más adelante veremos cómo se hace en Python).

Aquí tienes un ejemplo de cómo obtener un parámetro llamado `name` y cómo usarlo para mostrar el valor de dicho parámetro en la web (va a ser TU PRIMER SITIO DINÁMICO):

``` php
<?php
$nameValue = $_GET["name"];

echo "Hola $nameValue";
```

Lo que hace **nginx** (que es el servidor web que estamos usando en el contenedor de **Docker**) es recibir la petición y pasarle al *script* de **PHP** los parámetros en un **array** llamado `$_GET`.

# Vale... pues podemos hacer algún programilla con PHP
Vamos a escribir una página en **PHP** que muestre la suma de dos **query parameters**.

# Hace muchos años... HTML en scripts de PHP
Volviendo a aquellos maravillosos años, vamos a ver ahora cómo crear páginas web dinámicas mezclando HTML y PHP.

(No, he mentido, no eran tan maravillosos aquellos años... o sí).
