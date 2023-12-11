import os

from mysql.connector import connect, Error

from src.inserts import insert_movies
from src.selects import select_movies_by_title
from src.deletes import delete_movies_between_dates
from src.updates import update_movie_by_id


# Conectamos a la base de datos dentro de un context manager.
# Esta parte es susceptible a errores:
# - El servidor no reponde
# - Los datos de conexión no son correctos
# - ...
# Por tanto hay que poner esta conexión en un try-except.
try:
    with connect(
            host="db", user="dwes", password="dwes", database="dwesdb"
    ) as connection:
        option: int = -1
        while option != 0:
            os.system("clear")
            print("MENÚ")
            print("--------------------------------------------------------------")
            print("1.- Insertar películas")
            print("2.- Buscar películas por título")
            print("3.- Eliminar película")
            print("4.- Modificar película por id")
            print("0.- Salir")

            option = int(input("Opción: "))

            if option == 1:
                os.system("clear")
                insert_movies(connection)
                input("Pulsa intro para continuar... ")
            elif option == 2:
                os.system("clear")
                select_movies_by_title(connection)
                input("Pulsa intro para continuar... ")
            elif option == 3:
                os.system("clear")
                delete_movies_between_dates(connection)
                input("Pulsa intro para continuar... ")
            elif option == 4:
                os.system("clear")
                update_movie_by_id(connection)
                input("Pulsa intro para continuar... ")
            elif option == 0:
                print("Hasta pronto!")
            else:
                print("Error: opción desconocida")
                input("Pulsa intro para continuar... ")
except Error as e:
    print(f"Error fatal: {e}")
