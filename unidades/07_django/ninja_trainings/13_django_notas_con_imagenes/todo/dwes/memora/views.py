from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import NoteForm, UploadImageForm
from .utils import handle_upload_file


def index(request):
    return render(request, "memora/index.html")


def notes(request):
    notes = Note.objects.all()
    return render(request, "memora/list.html", {"notes": notes})


def detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")

    return render(request, "memora/detail.html", {"note": note})


@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.pub_date = timezone.now()
            note.save()
            return redirect(reverse("memora:notes"))
    else:
        form = NoteForm()

    return render(
        request,
        "memora/note_form.html",
        {"form": form, "action": reverse("memora:create_note")}
    )


def edit_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("La nota no existe")

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse("memora:notes"))
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "memora/note_form.html",
        {"form": form, "action": reverse("memora:edit_note", args=(note_id,))}
    )


def delete_note(request, note_id):
    try:
        Note.objects.get(id=note_id).delete()
    except Note.DoesNotExist:
        raise Http404("La nota no existe")

    return redirect(reverse("memora:notes"))


def upload_image(request):
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(form.cleaned_data["title"], request.FILES["image"])
            return redirect(reverse("memora:index"))
    else:
        form = UploadImageForm()

    return render(request, "memora/image_form.html", {"form": form})
