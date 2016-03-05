from django.contrib import admin
from .models import Vuelo, Favorite

# Register your models here.
@admin.register(Vuelo)

class AdminVuelo(admin.ModelAdmin):
	list_display = ('name', 'destiny', 'time', 'price',)
	list_filter = ('price', 'destiny',)
	
@admin.register(Favorite)

class AdminFavorite(admin.ModelAdmin):
	list_display = ('user', 'vuelo',)
	list_filter = ('user', 'vuelo',)