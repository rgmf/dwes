# Creamos una tupla vacía.
empty: tuple[any] = ()

# Un ejemplo útil.
week_days: tuple[str] = (
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
)
week_days_abbr: tuple[str] = ("L", "M", "X", "J", "V", "S", "D")

# Acceso.
print(f"El tercer día de la semana es {week_days[2]} ({week_days_abbr[2]})")

# Quieres crear un tupla de un solo elemento: cuidado, fíjate en la sintaxis.
best_number: tuple[int] = (10,)

# Algunos trucos interesantes (también funcionaría con listas).
#
# Crear una tupla a partir de dos.
t1: tuple[int] = (1, 2, 3, 4, 5)
t2: tuple[str] = ("uno", "dos", "tres", "cuatro", "cinco")
t3: tuple[int | str] = t1 + t2
print(t1)
print(t2)
print(t3)

# Repetir: multiplica.
ten: tuple[int] = (10,)
ten_ten_times: tuple[int] = ten * 10
print(ten)
print(ten_ten_times)

hi_bye: tuple[str] = ("Hi", "Bye")
hi_bye_5_times: tuple[str] = hi_bye * 5
print(hi_bye)
print(hi_bye_5_times)

# Como en las listas: comprobar si un elemento está.
print("hi" in hi_bye)
print("Bye" in hi_bye)
print("BYE".lower() in hi_bye)
print("See you later" not in hi_bye)
