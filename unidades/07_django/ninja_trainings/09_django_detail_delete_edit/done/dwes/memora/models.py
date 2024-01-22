from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Note(models.Model):
    note = models.TextField(verbose_name="Nota o recordatorio")
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)
