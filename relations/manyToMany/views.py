from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):
    # Creamos los objetos por separado y los guardamos,
    # porque la tabla de relaciones necesita los id de los objetos.
    # Si no están guardados, no hay id para relacionar.
    article1 = Article(headline='Artículo 1')
    article1.save()
    article2 = Article(headline='Artículo 2')
    article2.save()
    article3 = Article(headline='Artículo 3')
    article3.save()

    publication1 = Publication(title='Publicación 1')
    publication1.save()
    publication2 = Publication(title='Publicación 2')
    publication2.save()
    publication3 = Publication(title='Publicación 3')
    publication3.save()
    publication4 = Publication(title='Publicación 4')
    publication4.save()
    publication5 = Publication(title='Publicación 5')
    publication5.save()
    publication6 = Publication(title='Publicación 6')
    publication6.save()
    publication7 = Publication(title='Publicación 7')
    publication7.save()

    # # Luego establecemos las relaciones con [clase].add()
    article1.publications.add(publication1)
    article1.publications.add(publication2)
    article1.publications.add(publication3)

    article2.publications.add(publication4)
    article2.publications.add(publication5)
    article2.publications.add(publication6)

    article3.publications.add(publication7)

    # Obtenemos todas las publicaciones del artículo 1
    result1 = article1.publications.all()

    # Obtenemos todos los artículos que están relacionados con la publicación 1 con article_set
    pub1 = Publication.objects.get(id=1)
    result2 = pub1.article_set.all()

    # Eliminar una relación
    article1.publications.remove(publication2)

    return HttpResponse(result1)