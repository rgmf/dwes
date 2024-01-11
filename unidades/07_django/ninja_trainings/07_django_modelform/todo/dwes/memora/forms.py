from django import forms


class NoteForm(forms.Form):
    note = forms.CharField(
        label="Escribe la nota o recordatorio",
        widget=forms.Textarea(attrs={"rows": "5"})
    )
    label = forms.CharField(label="Etiqueta", max_length=20)
