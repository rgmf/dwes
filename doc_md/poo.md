# Clases en Python
Antes de empezar, ten en cuenta estos puntos:

- Nombre de las clases en **PascalCase**.
- Nombre de los atributos **lowercase_underscore**.
- `__init__` es el método que se llama cuando creas un objeto (constructor de la clase).
- Todos los métodos, incluido `__init__`, reciben como primer parámetro el objeto que lo invoca y lo llamamos `self`.
- Este primer parámetro no se lo tienes que pasar tú cuando llames al método. Lo inyecta Python automáticamente.

En Python los modificadores "public", "private" y "protected" son un tanto peculiares para alguien que viene de lenguajes como Java:

- Los atributos y métodos que empiezan por `__` (dos barras baja) los consideramos privados y no se puede acceder a ellos desde fuera de la clase.
- Los atributos y métodos que empiezan por `_` (una sola barra baja) los consideramos protegidos y no debes acceder a ellos fuera de la clase.
- El resto son públicos.

En esta clase:

```python
class Dog:
	def __init__(self, name: str, breed: str) -> None:
		self.__name = name
		self.__breed = breed
		
	def description(self) -> str:
		return f"Soy un perro y me llamo {self.__name}"
```

Podemos ver:

- La clase se llama `Dog`.
- El constructor recibe dos parámetros: `name` y `breed`. Recuerda que `self` es un parámetro especial donde tenemos la referencia del objeto.
- Se crean atributos con `self.` seguido del nombre del atributo. En este caso tenemos dos atributos privados: `self.__name` y `self.__breed`.
- Tenemos un método que no recibe parámetros (sí, lo sé, se pasa `self` pero es el parámetro especial). Este método es público porque su nombre es `description` y no empieza por `_` ni `__`.

# Instanciar objetos
Podemos crear objetos de esa clase así:

```python
otto: Dog = Dog("Otto", "Labrador")
oriol: Dog = Dog("Oriol", "Chihuahua")
```

Y para invocar el método `description`:

```python
otto.description()
oriol.description()
```

Fíjate cómo llamo a description dejando la lista de argumentos vacía. El parámetro `self` se lo pasa Python automáticamente. En el caso de `otto`, dentro de  `description` el parámetro `self` es `otto` y para `oriol` será `oriol`.

# Getters y setters
Estos métodos se usan en las clases para permitir el acceso a los atributos (para lectura, *getters*, y/o para escritura, *setters*).

Se denominan métodos *getters* y *setters* porque estos método suelen empezar por `get_` y `set_`. No obstante, en Python, esto también es particular y "raro" al principio: se usan decoradores:

- `@property` para los *getters*, y
- `@<nombre atributo>.setter` para los *setters*.

Veamos un par de ejemplos para aclararlo.

En este ejemplo podemos ver cómo usamos el modo tradicional pero no *pythonesco* para acceder a la fecha de nacimiento de una persona y para modificar dicha fecha. Usamos métodos `get_` y `set_`:

```python
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_date: datetime):
        self.__name: str = name
        self.__birth_date = birth_date

    def get_birth_date(self) -> datetime:
        return self.__birth_date

    def set_birth_date(self, value: datetime) -> None:
		self.__birth_date = value
```

Pero en Python deberíamos usar los decoradores que te comentaba más arriba. Este sería el ejemplo anterior en el modo *pythonesco*:

```python
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_date: datetime):
        self.__name: str = name
        self.__birth_date = birth_date

	@property
    def birth_date(self) -> datetime:
        return self.__birth_date

	@birth_date.setter
    def birth_date(self, value: datetime) -> None:
		self.__birth_date = value
```

Como ves en esta última versión los métodos *getter* y *setter* se llaman igual: `birth_date`. La diferencia está en el número de parámetros (el *setter* necesita el nuevo valor) y la decoración de los mismos.

