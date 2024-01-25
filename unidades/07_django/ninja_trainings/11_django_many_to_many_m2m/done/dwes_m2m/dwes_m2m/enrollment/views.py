from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.utils import IntegrityError

from .models import Subject, Enrollment
from .forms import SubjectForm, StudentForm, EnrollmentForm


def index(request):
    return render(request, "enrollment/index.html")


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "enrollment/subject_list.html", {"subjects": subjects})


def subject_detail(request, id):
    subject = get_object_or_404(Subject, id=id)
    return render(request, "enrollment/subject_detail.html", {"subject": subject})


def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("enrollment:subject_list"))
    else:
        form = SubjectForm()

    return render(
        request,
        "enrollment/form.html",
        {"form": form, "header": "Añadir Materia"}
    )


def subject_enroll_student(request, id):
    subject = get_object_or_404(Subject, id=id)
    message = ""

    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            try:
                Enrollment.objects.create(
                    student=form.cleaned_data["student"],
                    subject=subject,
                    morning_session=form.cleaned_data["morning_session"]
                )
                return redirect(reverse("enrollment:subject_detail", args=(id,)))
            except IntegrityError:
                message = "Ya existe el alumno en el curo"
    else:
        form = EnrollmentForm()

    return render(
        request,
        "enrollment/form.html",
        {"form": form, "header": "Matricular Alumnado", "message": message}
    )


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("enrollment:subject_list"))
    else:
        form = StudentForm()

    return render(
        request,
        "enrollment/form.html",
        {"form": form, "header": "Añadir Alumnado"}
    )
