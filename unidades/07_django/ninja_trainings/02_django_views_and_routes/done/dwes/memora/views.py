from django.http import HttpResponse, Http404

from . models import Note


def index(request):
    return HttpResponse("Hola Mundo! Estás en Memora, la aplicación definitiva.")


def notes(request):
    html = """
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Listado de notas</h1>
        <ul>
            {ul_list}
        </ul>
    </body>
    </html>
    """

    notes = Note.objects.all()
    note_list_html = ""
    if notes:
        for note in notes:
            note_list_html += "<li>" + note.note + "</li>"
    else:
        note_list_html = "No hay notas"

    return HttpResponse(html.format(ul_list=note_list_html))


def detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")

    html = """
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Detalles de la nota</h1>
        <p>{note}</p>
        <small>{category></small>
    </body>
    </html>
    """
    return HttpResponse(html.format(note=note.note, category=note.category.name))
