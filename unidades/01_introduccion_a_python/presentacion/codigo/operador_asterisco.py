# Una lista de edades de coches en años.
car_ages: list[int] = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]

# Queremos obtener los dos coches de mayor antigüedad.
# 1. Ordenamos la lista al revés.
car_ages.sort(reverse=True)
# 2. El primero de la lista, ahora es el más antiguo.
oldest: int = car_ages[0]
# 3. El segundo de la lista, ahora es el segudno más antiguo.
second_oldest: int = car_ages[1]
# 4. Vamos a guardar el resto de coches en otra lista.
others: list[int] = car_ages[2:]

# El operador * nos permitiría hacer esto de forma más fácil.
# Pero primero, veamos cómo funciona y para que se utiliza.
students: list[str] = ["Alice", "Bob", "María", "Juan"]

# Nos interesan los dos primero estudiantes, así que el resto los ignoramos.
student1, student2, _, _ = students

# Si no nos interesan más que los dos primero estudiantes, usemos el operador
# asterisco para desempaquetar dejando los sobrantes en otro lugar (en la
# variable con el asterisco).
student1, student2, *other_students = students

# Ahora podemos simplificar nuestro programa de los coches.
# Lo repito entero.
car_ages: list[int] = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages.sort(reverse=True)
oldest, second_oldest, *others = car_ages
