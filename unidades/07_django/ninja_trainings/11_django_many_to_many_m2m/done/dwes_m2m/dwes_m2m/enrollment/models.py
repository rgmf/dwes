from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.surname}, {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    students = models.ManyToManyField(
        Student,
        through="Enrollment"
    )


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrolled_date = models.DateField(auto_now_add=True)
    morning_session = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=(["student", "subject"]),
                name="subject_student_enrollment"
            )
        ]
