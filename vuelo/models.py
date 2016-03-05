from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vuelo(models.Model):
	name = models.CharField(max_length=255)
	time = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	destiny = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)