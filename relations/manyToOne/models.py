from django.db import models

# Creamos una clase Reportero y otra Artículos. Un reportero podrá tener muchos artículos
class Reporter(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Article(models.Model):
    headline = models.CharField(max_length=20)
    publication_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline
    