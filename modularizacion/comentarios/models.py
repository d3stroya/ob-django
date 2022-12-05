from django.db import models
from django.forms import DateField

class Comment(models.Model):
    # Definimos los atributos de la clase
    name = models.CharField(max_length=250, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)

    # Si ya hemos migrado los datos previamente, debemos
    # establecer un valor por defecto
    # o indicar que el campo puede ser nulo
    # Si no lo hacemos directamente, nos lo indicará en la terminal
    signature = models.CharField(max_length=10, default="mysignature")

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=True)
    alias = models.CharField(max_length=20, null=False, unique=True)
    email = models.CharField(max_length=30, unique=True, null=False)
    description = models.TextField(max_length=3000, default="Hey there!", null=False)

    def __str__(self):
        return self.alias

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.TextField(max_length=10000, null=False)
