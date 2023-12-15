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
4. Recoger resultados: rowcount o fetchone/fetchall.

> fetchone o fetchall solo hay que usarlo para sentencias SQL Select para recoger la información de las filas (tuplas) devueltas como resultado de dicha select.

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

## Ejemplo de select
```python
from mysql.connector import connect


with connect(host="l", user="d", password="d", database="db") as conn:
    with conn.cursor() as cursor:
        sql = "select nia, name, age from students"
        
        cursor.execute(sql, values)
        results = cursor.fetchall()
        for row in results:
            print(f"Datos del estudiante con NIA {row[0]}:")
            print(f"Nombre: {row[1]}")
            print(f"Edad: {row[2]}")
            print()
```

# Notas importantes
Te pongo un código de ejemplo, el que vimos en clase, y te recurdo algunos puntos en los subapartados siguientes.

Pero antes, este es el Modelo Relacional de la base de datos sobre el que actúa este código:

```text
categories(id, name)
    PK: id

comments(id, comment, category)
    PK: id
    FK: category -> categories(id)
```

Y aquí el código:

```python
def insert_comment(comment: str, category: str) -> None:
    with connect(host="h", user="u", password="p", database="db") as conn:
        with conn.cursor(buffered=True) as cursor:
            sql = "select id from categories where name=%s"
            values = (category_name,)

            category_id = None

            cursor.execute(sql, values)
            result = cursor.fetchone()
            if not result:
                sql = "insert into categories (name) values (%s)"
                values = (category_name,)

                cursor.execute(sql, values)
                conn.commit()

                category_id = cursor.lastrowid
            else:
                category_id = result[0]

            sql = "insert into comments (comment, category) values (%s, %s)"
            values = (comment, category_id)

            cursor.execute(sql, values)
            conn.commit()
```

## Atributos del cursor
Recuerda que el objeto `Cursor` tiene varias propiedades que te pueden resultar muy útil y que acabarás usando:

- `rowcount`: es un atributo de tipo `int` que contiene el número de filas efactada en la última query. Puedes usar este valor para verificar que la operación haya sido correcta. También puedes comprobar cuántas filas se han insertado, eliminado, actualizado...

- `lastrowid`: tiene el último valor generado por un atributo con el *flag* de `auto_increment`. El ejemplo típico de uso es el siguiente: insertas un registro nuevo en una tabla con un insert y quieres/necesitas el valor que se ha generado para el `id` en esa tabla.

## No olvides el commit
Cuando hagas *insert*, *delete* o *update* no olvides llamar al método `commit` del conector a MariaDB después de elecutar la SQL.

## ¿Quieres ejecutar varias SQL con el mismo objeto cursor?
Pues no olvides pasar al parámetro `buffered` el valor de `True`:

```python
...

with conn.cursor(buffered=True) as cursor:
    ...
    
...
```

# Y, por último: manejo de excepciones
En todos los casos conviene que envuelvas todo el código en un bloque `try-except` y uses el sistema de *logs* de Python disponible en el módulo `logging`.

Esto te permitirá salir de los errores de manera controlada y tu programa seguirá ejecutándose.

```python
import logging

from mysql.connector import connect

logging.basicConfig(level=logging.DEBUG)


try:
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
except Exception as e:
    logging.debug(f"Error en la base de datos: {str(e)}")
```
