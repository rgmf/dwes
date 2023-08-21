name: str = "Alice"
age: int = 18
height: float = 1.75

# Interpolamos el valor de la variable name.
print(f"Mi nombre es {name}")

# Interpolamos todos los datos.
print(f"Mi nombre es {name}, tengo {age} años y mido {height}m")

# Podemos interpolar el resultado de una expresión.
print(f"Dentro de 5 años tendré {age + 5} años")

# Puedes usarlo en todos los contextos.
msg: str = f"Soy {name} y tengo {age} años"
