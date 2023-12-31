from mysql.connector import connect, Error


def update_movie_by_id() -> None:
    # 1. Todo este código lo metemos en un bloque try-except para manejar
    #    posibles excepciones.
    try:
        # 2. Conectamos con MariaDB/MySQL.
        #    Usamos un Context Manager para la gestión automática del recurso,
        #    así se libera automáticamente.
        with connect(
                host="db", user="dwes", password="dwes", database="dwesdb"
        ) as conn:
            id: str = input("ID de la película a modificar: ")
            title: str = input("Nuevo título de la película: ")
            release_year: int = int(input("Nuevo año de estreno: "))
            genre: str = input("Nuevo género: ")

            # 1. Crea la Query SQL que guardo en una variable de tipo str de
            #    Python.
            update_query: str = """
            update movies set
            title=%s, release_year=%s, genre=%s
            where id=%s
            """
            values: tuple = (title, release_year, genre, id)

            # 2.- Creamos un Cursor de MySQL. Es el objeto con el que podemos
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
                # 3.- Usamos el cursor para ejecutar la Query.
                #     Se usa el método "execute" del objeto "Cursor" ("cursor es la
                #     variable de tipo "Cursor").
                cursor.execute(update_query, values)

                # 4.- Cuando termines de ejecutar todas tus Query recuerda hacer un
                #     commit para hacer efectivos los cambios en la base de datos.
                #
                #     Para ello: llama al método "commit" del objeto "Connection"
                #     (recuerda que "conn" es la variable de tipo "Connection".
                conn.commit()

                # 5.- Para todas las operaciones que hagas con el cursor puedes
                #     obtener el número de filas afectadas con el atributo "rowcount"
                #     del objeto "Cursor".
                #
                #     En este caso podemos conocer si se ha producido o no la
                #     actualización.
                if cursor.rowcount == 0:
                    print(f"No existe la películoa con ID = {id}")
                else:
                    print(f"Se actualizó la película con ID = {id}")

    except Error as e:
        print(f"Error fatal: {e}")
