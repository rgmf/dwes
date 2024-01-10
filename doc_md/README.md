# Índice de contenidos
En este documento encontrarás documentación útil para el módulo de Desarrollo Web en Entorno Servidor (DWES) del Ciclo de Formación Profesional de Desarrollo de Aplicaciones Web (DAW).

Aquí no vas a encontrar el material organizado por temas sino por contenidos que puedan requerir de ciertas aclaraciones o que entrañen una especial dificultad para el alumnado.

1. [Desarrollo en el backend con Python y Gunicorn](wsgi.md)

Para el desarrollo de aplicaciones web con Python se suele usar un framework como Django o Flask. También se usa frameworks como FastAPI si lo que quieres es desarrollar servicios web. No obstante, es muy importante para un desarrollador de aplicaciones web del lado del servidor entender cómo funciona, desde abajo, un servidor.

Es por ello que en este apartado te explico los fundamentos del desarrollo web con Python empleando un *middleware* estandarizado denominado **WSGI** (también tenemos **ASGI**). El **WSGI** que vamos a usar en clase se llama **Gunicorn**.

2. [Manejo de formularios con Python y WSGI](form.md)

En este apartado encontrarás las líneas maestras y generales que hemos seguido en clase para manejar los formularios en nuestros servidores Python/WSGI.

3. [Manejo de cookies con Python y WSGI](cookies.md)

En este apartado te explico cómo manejar las cookies en nuestras aplicaciones web con Python y WSGI.

Verás cómo enviar y recibir cookies, así como manejarlas usando la clase `SimpleCookie`. También te presento la clase `Morsel`. Por último, aprenderás a codificar con `quote` y decodificar con `unquote` los valores de las cookies, para que puedas usar valores con espacios y todo tipo de caracteres.

4. [`datetime`: hoy, mañana y pasado... en Madrid, Los Ángeles o Moscú](datetime.md)

El manejo y gestión de fechas es un campo complicado pero fundamental en todo programa. Aquí te voy describir de forma muy, muy breve, cómo trabajar con fechas y zonas horarias en Python.

Te recomiendo que guardes todas tus fechas en formato ISO-8601 en UTC. Luego podrás pasar esa hora referencia a cualquier zona horaria.

5. [La (des)Orientación a Objetos en Python](poo.md)

Python es un lenguaje multiparadigma que incorpora la Programación Orientada a Objetos. Te resumo aquí lo más importante. Casi todo son fragmentos de código. Si "mareas" un poco por la Web encontrarás mejores recursos.

6. [Acceso a bases de datos desde Python](bbdd.md)

Casi todos, sino todos, los programas necesitan alguna manera de guardar permanentemente datos e información (persistencia de datos). Hay varias soluciones. Aquí te explico cómo usar bases de datos.
