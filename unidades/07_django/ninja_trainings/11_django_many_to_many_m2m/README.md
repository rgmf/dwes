# Manejo de relaciones muchos-a-muchos (m2m)
Vamos a comenzar un proyecto nuevo de Django en el que vamos a aprender a manejar relaciones entre los modelos **muchos-a-muchos** o **many-to-many** (**m2m**).

> [Aquí](https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_many/) encontrarás más información sobre las relaciones muchos-a-muchos en Django.

> También te resultará útil saber cómo [manejar el modelo intermedio](https://docs.djangoproject.com/en/5.0/topics/db/models/#intermediary-manytomany) en relaciones muchos-a-muchos.

## Descripción del proyecto
Vamos a construir un proyecto de Django llamado `dwes_m2m` con una aplicación a la que vamos a llamar `enrollment`.

En dicha aplicación vamos a tener alumnado de los que conocemos su nombre, apellidos y edad.

Este alumnado podrá matricularse a una serie de materias de las que conocemos el nombre de la materia y una descripción.

Cuando se matricula alumnado a una materia se tiene que indicar el turno en que se matricula: existen dos turnos que son "de mañana" y "de tardes", así que podemos usar un campo booleano para indicar si se matricula en turno de mañana (True) y de tardes (False).

### Ejercicio: puesta en marcha del proyecto
Llegados aquí tienes algunas tareas que realizar:

1. Construye el proyecto de Django (`dwes_m2m`).

2. Crea la aplicación en dicho proyecto (`enrollment`).

3. Conocido el sistema de información de la aplicación, construye el Entidad-Relación (EER) y el Modelo Relacional para, finalmente, crear los modelos de esta aplicación. Utiliza términos en inglés:
	- Alumando: `students`
		- Nombre: `name`
		- Apellidos: `surname`
		- Edad: `age`
	- Materias: `subjects`
		- Nombre: `name`
		- Descripción: `description`
	- Matrícula: `enrollment`
		- Fecha matriculación: `enrolled_date`
		- Turno: `morning_session`
	
4. Crea y ejecuta las migraciones.

En el punto 3 es donde nos vamos a encontrar con una de las novedades porque hay dos modelos: estudiantes y materias que se relacionan por medio de una relación muchos-a-muchos que se verá reflejada con un tercer modelo. [Aquí](https://docs.djangoproject.com/en/5.0/topics/db/models/#intermediary-manytomany) tienes el ejemplo de la documentación de Django que deberías leer antes de construir los modelos de este ejercicio.

> Ese tercer modelo es la tabla intermedio del Modelo Relacional de las bases de datos relacionales que ya conoces.

## Template base
Añade un *template* llamado `base.html` en el que se tenga un menú principal y un bloque `content` donde las plantillas hijas puedan introducir contenido. Tal como hemos hecho en los Ninja Training anteriores.

## Crea un formulario para añadir materias
Crea un formulario, un `ModelForm` sería lo ideal aquí, con los campos `name` y `description` del modelo `Subject`.

Añade una URL `subjects/create/` así como la vista y el *template* necesario.

Añade un elemento al menú para acceder a este formulario.


## Crea un formulario para añadir alumnado
Haz lo mismo que has hecho en el punto anterior para las materias, pero aquí para el alumnado.

Usa la URL `students/create/`.

## Crea una vista para obtener el listado de las materias
Usa la URL `subjects/list/` y escribe la vista y el template necesario. Introduce en el menú de la aplicación un enlace para el listado.

Al lado de cada materia añade un enlace a los detalles de la materia. Por tanto, crea una nueva URl `subjects/<int:id>/detail/`, la vista correspondiente y el template correspondiente.

Al lado de cada elemento de la lista añade un enlace a los detalles.

A partir de aquí, seguimos todos juntos, en un ejercicio guiado, porque tenemos que hablar de una serie de novedades relativas al *many-to-many*.

## Completar detalles de la materia
En el mismo template de los detalles de la materia vamos a mostrar el listado con el alumndo matriculado a esta materia.

## Añadir alumnado a una materia (matricular)
En el *template* de los detalles de la materia, añade un enlace que permita añadir alumnado a dicha materia.

Esto lo pondremos en la URL `subjects/<int:id>/enroll/student/`.

Cuando el usuario haga clic en dicho enlace lo llevará a un formulario en el que podrá seleccionar un estudiante para matricularlo a la materia.
