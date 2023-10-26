from templates import render_template


def home(environ: dict) -> str:
    return render_template("views/home.html")


def python(environ: dict) -> str:
    return render_template("views/python.html")


def java(environ: dict) -> str:
    return render_template("views/java.html")
