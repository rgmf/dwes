from django.http import Http404, HttpResponse
from django.shortcuts import render


from . models import Note


def index(request):
    return HttpResponse("Hola Mundo! Estás en Memora, la aplicación definitiva.")


def notes(request):
    notes = Note.objects.all()
    return render(request, "memora/list.html", {"notes": notes})


def detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")

    return render(request, "memora/detail.html", {"note": note})
