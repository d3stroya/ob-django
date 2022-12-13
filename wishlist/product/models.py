from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField(max_length=300, null=False, blank=True)
    price = models.FloatField()
    link = models.CharField(max_length=500, null=False, blank=False)
    img = models.CharField(max_length=300, null=False, blank=False, default='https://cdn.pixabay.com/photo/2017/11/14/00/57/christmas-2947257_960_720.jpg')

    def __str__(self):
        return self.title
    