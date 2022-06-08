from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import loader
# Create your views here.


def inicio(request):

    return render(request , "plantillas.html" )



def cursos(request):
    cursos= Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada=287818)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} Camada: {curso.camada} "
    return HttpResponse(texto)


def estudiantes(request):

    return render(request , "estudiantes.html")


def contacto(request):

    return render(request , "contacto.html")


def entregables(request):

    return render(request , "entregables.html")


def profesores(request):

    return render(request , "profesores.html")



def curso_form(request):
     
    if request.method == "POST" :

        curso = Curso(nombre=request.POST['nombre'] , camada=request.POST['camada'])
        curso.save()
        return render(request , "formulario.html")

    return render(request , "formulario.html")