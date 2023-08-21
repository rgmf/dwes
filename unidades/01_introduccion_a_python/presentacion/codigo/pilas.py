# Creamos una pila vacía.
stack: list[int] = []

# Apilamos elementos.
stack.append(1)
stack.append(10)
stack.append(100)

# Veamos la pila.
print(stack)

# Vamos a desapilar (sacar el último elemento).
last: int = stack.pop()

# Ahora, el número 100 está en last y la pila tiene un elemento menos.
print(last)
print(stack)

# Si intentamos sacar elementos de una pila vacía obtendremos un error.
stack.pop()
stack.pop()
stack.pop() # aquí salta una excepción (stack está vacía)
