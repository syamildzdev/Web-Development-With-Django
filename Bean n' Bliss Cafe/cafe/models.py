from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import 


class Beverage(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.name