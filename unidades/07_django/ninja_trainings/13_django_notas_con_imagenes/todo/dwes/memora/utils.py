from os.path import join

from django.conf import settings


def handle_upload_file(name, f):
    extension = f.name.split(".")[-1]
    name_and_ext = name + "." + extension

    image_folder = join(settings.MEDIA_ROOT, "img")

    complete_path = join(image_folder, name_and_ext)

    with open(complete_path, "wb+") as fd:
        for chunk in f.chunks():
            fd.write(chunk)
