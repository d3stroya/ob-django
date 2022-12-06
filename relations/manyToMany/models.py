from django.db import models

# Modelamos una clase Publication y otra Article. Tendra una relación muchos a muchos
class Publication(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
    
    