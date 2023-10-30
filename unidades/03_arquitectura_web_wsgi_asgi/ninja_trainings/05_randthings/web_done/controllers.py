from random import randint
from urllib.parse import parse_qs

from templates import render_template


def home(environ: dict) -> str:
    return render_template("views/home.html")


def random_number(environ: dict) -> str:
    qs_dict: dict[str, str] = parse_qs(environ["QUERY_STRING"])
    from_number: int = 0
    to_number: int = 1_000_000

    # Obtenemos los números "from" y "to" de los query parameters.
    if "from" in qs_dict and qs_dict["from"][0].isalnum():
        from_number = int(qs_dict["from"][0])

    if "to" in qs_dict and qs_dict["to"][0].isalnum():
        to_number = int(qs_dict["to"][0])

    # Generamos el número al azar.
    random_number: int = randint(from_number, to_number)

    # Generamos el template y lo devolvemos.
    context: dict[str, str] = {"number": str(random_number)}
    return render_template("views/number.html", context)


def random_sentence(environ: dict) -> str:
    sentences: list[str] = []

    # Cargamos las frases del fichero de texto.
    with open("assets/sentences.txt", "r") as file_object:
        while line := file_object.readline():
            sentences.append(line[:-1])

    # Elegimos una frase al azar.
    if len(sentences) > 0:
        sentence: str = sentences[randint(0, len(sentences) - 1)]
    else:
        sentence: str = ""

    # Generamos el template y lo devolvemos.
    context: dict[str, str] = {"sentence": sentence}
    return render_template("views/sentence.html", context)
