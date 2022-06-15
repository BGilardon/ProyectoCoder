from sys import maxsize
from time import timezone
from django.db import models
from datetime import datetime

# Create your models here.
class Familiar(models.Model):
    nombre      = models.CharField(max_length=40)
    edad        = models.IntegerField()
    FechDeNac   = models.DateField()