# Manejo de relaciones muchos-a-muchos (m2m)
Vamos a completar un nuevo proyecto de Django en el que vamos a aprender a manejar relaciones entre los modelos **muchos-a-muchos** o **many-to-many** (**m2m**).

> [Aquí](https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_many/) encontrarás más información sobre las relaciones muchos-a-muchos en Django.

> También te resultará útil saber cómo [manejar el modelo intermedio](https://docs.djangoproject.com/en/5.0/topics/db/models/#intermediary-manytomany) en relaciones muchos-a-muchos.

## Descripción del proyecto
El proyecto consta de una apliación llamada `enrollment` en el que podemos:

- Crear materias (asignaturas, módulos... como lo quieras llamar).
- Crear alumnado.
- Matricular al alumnado en las diferentes materias.

Así pues, en dicha aplicación vamos a tener alumnado de los que conocemos su nombre, apellidos y edad.

Este alumnado podrá matricularse a una serie de materias de las que conocemos el nombre de la materia y una descripción.

Cuando se matricula alumnado a una materia se tiene que indicar el turno en que se matricula: existen dos turnos que son "de mañana" y "de tardes", así que podemos usar un campo booleano para indicar si se matricula en turno de mañana (True) y de tardes (False).

El Entidad-Relación Extendido se describe a continuación. En él ves que hay una relación muchos a muchos y la tabla intermedia require de dos atributos (información): fecha de matriculación y turno.

``` text


                                 +---------+
+-----------+               N   /           \  N                   +-----------+
| Subject   |------------------| Enrollment  |---------------------| Student   |
+-----------+                   \           /                      +-----------+
                                 +---------+


subjects(id, name, description)
	PK: id
	VNN: name, description
	
students(id, name, surname, age)
	PK: id
	VNN: name, surname, age
	
enrollments(id, subject, student, enrolled_date, morning_session)
	PK: id
	VNN: subject, student, enrolled_date, morning_session
	FK: subject -> subjects(id)
	FK: student -> students(id)
```

## Completar el proyecto `todo`
Estas son las tareas que faltan por hacer:

- Crear los modelos (**models**)
- Añadir el listado del alumnado al detalle de las materias (**template subject_detail**)
- Crear una URL para matricular alumnado a una materia (**subjects/<int:id>/students/enroll/**)
- Escribir la vista para esta matriculación (**views**)
- Añadir un enlace, en el detalle de las materias, que permita matricular alumnado a la materia
