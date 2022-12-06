from django.db import models

class Salary(models.Model):
    amount = models.IntegerField(blank=False, null=False)
    extra_dic = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)

    def __str__(self):
        return self.amount

class Job(models.Model):
    title = models.CharField(max_length=15, blank=False, null=False)
    description = models.TextField()

    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Country(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    country_code = models.CharField(max_length=3, blank=False, null=False)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Factory(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=20, blank=False, null=False)
    zip_code = models.CharField(max_length=10, blank=False, null=False)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    dni = models.CharField(max_length=7, blank=False, null=False)
    first_name = models.CharField(max_length=10, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return self.dni    
    

    
