from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/notes/user_<id>/<filename>
    return f"notes/user_{instance.user.id}/{filename}"


class Note(models.Model):
    note = models.TextField(verbose_name="Nota o recordatorio")
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="notes/", null=True, blank=True)
