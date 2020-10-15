from django.db import models

# Category, City
class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
