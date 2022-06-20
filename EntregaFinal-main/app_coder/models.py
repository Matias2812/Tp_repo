from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    nacimiento = models.DateField()

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    legajo = models.IntegerField()
    fecha_alta= models.DateTimeField()
    dicta_materia= models.CharField(max_length=20)
    email = models.CharField(max_length=40)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    