# Ejemplo de `if` (de paso vemos cómo pedir datos teclado con `input`).
age: int = int(input("Escribe tu edad: "))
if age < 18:
    print("Deberías llevar cuidado.")

# Ejemplo de `if-else`.
number: int = int(input("Escribe un número par: "))
if number % 2 == 0:
    print("Enhorabuena, parece que conoces los números pares.")
else:
    print(f"{number} no es un número par... deberías repasar más.")

# Ejemplo de `if-elif-else`.
number: int = int(input("Escribe un número: "))
if number > 0:
    print(f"{number} es mayor que 0.")
elif number < 0:
    print(f"{number} es menor que 0.")
else:
    print("Has escrito el número 0.")

# Un `if-else` más.
password: str = input("Escribe una contraseña de más de 7 caracteres: ")
if len(password) < 8:
    print("La contraseña que has escrito no es válida.")
else:
    print(f"La contraseña que has escrito tiene {len(password)} caracteres.")

# Condiciones compuestas.
word: str = input(
    "Escribe una palabra (sin espacios) con, al menos, 5 caracteres: "
)
if len(word) < 5 or " " in word:
    print(f"La palabra '{word}' no cumple con los requisitos.")
else:
    print(f"Bien, la palabra '{word}' cumple los requisitos.")

# Mismo programa que arriba pero dándole la vuelta a las condiciones.
word: str = input(
    "Escribe una palabra (sin espacios) con, al menos, 5 caracteres: "
)
if len(word) >= 5 and " " not in word:
    print(f"Bien, la palabra '{word}' cumple los requisitos.")
else:
    print(f"La palabra '{word}' no cumple con los requisitos.")
