from django.db import models

# Create your models here.

class Manager(models.Model):
	name = models.CharField(max_length=88)
	email = models.EmailField(max_length=88)
	age = models.IntegerField()
	city = models.CharField(max_length=88)