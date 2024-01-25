from django.urls import path

from . import views

app_name = "enrollment"

urlpatterns = [
    path("", views.index, name="index"),

    path("subjects/list/", views.subject_list, name="subject_list"),
    path("subjects/<int:id>/detail/", views.subject_detail, name="subject_detail"),
    path("subjects/create/", views.subject_create, name="subject_create"),
    path("subjects/<int:id>/enroll/student/", views.subject_enroll_student, name="subject_enroll_student"),

    path("students/create/", views.student_create, name="student_create"),
]
