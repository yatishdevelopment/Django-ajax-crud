from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50,default="Black")
    ram = models.CharField(max_length=50,default="2 GB")
    price = models.IntegerField(default=10000)