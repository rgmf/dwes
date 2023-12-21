from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola Mundo! Estás en Memora, la aplicación definitiva.")
