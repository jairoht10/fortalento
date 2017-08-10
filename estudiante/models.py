from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudiante(models.Model):

    nombre = models.CharField(max_length=100)

    apellido = models.CharField(max_length=100)

    user = models.ForeignKey(User)
