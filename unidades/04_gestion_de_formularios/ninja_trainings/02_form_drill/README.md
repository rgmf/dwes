# Descripción
En este Ninja Training te propongo la realización de una serie de sitios web con Python + WSGI en el que tendrás que manejar formularios: recibirlos, limpiar campos y validarlos. Los tienes que hacer desde 0, desde la hoja en blanco.

# 1.- Suma de dos números
Crea un sitio web con un formulario de dos campos en los que el usuario escriba dos números, uno en cada campo, y al enviar el formulario se devuelva dicho formulario rellenado junto a la suma de los dos números.

Aquí tienes que validar que lo que el usuario ha introducido en los campos sea números.

# 2.- Calculadora de dos números
Mejora el ejercicio anterior convirtiéndolo en una calculadora.

Ahora, el formulario constará de:

- Un campo de texto para el primero operando.
- Otro campo de texto para el segundo operando.
- Una lista desplegable con las opciones: **Sumar**, **Restar**, **Multiplicar** y **Dividir** (`select` con varios `option`).

Así, dependiendo del valor del `select` tendrás que sumar, restar, multiplicar o dividir los números de los campos de texto.

Tienes que validar que lleguen números en los campos de texto y que la opción del `select` sea una de las cuatro indicadas.

# 3.- Traductor
Crea un traductor del español al inglés con 10 palabras que elijas tú.

El traductor consistirá en un formulario con un `select` en el que el usuario podrá elegir entre esas 10 palabras a tu elección y, cuando el usuario elija una opción y envie el formulario tendrás que devolver la misma página web con el formulario rellenado y la traducción de esa palabra al inglés.

Aquí tendrás que validar que la palabra que nos llega vía formulario sea una de las 10.

Ayuda: crea un diccionario, como este, pero con 10 palabras, de donde sacarás la información:

``` python
WORDS: dict[str, str] = {
	"Hola": "Hello",
	"Adiós": "Bye",
	"Perro": "Dog",
	"Gato": "Cat"
}
```
