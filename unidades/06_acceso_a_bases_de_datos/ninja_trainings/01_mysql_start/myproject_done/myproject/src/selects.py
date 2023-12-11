def select_movies_by_title(conn) -> None:
    """
    Para seleccionar registros hay que llevar a cabo una serie de pasos que te
    marco en comentarios junto al código.
    """
    title: str = input("Título de la película que quieres buscar: ")

    # 1. Crea la Query SQL que guardo en una variable de tipo str de
    #    Python.
    select_query: str = f"""
    select title, release_year, genre
    from movies
    where title like "%{title}%"
    """

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
        cursor.execute(select_query)

        # 4.- Como es una SELECT, tras ejecutar la sentencia, podemos recuperar
        #     los resultados con el método "fetchall" del "Cursor".
        #
        #     Esto devuelve una lista de tuplas. Los elementos de la tupla son
        #     los campos que proyectamos en la SELECT, en el mismo orden, en
        #     nuestor caso: title, release_year y genre.
        #
        #     Podemos decir que cada tupla es una fila de resultados.
        results = cursor.fetchall()

        # 5.- Recorremos los resultados para mostrarlos por pantalla.
        print("Resultados de la búsqueda: ")
        for row in results:
            print(f"Título: {row[0]}")
            print(f"Año de lanzamiento: {row[1]}")
            print(f"Género: {row[2]}")
            print()
