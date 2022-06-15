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

def Fam(request):
     familiares = Familiar()
     l_nombre = [x.nombre for x in Familiar.objects.all()]
     l_edad = [x.edad for x in Familiar.objects.all()]
     l_fecha = [x.FechDeNac for x in Familiar.objects.all()]

     Html=f'''
     <html>
     <body>
        <p> Nombres: {str(l_nombre)} </p>
        <p> Edades:  {str(l_edad)} </p>
        <p> Fecha de nacimiento: {l_fecha} </p>

     </body>
     </html>
     '''
     def lista():
          for i in range(len(l_nombre)):
               nombre = l_nombre[i]
               edad = l_edad[i]
               fecha = l_fecha[i]
               return f'nombre: {nombre}, edad: {edad}, FechaDeNacimiento: {fecha}'

     Html2 = f'''
     <html>
     <body>
        <p> Nombres: {lista()} </p>
     </body>
     </html>
     '''

     return HttpResponse(Html)

def fam(request):

   with open(r"C:\Users\bauti\OneDrive\Escritorio\Coder\Django\MVT Bautista Gilardon\MVT\MVT\plantillas\template2.html") as miHtml:
      plantilla=Template(miHtml.read())
   
   l_nombre = [x.nombre for x in Familiar.objects.all()]
   l_edad = [x.edad for x in Familiar.objects.all()]
   l_fecha = [x.FechDeNac for x in Familiar.objects.all()]
   indice = range(len(l_nombre))

   dic = {'miNombre':'Bautista', 'miEdad':20,'l_nombres':l_nombre, 'l_edad':l_edad, 'l_fecha':l_fecha, 'indice':indice}

   miContexto=Context(dic)
   
   doc=plantilla.render(miContexto)
   
   return HttpResponse(doc)


