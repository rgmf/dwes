from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Note(models.Model):
    note = models.TextField()
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
