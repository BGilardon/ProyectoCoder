from django.shortcuts import render
import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.



def editar_perfil(request):

    user = request.user # usuario con el que estamos loggueados

    if request.method == "POST":
        
        form = UserEditForm(request.POST) # cargamos datos llenados

        if form.is_valid():

            info = form.cleaned_data
            user.imagen         = info['imagen']
            user.nickname       = info['nickname']
            user.descripcion    = info['descripcion']
            user.linkWeb        = info['linkWeb']
            user.email          = info['email']
            user.password1      = info['password1']
            user.password2      = info['password2']
            # 

            user.save()

            return redirect("inicio")


    else:
        form = UserEditForm(initial={'imagen':user.email, 'nickname':user.nickname, 'descripcion':user.descripcion, 'linkWeb':user.linkWeb,'email':user.email, 'password1':user.password1, 'password2':user.password2})

    return render(request,"Perfil.html",{"form":form})