from django.db import models

# Create your models here.

# PLANT NAME, SCIENTIFIC NAME, lOCAL/HYBRID, PRICE, AGE, PIC
class Plant(models.Model):
    plant_name = models.TextField(max_length=100)
    scientific_name= models.TextField(max_length=100)
    price = models.IntegerField(default=100)
    age = models.IntegerField()
    pic = models.ImageField(null=True)
    imported = models.BooleanField(default=False)