from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Todo ok!")

def create(request):
    # Creamos un objeto de la clase Comment
    #comment = Comment(name="Franky", scrote=10, comment="Comentario de prueba")

    # Guardamos el objeto en base de datos
    #comment.save()

    # Otra forma de hacer lo mismo 
    comment = Comment.objects.create(name="Bridget")

    return HttpResponse("Ruta para crear modelos")

def delete(request):
    # Buscar el objeto que queremos borrar
    #comment = Comment.objects.get(id=1)

    # Borramos
    #comment.delete()

    # Otra forma de hacer lo mismo
    Comment.objects.filter(id=2).delete()

    return HttpResponse("Objeto borrado correctamente")