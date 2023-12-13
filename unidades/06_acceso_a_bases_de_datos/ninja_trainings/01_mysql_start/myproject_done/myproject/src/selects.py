from mysql.connector import connect, Error


def select_movies_by_title() -> None:
    # 1. Todo este código lo metemos en un bloque try-except para manejar
    #    posibles excepciones.
    try:
        # 2. Conectamos con MariaDB/MySQL.
        #    Usamos un Context Manager para la gestión automática del recurso,
        #    así se libera automáticamente.
        with connect(
                host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            title: str = input("Título de la película que quieres buscar: ")

            # 3. Crea la Query SQL que guardo en una variable de tipo str de
            #    Python.
            select_query: str = """
            select title, release_year, genre
            from movies
            where title like %s
            """
            values: tuple = (f"%{title}%",)

            # 4.- Creamos un Cursor de MySQL. Es el objeto con el que podemos
            #     acceder a MySQL para seleccionar, insertar, eliminar o
            #     actualizar datos.
            #
            #     Para crear el cursor solo hay que llamar al método "cursor" del
            #     objeto "Connection" ("conn" es el objeto de tipo "Connection").
            #
            #     Todo esto se hace, de nuevo, dentro de un Context Manager de
            #     Python porque hay que liberar el cursor una vez terminamos y con
            #     el Context Manager la liberación de los recursos es automático,
            #     nos libramos de tener que cerrar el cursor "manualmente".
            with conn.cursor() as cursor:
                # 5.- Usamos el cursor para ejecutar la Query.
                #     Se usa el método "execute" del objeto "Cursor" ("cursor es la
                #     variable de tipo "Cursor").
                cursor.execute(select_query, values)

                # 6.- Como es una SELECT, tras ejecutar la sentencia, podemos recuperar
                #     los resultados con el método "fetchall" del "Cursor".
                #
                #     Esto devuelve una lista de tuplas. Los elementos de la tupla son
                #     los campos que proyectamos en la SELECT, en el mismo orden, en
                #     nuestor caso: title, release_year y genre.
                #
                #     Podemos decir que cada tupla es una fila de resultados.
                results = cursor.fetchall()

                # 7.- Recorremos los resultados para mostrarlos por pantalla.
                print("Resultados de la búsqueda: ")
                for row in results:
                    print(f"Título: {row[0]}")
                    print(f"Año de lanzamiento: {row[1]}")
                    print(f"Género: {row[2]}")
                    print()

    except Error as e:
        print(f"Error fatal: {e}")
