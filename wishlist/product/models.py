from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField(max_length=300, null=False, blank=True)
    price = models.FloatField()
    link = models.CharField(max_length=500, null=False, blank=False)
    # img = models.ImageField()

    def __str__(self):
        return self.title
    