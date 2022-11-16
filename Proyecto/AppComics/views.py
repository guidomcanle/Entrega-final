from django.shortcuts import render
from .models import *
from .forms import *

from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, 'AppComics/static/AppComics/index.html')

def comics(request):

    return render(request, 'AppComics/templates/AppComics/comics.html')

# Agregar objetos

def agregar_comics(request):

    if request.method == 'POST':
        miForm = ComicsFormulario(request.POST)
        print(miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data

            comic = Comics (titulo = info['titulo'], guionista = info['guionista'], dibujante = info['dibujante'], otros_artistas = info['otros_artistas'], editorial = info['editorial'])
            comic.save()

            return render(request, 'AppComics/templates/AppComics/agregar_comics.html',{"miForm":miForm})

    else:
        miForm = ComicsFormulario()

    return render(request, 'AppComics/templates/AppComics/agregar_comics.html',{"miForm":miForm})


def agregar_guionistas(request):

    if request.method == 'POST':
        miForm = GuionistasFormulario(request.POST)
        print(miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data

            guionista = Guionista (nombre = info['nombre'], apellido = info['apellido'])
            guionista.save()

            return render(request, 'AppComics/templates/AppComics/agregar_guionistas.html',{"miForm":miForm})

    else:
        miForm = GuionistasFormulario()

    return render(request, 'AppComics/templates/AppComics/agregar_guionistas.html',{"miForm":miForm})

def agregar_dibujantes(request):

    if request.method == 'POST':
        miForm = DibujantesFormulario(request.POST)
        print(miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data

            dibujante = Dibujante (nombre = info['nombre'], apellido = info['apellido'])
            dibujante.save()

            return render(request, 'AppComics/templates/AppComics/agregar_dibujantes.html',{"miForm":miForm})

    else:
        miForm = DibujantesFormulario()

    return render(request, 'AppComics/templates/AppComics/agregar_dibujantes.html',{"miForm":miForm})

def agregar_editoriales(request):

    if request.method == 'POST':
        miForm = EditorialesFormulario(request.POST)
        print(miForm)
        if miForm.is_valid:
            info = miForm.cleaned_data

            editorial = Editorial (nombre = info['nombre'], país = info['país'])
            editorial.save()

            return render(request, 'AppComics/templates/AppComics/agregar_editoriales.html', {"miForm":miForm})

    else:
        miForm = EditorialesFormulario()

    return render(request, 'AppComics/templates/AppComics/agregar_editoriales.html',{"miForm":miForm})

# Buscar objetos


def buscar_comics(request):

    return render(request, 'AppComics/templates/AppComics/buscar_comics.html')

def buscar(request):

    if request.GET['titulo']:

        titulo = request.GET['titulo']
        comics = Comics.objects.filter(titulo__icontains=titulo)

        return render(request, "AppComics/templates/AppComics/resultados_busqueda.html", {"comics":comics, "titulo":titulo})
    
    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
