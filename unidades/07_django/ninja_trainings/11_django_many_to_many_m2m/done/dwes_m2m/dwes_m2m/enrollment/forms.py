from django import forms

from .models import Subject, Student, Enrollment


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "age"]


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["student", "morning_session"]
