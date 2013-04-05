from django.db import models

# Create your models here.

class producto(models.Model):
	nombre = models.CharField(max_length = 100)
	cantidad = models.IntegerField()
	precio = models.FloatField()

