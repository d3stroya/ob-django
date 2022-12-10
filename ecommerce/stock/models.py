from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    short_description = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    stock = models.IntegerField(default=20)

    def __str__(self):
        return self.name
    