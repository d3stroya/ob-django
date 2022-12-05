from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    # creamos objetos de las clases Reporter y Article
    rep1 = Reporter(first_name='Franky', last_name='Doyle', email='fdoyle@ww.com')
    rep1.save()

    art1 = Article(headline='This is article 1', publication_date=date(2022,1,2), reporter=rep1)
    art1.save()
    art2 = Article(headline='This is article 2', publication_date=date(2022,2,3), reporter=rep1)
    art2.save()
    art3 = Article(headline='This is article 3', publication_date=date(2021,4,5), reporter=rep1)
    art3.save()
    art4 = Article(headline='This is article 4', publication_date=date(2018,6,7), reporter=rep1)
    art4.save()

    # Con la realción muchos a uno podemos acceder a los datos del reportero que ha escrito el artículo
    result1 = art1.reporter.first_name

    # Acceder a los datos de los artículos que ha escrito el reportero
    result2 = rep1.article_set.all()

    # Podemos filtrar resultados igual que en las consultas
    result3 = rep1.article_set.filter(headline='This is article 4')

    # Y establecer un conteo
    result4 = rep1.article_set.count()

    return HttpResponse(result4)