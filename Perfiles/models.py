from django.db import models

# Create your models here.

class Perfil(models.Model):
    imagen      = models.ImageField(null=True, blank=True)
    nickname    = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    linkWeb     = models.URLField(null=True, blank=True)
    email       = models.EmailField(null=True, blank=True)
    pasword     = models.CharField(max_length=20)






