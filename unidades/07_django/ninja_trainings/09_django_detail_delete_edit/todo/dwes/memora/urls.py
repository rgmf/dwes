from django.urls import path

from . import views

app_name = "memora"

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("notes/<int:note_id>/", views.detail, name="detail"),
    path("notes/create/", views.create_note, name="create_note")
]
