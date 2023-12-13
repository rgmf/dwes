# Requisitos
Vas a necesitar **MariaDB o MySQL** instalado. Y, además, vamos a usar el driver/librería de MySQL para Python llamado `mysql-connector-python` que puedes instalar con `pip install mysql-connector-python`.

# Aclaración importante
Yo aquí **voy a hablar siempre de MariaDB**. Pero, da igual, si quieres utilizar MySQL hazlo.

¿De dónde viene todo este lío de MariaDB / MySQL, MySQL / MariaDB? Te lo resumo pero lo mejor es que, si te interesa, busques información lo más objetiva posible por ahí... si tal cosa existe.

MySQL nació como proyecto de software libre hace mucho tiempo,

no teníamos tantas opciones: Oracle y SQL Server,

poco más,

nada de NoSQL, "solo" relacionales,

MySQL se posicionó como una de las opciones de SGBD relacionales más populares,

entonces Oracle adquirió MySQL... y empieza el lío,

el equipo original de MySQL creo un fork,

¿cómo lo llamaron? ¡Sí!, MariaDB,

MariaDB y MySQL siguieron caminos separados,

yo me quedo con MariaDB,

tú haz lo que quieras,

no pasa nada.

# Directos al código
Desde un programa en Python puedes hacer todo tipo de operaciones con bases de datos: *selects*, *inserts*, *deletes*, *updates*, *create tables*, *update tables*, *create databases*... todo, es todo.

En clase nos vamos a centrar en las **operaciones CRUD**: **C**reate, **R**ead, **U**pdate y **D**elete, por lo que tendremos que montar la base de datos por otro lado o dicho de otro modo: siempre vamos a partir de la base de datos creada.

Los pasos que se tienen que dar, cada vez que tengas que acceder a la base de datos, siempre son los mismos:

1. Abrir conexión con MariaDB.
2. Crear un cursor.
3. Usar ese cursor para realizar operaciones (SQL).
4. Recoger resultados.

## Ejemplo de insert
```python
from mysql.connector import connect


with connect(host="l", user="d", password="d", database="db") as conn:
	with conn.cursor() as cursor:
		sql = """
			insert into students (nia, name, age)
			values (%s, %s, %s)
		"""
		values = (101, "Alice", 20)
		
		cursor.execute(sql, values)
		
		conn.commit()
		
		if cursor.rowcount == 1:
			print("Se ha insertado el estudiante")
		else:
			print("No se ha insertado el estudiante")
```

## Ejemplo de múltiples inserts
```python
from mysql.connector import connect


with connect(host="l", user="d", password="d", database="db") as conn:
	with conn.cursor() as cursor:
		sql = """
			insert into students (nia, name, age)
			values (%s, %s, %s)
		"""
		values = [
			(101, "Alice", 20),
			(102, "Bob", 18),
			(103, "Mary", 19),
		]
		
		cursor.executemany(sql, values)
		
		conn.commit()
		
		if cursor.rowcount == 3:
			print("Se han insertado los 3 estudiante")
		else:
			print(f"Solo se han insertado {cursor.rowcount} estudiantes")
```

## Ejemplo de delete
```python
from mysql.connector import connect


with connect(host="l", user="d", password="d", database="db") as conn:
	with conn.cursor() as cursor:
		sql = """
			delete from students
			where age < %s
		"""
		values = (18,)
		
		cursor.execute(sql, values)
		
		conn.commit()
		
		print(f"Se han eliminado {cursor.rowcount} estudiantes")
```

## Ejemplo de update
```python
from mysql.connector import connect


with connect(host="l", user="d", password="d", database="db") as conn:
	with conn.cursor() as cursor:
		sql = """
			update students set age=%s
			where age < %s
		"""
		values = (18, 18)
		
		cursor.execute(sql, values)
		
		conn.commit()
		
		print(f"Se han actualizado {cursor.rowcount} estudiantes")
```

# Ejemplo de select
```python
from mysql.connector import connect


with connect(host="l", user="d", password="d", database="db") as conn:
	with conn.cursor() as cursor:
		sql = "select nia, name, age from students"
		
		results = cursor.execute(sql, values)
		for row in results:
			print(f"Datos del estudiante con NIA {row[0]}:")
			print(f"Nombre: {row[1]}")
			print(f"Edad: {row[2]}")
			print()
```
