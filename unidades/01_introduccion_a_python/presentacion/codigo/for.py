# Típico programa: imprimir los primeros 10 números, del 0 al 9.
for i in range(10):
    print(i)

# Para ir entiendo qué hace range: imprimir números del 5 al 20.
for i in range(5, 21):
    print(i)

# Recorrer una lista.
students: list[str] = ["Alice", "Bob", "Mary", "Jon"]
for name in students:
    print(name)

# También podemos recorrer strings (porque son listas de caracteres).
name: str = input("Escribe tu nombre: ")
for c in name:
    print(c)

# Validar contraseña.
password: str = input(
    "Contraseña con más de 7 caracteres y, al menos, un número: "
)
has_number: bool = False
for c in password:
    if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        has_number = True

if len(password) > 7 and has_number:
    print(f"La contraseña '{password}' es correcta.")
else:
    print(f"La contraseña '{password}' no cumple los requisitos.")

# PARA DESESPERADOS: en Python, el problema anterior se puede resolver de una
# manera más "Pythonic", usando "list comprehension" que veremos más adelante.
# Como ves, nos quitamos el bucle for de encima.
#
# Este es un ejemplo de lo que se suele decir:
# "Se tarda muy poco en escribir programas en Python y toda una vida para
# aprender Python".
password: str = input(
    "Contraseña con más de 7 caracteres y, al menos, un número: "
)
if len(password) > 7 and [c for c in password if c.isdigit()]:
    print(f"La contraseña '{password}' es correcta.")
else:
    print(f"La contraseña '{password}' no cumple los requisitos.")

# Reto: ¿cuántas pruebas se necesitan para tener una cobertura total?


# Recorrer un diccionario.
student_grades: dict[str, float] = {
    "Alice": 6.75,
    "Bob": 8.5,
    "Mary": 9.0,
    "Jon": 4.25
}
for name, mark in student_grades.items():
    print(f"{name} ha sacado un {mark}")

# Si solo quieres los keys (en este caso los nombres).
for name in student_grades.keys():
    print(name)

# Si solo quieres los values (en este caso las notas).
for mark in student_grades.values():
    print(mark)

# Reto: escribe un programa que indique, dado un diccionario como el de arriba,
# los siguientes datos:
# - Cuántos aprobados hay.
# - Cuántos suspensos hay.
# - Quién ha sacado la nota más alta.

# Por último, ¿qué pasa si quieres el índice como se puede hacer en Java?
# Usamos: enumerate.
students: list[str] = ["Alice", "Bob", "Mary", "Jon"]
for i, name in enumerate(students):
    print(f"Estudiante número {i}: {name}")


# Devuelve esta salida:
# Estudiante número 0: Alice
# Estudiante número 1: Bob
# Estudiante número 2: Mary
# Estudiante número 3: Jon
