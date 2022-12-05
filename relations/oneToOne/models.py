from django.db import models

# Vamos a modelar un lugar y un restaurante con una relación uno a uno
# Modelamos el lugar
class Place(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Modelamos el restaurante
class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    numEmployees = models.IntegerField(default=1)

    def __str__(self):
        # Cuando establecemos una realación entre clases, p
        # #odemos acceder a los atributos de la clase relacionada 
        # #(en este caso, Place; puedo obtener el nombre).
        return self.place.name

    
