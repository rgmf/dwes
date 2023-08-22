# Creamos un diccionario vacío.
d: dict = {}

# Creamos un diccionario con las notas del alumnado.
grades: dict[str, float] = {"Alice": 9.75, "Bob": 8.5}

# Añadimos una alumna más al diccionario anterior.
grades["Mary"] = 7.0

# Modificamos la nota de "Alice".
grades["Alice"] = 9.25

# Eliminamos a "Mary".
del grades["Mary"]

# ¿Tenemos un alumno llamado "Bob" en el diccionario?
# Podemos comprobar si tenemos una key en el diccionario con el operador `in`.
has_bob: bool = "Bob" in grades

# Obtenemos una lista con el alumnado.
# Al convertir un dict en un list obtenemos la lista de keys.
student_names: list[str] = list(grades)

# Podemos obtener las claves y los valores en vistas de objetos.
# Útil para recorrerlos en bucles (lo veremos más adelante).
student_names = grades.keys()  # dict_keys(['Alice', 'Bob'])
student_names_list: list[str] = list(student_names)

student_marks = grades.values()  # dict_values([9.25, 8.5])
student_marks_list: list[float] = list(student_marks)

# Puedes crear dict con el constructor `dict` lo que es más cómodo si tienes
# que crear un dict en el que los keys son strings.
grades: dict[str, float] = dict(Alice=9.75, Bob=8.5, Mary=7.0)
