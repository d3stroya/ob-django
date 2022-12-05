from django.shortcuts import render
from django.http import HttpResponse

# Importamos los modelos
from .models import Author, Entry

def queries(request):
    # Obtener todos los elementos
    allAuthors = Author.objects.all()

    # Obtener datos filtrados
    authorByEmail = Author.objects.filter(email="tthomas@example.org")
    authorById = Author.objects.filter(id=9)

    # Obtener un único objeto
    author = Author.objects.get(id=12)

    # Obtener los 10 primeros elementos
    tenAuthors = Author.objects.all()[:10]

    # Obtener los autores de 6 a 15 (con límite y offset)
    authorsOffset = Author.objects.all()[5:15]

    # Obtener todos los objetos ordenados
    authorsOrderedByEmail = Author.objects.all().order_by('email')

    # Obtener todos los autores con id <= 15; necesitamos un modificador del =, 
    # #porque no estamos usando un comparador, sino un asignador (=):
        # __lte: <= (lower than equals)
        # __gte: >= (grater than equals)
        # __lt: < (lower than)
        # __gt: > (greater than)
        # __contains
        # __exact
    authorsId15 = Author.objects.filter(id__lte=15)

    # Obtener todos los autores que contienen en su nombre la palabra one
    authorsWithOne = Author.objects.filter(name__contains='one')


    return render(
        request, 
        './posts/queries.html', 
        {
            'allAuthors': allAuthors, 
            'authorByEmail': authorByEmail,
            'authorById': authorById,
            'author': author,
            'tenAuthors': tenAuthors,
            'authorsOffset': authorsOffset,
            'authorsOrderedByEmail': authorsOrderedByEmail,
            'authorsId15': authorsId15,
            'authorsWithOne': authorsWithOne
        }
        )

def update(request):
    authorUpdate = Author.objects.get(id=1)

    # Modificamos el objeto
    authorUpdate.name = 'Franky'
    authorUpdate.email = 'fdoyle@ww.com'
    authorUpdate.save()

    return HttpResponse("Autor actualizado correctamente.")

