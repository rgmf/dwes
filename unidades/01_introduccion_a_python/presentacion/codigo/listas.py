# Declaramos una lista con 5 números enteros.
nums = [2, 4, 6, 8, 10]

# Lo mismo pero con "type hint".
nums: list[int] = [2, 4, 6, 8, 10]

# Podemos "printear" la lista completa.
print(nums)

# Podemos mostrar solo un elemento, por ejemplo, el segundo elemento.
print(nums[1])

# Podemos mostrar el número de elementos de la lista con len().
# Igual que hacíamos con los str.
print(len(nums))

# Para acceder al último elemento de una lista.
# El modo no "pythonic".
print(nums[len(nums) -1])

# Es muy feo. Usemos el modo "pythonic".
# En Python podemos usar índices negativos para recorrer la lista al revés.
print(nums[-1])

# El penúltimo elemento.
print(nums[-2])

# Podemos mostrar un rango (slicing).
# En este ejemplo, mostramos los elementos del 2º al 3º.
# Como ves, la cota inferior está incluido y la superior no.
# Va a mostrar: [4, 6].
print(nums[1:3])

# Además, podemos dejar una cota vacía para indicar "hasta el últmo" o "desde
# el principio".
# Aquí tienes un ejemplo: desde el tercer elemento hasta el último.
print(nums[2:])

# O desde el principio hasta el 3º (recuerda que la cota superior no está
# incluida).
print(nums[:3])

# Rizando el rizo: desde el penúltimo hasta el final con índices negativos.
print(nums[-2:])

# Las listas aceptan un elemento más entre corchetes: el stride (o el paso, los
# saltos que dará para sacar los elementosde la lista: de 2 en 2, de 3 en 3...
print(nums[0:5:2])
print(nums[::3])

# Así, el formato es: lista[start:end:stride]

# Lo más chulo de todo (gracias a que Python es de tipado dinámico): en una
# lista podemos tener elementos de diferente tipo.
mix_list: list = [1, "Hello", 3.4, 1]

# Ojo al detalle: como ves, en una lista de Python puede haber duplicados. El
# primer elemento y el último son el mismo.
print(mix_list)
print(len(mix_list))

# Puedes eliminar un elemento.
del mix_list[1]
print(mix_list)

# O añadir nuevos (se añaden al final).
mix_list.append(10)
print(mix_list)

# Obviamente, los puedes modificar.
mix_list[1] = 3
print(mix_list)

# Tienes muchas otras operaciones con listas.
# Órdena una lista (el método sort modifica la lista).
mix_list.sort()
print(mix_list)

# Órdenala al revés (pasa True al argumento "reverse" del método sort).
mix_list.sort(reverse=True)
print(mix_list)

# Puedes comprobar si un elemento está en una lista con los operadores: in y
# not in (devuelven True o False según el caso).
# Por ejemplo, vamos a preguntarnos si en mix_list está el elemento 1.
has_item_1 = 1 in mix_list
print(has_item_1)

# Vamos a ver si no tiene el 100.
no_item_100 = 100 not in mix_list
print(no_item_100)

# También puedes extender y añadir listas a listas.
# Imagina estas dos listas.
l1: list[int] = [1, 2, 3]
l2: list[int] = [4, 5]

# Veamos cómo extender una lista con elementos de otras listas.
l1.extend(l2)
print(l1)

# Y si haces una suma de listas...
l3: list[int] = l1 + [10, 11, 12]
print(l3)
