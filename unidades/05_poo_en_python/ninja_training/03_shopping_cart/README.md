# Descripción del Ninja Training
En este Ninja Training vas a realizar un programa aplicando la orientación a objetos en Python. En concreto vas a implementar un *Shopping Cart* o carrito de la compra.

Solo tienes que implementar las clases que te indico a continuación en formato UML. Escribe estas clases en un fichero llamado `shopping_cart.py`, dentro de una carpeta llamada `src`. Recuerda crear los ficheros `__init__.py` para convertir las carpetas que creas en paquetes de Python.

| Product                                                                                                                                                 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| - uuid: str<br> - name: str<br> - description: str<br> -price: float                                                                                    |
| + Product(name: str, description: str, prices: float)<br> + get_uuid(): str<br> + get_name(): str<br> + get_description(): str<br> + get_price(): float |


- `uuid` será el identificador único del `Product`. Usa la función `uuid4()` del módulo `uuid` de Python para generar un identificador único.
- El resto de atributos de la clase serán inicializados en el constructor.
- Esta clase solo tiene método **getter** para poder acceder a los atributos de la clase.


| ShoppingCart                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| - products: list[Product]                                                                                                                      |
| + ShoppingCart()<br> + total_price(): float<br> + get_products(): list[Product]<br> + add_product(p: Product)<br> + remove_product(p: Product) |


- El constructor de esta clase crea un carrito vacío (lista de `Product` vacía).
- Se pueden añadir productos repetidos (mismo `uuid`).
- El método `remove_product` elimina todos los productos que son como `p`. Dos productos son el mismo producto si tienen el mismo `uuid`.


UML es un lenguaje de modelado general que se usa independientemente del lenguaje final. En Python, cuando vayamos a implementar estos modelos de UML cambiaremos algunas cosas:

1. Los constructores en Python son el método `__init__`. Cuando ves en el UML el método `+ ShoppingCart()`, en Python, tendrás que crear el método `__init__(self)` (en este caso sin pasarle nada... sí, recibe el parámetro especial `self`, pero ya sabes que ese parámetro es "como si no existiera" porque nosotros no se lo pasamos, lo hace Python).

2. Los atributos privados empezarán por `__`. Es decir, en vez de usar `uuid` como nombre de atributo de `Product`, usaremos `__uuid`.

3. En Python **los getter y los setter usan una sintaxis espcial** con los decoradores que hemos visto en clase. Así pues, cuando vayas a implementar el método `get_name` de `Product`, por ejemplo, lo que harás será lo siguiente:

``` python
@property
def name(self) -> str:
	return self.__name
```

**Importante**: no olvides que, en Python, cuando accedas a un atributo dentro de la clase tienes que anteponer el *keyword* `self`. Por ejemplo, en `Product` cuando vayas a usar el atribut `uuid` lo harás así: `self.__uuid`. Te recuerdo que `self` referencia al objeto o instancia concreta.

**No olvides**: sobreescribir los métodos `__str__` y `__repr__` de todos las clases que escribas. Tu "yo" del futuro acabará agradeciéndoselo a tu "yo" del presente :D
