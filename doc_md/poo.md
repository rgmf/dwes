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

En este ejemplo podemos ver cómo usamos el modo tradicional pero no *pythonesco* para acceder a la fecha de nacimiento de una persona y para modificar dicha fecha. Usamos métodos `get_` y `set_`. Como ves en el ejemplo se parece mucho a cómo lo hacías en Java:

```python
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_date: datetime):
        self.__name: str = name
        self.__birth_date = birth_date
		
	def get_name(self) -> str:
		return self.__name

    def get_birth_date(self) -> datetime:
        return self.__birth_date

    def set_birth_date(self, value: datetime) -> None:
		self.__birth_date = value
		
		
if __name__ == "__main__":
	person: Person = Person("Alice", datetime(2010, 10, 10, 17, 45, 38))
	
	name: str = person.get_name()
	
	person.set_birth_date(datetime(2009, 10, 10, 17, 45, 38))
```

Pero en Python deberíamos usar los decoradores que te comentaba más arriba. Este sería el ejemplo anterior en el modo *pythonesco*. Fíjate bien cómo se accede a los métodos decorados, parece más bien un acceso a atributos:

```python
from datetime import datetime


class Person:
    def __init__(self, name: str, birth_date: datetime):
        self.__name: str = name
        self.__birth_date = birth_date
		
	@property
	def name(self) -> str:
		return self.__name

	@property
    def birth_date(self) -> datetime:
        return self.__birth_date

	@birth_date.setter
    def birth_date(self, value: datetime) -> None:
		self.__birth_date = value
		
		
if __name__ == "__main__":
	person: Person = Person("Alice", datetime(2010, 10, 10, 17, 45, 38))
	
	name: str = person.name  # se llama al método get de name.
	
	person.birth_date = datetime(2009, 10, 10, 17, 45, 38)  # se llama al método set de birth_date.
```

Como ves en esta última versión los métodos *getter* y *setter* para el atributo `birth_date` se llaman igual: `birth_date`. La diferencia está en el número de parámetros (el *setter* necesita el nuevo valor) y la decoración de los mismos.

# Métodos dunder: __str__ y __repr__
Cuando imprimes un objeto por pantalla aparece la referencia del mismo así como la posición de memoria que ocupa. Esto no nos dice mucho cuando queremos depurar y ver los valores que tienen nuestro objetos y variables.

Para ese tipo de situaciones tenemos los métodos `__str__` y `__repr__` que puedes sobreescribir en cada clase para decidir cómo se van a mostrar por pantalla en los dos contextos posibles:

- En el contexto de un string (por ejemplo porque hacemos un `print` del objeto) se ejecuta el método `__str__` de la clase del objeto.

- En el contexto de la representación de un objeto, como cuando escribimos el nombre del objeto en el REPL de Python, se lanzará el método `__repr__`.

Siguiendo con el ejemplo de la clase anterior de `Person`, si ejecuto este código:

```python
person: Person = Person("Alice", datetime(2010, 10, 10, 17, 45, 38))
print(person)
```

Lo que obtengo por pantalla es algo así:

```python
<__main__.Person object at 0x7faa67927990>
```

Lo que nos indica muy poco. Si completamos la clase con sobreescribiendo el método `__str__`:

```python
from datetime import datetime


class Person:
	def __init__(self, name: str, birth_date: datetime):
		self.__name: str = name
		self.__birth_date = birth_date
		
	@property
	def name(self) -> str:
		return self.__name

	@property
	def birth_date(self) -> datetime:
		return self.__birth_date

	@birth_date.setter
	def birth_date(self, value: datetime) -> None:
		self.__birth_date = value
		
	def __str__(self) -> str:
		return f"Nombre: {self.name}; Fec. nac.: {self.birth_date}"
```

Ahora, si ejecutamos:

```python
person: Person = Person("Alice", datetime(2010, 10, 10, 17, 45, 38))
print(person)
```

Lo que obtengo por pantalla es algo así:

```python
Nombre: Alice; Fec. nac.: 2010-10-10 17:45:38
```

Y, ahora sí, esto tiene más sentido para nosotros como desarrolladores para poder depurar y visualizar el contenido de la clase `Person`.

Por último, te muestro cómo sobreescribir el método `__repr__` para completar la clase `Person`:

```python
from datetime import datetime


class Person:
	def __init__(self, name: str, birth_date: datetime):
		self.__name: str = name
		self.__birth_date = birth_date
		
	@property
	def name(self) -> str:
		return self.__name

	@property
	def birth_date(self) -> datetime:
		return self.__birth_date

	@birth_date.setter
	def birth_date(self, value: datetime) -> None:
		self.__birth_date = value
		
	def __str__(self) -> str:
		return f"Nombre: {self.name}; Fec. nac.: {self.birth_date}"
		
	def __repr__(self) -> str:
		class_name: str = type(self).__name__
		return f"{class_name}(title={self.__name!r}, author={self.__birt_date!r})"
```

Siempre puedes llamar de forma explícita a los métodos `__str__` y `__repr__`:

```python
person: Person = Person("Alice", datetime(2010, 10, 10, 17, 45, 38))
print(person.__str__())
print(person.__repr__())
```
