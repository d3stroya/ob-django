from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=10, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.first_name
    
