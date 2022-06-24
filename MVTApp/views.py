from django.shortcuts import render
from datetime import *
from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
from MVTApp.models import Familiar

# Create your views here.

def prueba(self):

   with open(r"C:\Users\bauti\OneDrive\Escritorio\Coder\Django\MVT Bautista Gilardon\MVT\MVT\plantillas\template1.html") as miHtml:
        plantilla=Template(miHtml.read())
   
   dic = {'n':'Bautista', 'e':[1,2,3]}

   miContexto=Context(dic)
   
   doc=plantilla.render(miContexto)
   
   return HttpResponse(doc)


# def fam(request):

#    with open(r"C:\Users\bauti\OneDrive\Escritorio\Code\Django\MVT Bautista Gilardon\MVT\MVT\plantillas\template2.html") as miHtml:
#       plantilla=Template(miHtml.read())
   
#    l_nombre = [x.nombre for x in Familiar.objects.all()]
#    l_edad = [x.edad for x in Familiar.objects.all()]
#    l_fecha = [x.FechDeNac for x in Familiar.objects.all()]
#    indice = range(len(l_nombre))

#    dic = {'miNombre':'Bautista', 'miEdad':20,'l_nombres':l_nombre, 'l_edad':l_edad, 'l_fecha':l_fecha, 'indice':indice}

#    miContexto=Context(dic)
   
#    doc=plantilla.render(miContexto)
   
#    return HttpResponse(doc)

def fam(request):
   
   familiar = Familiar.objects.all()

   return render(request, 'template2.html',{'familiar': familiar})


def inicio(request):
   pass

   return render(request, 'index.html')

def CrearFamiliar(request):
   
   if request.method == 'POST':

      familiar = Familiar(
         nombre=request.POST['Nombre'], 
         edad=request.POST['Edad'], 
         FechDeNac=request.POST['Fecha'])

      familiar.save()

   
   return render(request, 'CrearFamiliar.html')

