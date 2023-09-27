"""Estadísticas de frases.

Aquí tienes un programa incompleto con un menú en el que puedes realizar las
siguientes acciones:

- Añadir frases al sistema
- Mostrar frases
- Salir

Las frases son almacenadas en una lista de diccionarios donde cada diccionario
contiene la información y estadísticas de una frase. Esta es la estructura de
los diccionarios, las claves que debe tener y los tipos de sus valores:

- "sentence"   -> str
- "language"   -> str
- "vowels"     -> int
- "consonants" -> int
- "others"     -> int

Por ejemplo, imagina que tu programa ha pedido al usuario que escriba una
frase y ha escrito: "Hola Mundo!". Y luego, le ha pedido que indique el
lenguaje que ha usado empleando la abreviatura de dicho idioma y ha escrito
"es". El programa creará el diccionario y lo meterá a la lista:
[
    {
        "sentence": "Hola Mundo!",
        "language": "es",
        "vowels": 4,
        "consonants": 5,
        "others": 2
    }
]

Ahora, imagina que el usuario escribe "Hello World!" y "en" para idioma. El
programa creará el diccionario correspondiente y lo mete en la lista, con lo
que la lista quedará así:
[
    {
        "sentence": "Hola Mundo!",
        "language": "es",
        "vowels": 4,
        "consonants": 5,
        "others": 2
    },
    {
        "sentence": "Hello World!",
        "language": "en",
        "vowels": 3,
        "consonants": 7,
        "others": 2
    }
]

La base del programa ya la he escrito yo, donde ves que hay un menú y tienes
que completarlo.

En este program podrás usar todas las funciones de Python que consideres
oportuno.

Tienes comentarios TODO en el código para lo completos pero antes intentan
comprender el código que ya hay escrito. Todo comienza al final, donde verás
que se llama a una funición llamada `main` que mantiene el estado del programa
y gestiona el menú de opciones.
"""


def welcome() -> None:
    print("Bienvenid@s a frases con estadísticas: ")
    print("------------------------------------------------")
    print()
    print("Elige una opción del menú: ")


def show_menu_and_ask_option() -> int:
    is_option_valid: bool = False

    while not is_option_valid:
        print("MENÚ")
        print("1.- Añadir frase")
        print("2.- Mostrar todas las frases")
        print("0.- Salir")
        option: int = int(input("Elige una opción: "))
        is_option_valid = True if 0 <= option <= 2 else False

    return option


def add_sentence(sentence_list: list[dict[str, str | int]]) -> None:
    """TODO Just do it.

    Ya sabes lo que tienes que hacer (te lo he indicado en un comentario muy
    largo y denso arriba, al principio del fichero): pide una frase al usuario,
    genera el diccionario con la iformación y añádelo a la lista (parámetro).
    """
    pass


def show_sentences(sentence_list: list[dict[str, str | int]]) -> None:
    print()
    print(f"Hay {len(sentence_list)} frases")
    for sentence_info in sentence_list:
        print(sentence_info["sentence"])
    print()


def main() -> None:
    """Función principal del programa.

    Aquí empieza todo: encendemos las luces.

    Happy Hacking!
    """
    # Cuando empieza el programa, la lista de diccionarios está vacía.
    sentences: list[dict[str, str | int]] = []

    # Mostramos mensaje de bienvenida al programa.
    welcome()

    # Mientras el usuario no elija salir mostramos el menú y realizamos
    # la acción que solicita.
    while (option := show_menu_and_ask_option()) != 0:
        if option == 0:
            print("Hasta pronto!!!")
        elif option == 1:
            add_sentence(sentences)
        elif option == 2:
            show_sentences(sentences)


# Programa principal... llama a la función main para empezar todo.
main()
