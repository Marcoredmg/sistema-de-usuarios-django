from django.contrib import admin
from .models import Vuelo
# Register your models here.
@admin.register(Vuelo)

class AdminVuelo(admin.ModelAdmin):
	list_display = ('name', 'destiny', 'time', 'price',)
	list_filter = ('price', 'destiny',)
