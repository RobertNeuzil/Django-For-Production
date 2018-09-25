from django.db import models

class Blog_Post(models.Model):

	author = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	date = models.CharField(max_length=100)

	def __str__(self):
		return self.title



# Create your models here.
