from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .models import Note, Category
from .forms import NoteForm


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


def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data["note"]
            label = form.cleaned_data["label"]
            category = Category.objects.filter(name=label).first()
            if not category:
                category = Category(name=label)
                category.save()
            note_object = Note(note=note, category=category, pub_date=timezone.now())
            note_object.save()
            return HttpResponseRedirect("/memora/notes/")
    else:
        form = NoteForm()

    return render(request, "memora/note_form.html", {"form": form})
