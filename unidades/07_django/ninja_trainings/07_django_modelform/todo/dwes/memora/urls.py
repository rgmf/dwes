from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("<int:note_id>/", views.detail, name="detail"),
    path("notes/create/", views.create_note, name="create_note")
]
