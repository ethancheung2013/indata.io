from django.db import models

# Create your models here.
class User(models.Model):
	firstname		= models.CharField(max_length=100)
	lastname		= models.CharField(max_length=100)
	email			= models.CharField(max_length=150)
	comment			= models.CharField(max_length=5000) 