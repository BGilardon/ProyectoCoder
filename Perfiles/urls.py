from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', editar_perfil, name='editar_perfil')

]