def delete_movies_between_dates(conn) -> None:
    """
    Para eliminar registros hay que llevar a cabo una serie de pasos que te
    marco en comentarios junto al código.
    """
    year1: str = input("Año de inicio: ")
    year2: str = input("Año de fin: ")

    # 1. Crea la Query SQL que guardo en una variable de tipo str de
    #    Python.
    delete_query: str = """
    delete from movies
    where release_year >= %s and release_year <= %s
    """
    values: tuple[int, int] = (year1, year2)

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
        cursor.execute(delete_query, values)

        # 4.- Cuando termines de ejecutar todas tus Query recuerda hacer un
        #     commit para hacer efectivos los cambios en la base de datos.
        #
        #     Para ello: llama al método "commit" del objeto "Connection"
        #     (recuerda que "conn" es la variable de tipo "Connection".
        conn.commit()

        # 5.- Para todas las operaciones que hagas con el cursor puedes
        #     obtener el número de filas afectadas con el atributo "rowcount"
        #     del objeto "Cursor".
        print(f"Películas eliminadas: {cursor.rowcount}")
