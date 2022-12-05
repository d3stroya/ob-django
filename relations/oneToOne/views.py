from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

def create(request):
    # Creamos objetos de la clase lugar y restaurante
    place1 = Place(name='Plaza redonda', address='calle Alcalá')
    place1.save()
    restaurant1 = Restaurant(place=place1, numEmployees=10)
    restaurant1.save()

    return HttpResponse(restaurant1.place.name)