# Declaramos un set vacío.
# No puedes crear un set vacío así: `ids = {}` porque estarías creando un
# diccionario y no un set. Así pues, tienes que hacer lo siguiente:
ids = set()

# Declaramos un set con varios elementos de diferentes tipos.
items: set[any] = {10, "rojo", 6.75, "temperatura", True}

# Abro un paréntesis: ¿cómo saber el tipo de una variable?
print(type(items))

# Si intentas crear este set.
numbers: set[int] = {1, 2, 2, 2, 1, 3, 5}

# Varás que los duplicados han sido ignorados.
print(numbers)

# Añade nuevos elementos (si es un duplicado no se inserta): método add.
numbers.add(3)
numbers.add(7)
numbers.add(10)
print(numbers)

# Actualizar un set con un conjunto de elementos: método update.
# Se añaden los no duplicados.
odd_numbers: list[int] = [1, 3, 5, 7, 9, 11, 13, 15]
numbers.update(odd_numbers)
print(numbers)

# Elimina elementos de un set: método discard.
numbers.discard(10)
numbers.discard(100)
print(numbers)
