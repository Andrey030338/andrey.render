from django.db import models

# Create your models here.
class Project(models.Model):
    Titulo = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Tecnologia = models.CharField(max_length=200)
    F_Creacion = models.DateTimeField(auto_now_add=True)