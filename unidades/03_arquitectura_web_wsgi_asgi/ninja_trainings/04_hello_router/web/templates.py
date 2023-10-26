def render_template(template_name: str, context: dict = {}) -> str:
    """Renderiza un fichero HTML.

    Básicamente lo que hace esta función es cargar la página web
    `template_name` en un string de Python e interpola los valores del
    `context` si los hubiera.

    :template_name str: ruta del fichero HTML a renderizar.
    :context dict: el diccionario con los valores a interpolar.

    :return: un string con el HTML y los valores interpolados.
    """
    html_str = ""
    with open(template_name, "r") as f:
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str
