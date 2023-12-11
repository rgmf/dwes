def insert_movies(conn) -> None:
    """
    Para insertar registros hay que llevar a cabo una serie de pasos que te
    marco en comentarios junto al código.
    """
    cont: bool = True

    while cont:
        title: str = input("Título de la película: ")
        release_year: int = int(input("Año de estreno: "))
        genre: str = input("Género: ")

        # 1. Crea la Query SQL que guardo en una variable de tipo str de
        #    Python.
        insert_query: str = """
        insert into movies (title, release_year, genre)
        value (%s, %s, %s)
        """
        values: tuple = (title, release_year, genre)

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
            cursor.execute(insert_query, values)

            # 4.- Cuando termines de ejecutar todas tus Query recuerda hacer un
            #     commit para hacer efectivos los cambios en la base de datos.
            #
            #     Para ello: llama al método "commit" del objeto "Connection"
            #     (recuerda que "conn" es la variable de tipo "Connection".
            conn.commit()

        print()
        print()
        reply: str = input("Añadir más [s/n]: ")
        cont = True if reply.lower() == "s" else False
