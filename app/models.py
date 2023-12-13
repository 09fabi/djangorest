from django.db import models

# Create your models here.

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    curso = models.CharField(max_length=20)
    promedio = models.DecimalField(max_digits=4, decimal_places=2)