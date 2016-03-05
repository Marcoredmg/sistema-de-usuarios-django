from __future__ import unicode_literals
from django.contrib.auth.models import User
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

class Favorite(models.Model):
	user = models.ForeignKey(User)
	vuelo = models.ForeignKey(Vuelo)

	class Meta:
		verbose_name= 'Favorite'
		verbose_name_plural = 'Favorites'

	def __str__(self):
		return '%s %s' % (self.user.name, self.vuelo.name)