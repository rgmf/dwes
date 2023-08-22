###############################################################################
#
# Primera parte: introducció a las funciones en Python
#
###############################################################################

# En Python:
# - usamos la palabra reservada `def` para declarar una función,
# - al declarar la función elegimos un identificador (nombre) siguiendo el
#   formato unser_score,
# - entre paréntesis ponemos la lista de argumentos (puede ser una lista
#   vacía),
# - terminamos con el carácter dos puntos y, en las líneas siguientes
#   escribimos el cuerpo de la función.
def hello_world():
    print("Hola Mundo")


# La función de arriba no devuelve ningún valor. Podemos anotar el resultado
# que devuelve la función de esta manera (en este caso no devuelve nada).
def bye_bye() -> None:
    print("Adiós mundo")


# Una función más en la que tenemos argumentos (sin anotación de tipos).
def add(n1, n2):
    addition = n1 + n2
    return addition


# Una función, parecida a la de arriba, anotando tipos (type hint).
def sub(n1: int, n2: int) -> int:
    substraction: int = n1 - n2
    return substraction


# Por último, veamos cómo llamar a cada una de las funciones de arriba.
hello_world()
bye_bye()
add(15, 25)
sub(3, 4)


###############################################################################
#
# Segunda parte: valores por defecto
#
###############################################################################

# Valor por defecto en parámetros de una función.
# (TIENEN QUE PONERSE AL FINAL).
def my_country(country: str = "Spain") -> None:
    print(f"Soy de {country}")


# Sin type hint:
# def my_countr(country="Spain"):
#     print(f"Soy de {country}")


def greet(name: str, weather: int, status: str = "bien") -> None:
    print(f"Hola, estoy {status} y estamos a {weather}ºC")


# Sin type hint:
# def greet(name, weather, status="bien"):
#     print(f"Hola, estoy {status} y estamos a {weather}ºC")


# Llamando a `greet`.
greet("Román", 25)
greet("Román", 25, "my bien")


###############################################################################
#
# Tercera parte: número de parámetros arbitrario.
#
###############################################################################

# Número de parámetros arbitrario (sin type hint).
def last_student_v1(*students):
    print(f"El último estudiante es {students[-1]}.")

    print(f"Hay {len(students)} estudiantes, que son:")
    for name in students:
        print(name)

    return students[-1]


# Con type hint: sí, efectivamente, como ves, `students` es una tupla y, por
# tanto, dentro de la función no se pueden cambiar los elementos de
# `students`.
#
# NOTA: uso `pass` como cuerpo de esta función porque la implementación de esta
# función es la misma que la de arriba.
def last_student_v2(*students: tuple[str]) -> str:
    pass


# Por último: es habitual usar como parámetro el nombre `args` en estos casos.
def last_student_v3(*args: tuple[str]) -> str:
    pass


# Veamos cómo se llama a estas funciones.
last_student_v1("Alice", "Bob", "Mary", "Jon")


###############################################################################
#
# Cuarta parte: keywork arguments (kwargs)
#
###############################################################################

# También puedes enviar agumentos con la anotación `key=value`, de manera que
# no te tengas que acordar del orden de los parámetros.
#
# Nota: La frase "keyword arguments" se suele abreviar como "kwargs".
def my_func(child3, child2, child1):
    print(f"El hijo más joven es {child3}")


my_func(child1="Alice", child2="Bob", child3="Mary")


###############################################################################
#
# Quinta parte: número de kwargs arbitrario.
#
###############################################################################

# Una función que recibe un número de hijos arbitrario.
def my_children(**children):
    print("Listado de hijos:")
    for k, v in children:
        print(f"{k}: {v}")


# Con type hint.
def my_children_th(**children: dict[str, int]) -> None:
    print("Listado de hijos:")
    for k, v in children:
        print(f"{k}: {v}")


# Podemos llamar a `my_children` con un número de argumentos diferente.
my_children(alice=18, bob=23)
my_children(bob=23, mary=20, alice=18)
my_children(jon=17)


###############################################################################
#
# Sexta parte: mezclando tipos de argumentos.
#
###############################################################################

# Si tenemos en una función todo tipo de parámetros, tienen que ir en este
# orden:
#
# 1º) Parámetros posicionales
# 2º) Parámetros con valor por defecto
# 3º) Parámetros arbitrarios posicionales (*args)
# 4º) Parámetros arbitrarios de palabra clave (**kwargs)
def my_func_all_param(param1, param2, param3="default", *args, **kwargs):
    print("Has llamado a my_func_all_param con estos argumentos:")
    print(f"param1 =>     {param1}")
    print(f"param2 =>     {param2}")
    print(f"param3 =>     {param3}")
    print(f"num args =>   {len(args)}")
    print(f"num kwargs => {len(kwargs)}")
    print()


# Veamos cómo podemos llamara esta función (opciones diferentes).
my_func_all_param(10, 20)
my_func_all_param(10, 20, "uno", "dos", "tres")
my_func_all_param(10, 20, "uno", "dos", "tres", cuatro="cinco", seis="siete")
my_func_all_param(10, 20, "uno", cuatro="cinco", seis="siete")
