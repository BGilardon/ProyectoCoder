from django.contrib import admin
from .models import *

# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    list_display    = ('nickname', 'email')
    search_fields   = ('nickname', 'email')


admin.site.register(Perfil, PerfilAdmin)