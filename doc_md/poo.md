# Clases en Python
Antes de empezar, ten en cuenta estos puntos:

- Nombre de las clases en **PascalCase**.
- Nombre de los atributos **lowercase_underscore**.
- `__init__` es el método que se llama cuando creas un objeto (constructor de la clase).
- Todos los métodos, incluido `__init__`, reciben como primer parámetro el objeto que lo invoca y lo llamamos `self`.
- Este primer parámetro no se lo tienes que pasar tú cuando llames al método. Lo inyecta Python automáticamente.

En Python los modificadores "public", "private" y "protected" es un tanto peculiar para alguien que viene de lenguajes OO como Java:

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
