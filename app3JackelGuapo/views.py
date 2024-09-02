from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de app3JACK-EL-GUAPO</h1>")

def texto(request):
    return HttpResponse("<h1>Soy un TEXTO DE JACK EL GUAPO 1</h1>")
    return HttpResponse(html)
# Create your views here.
