from .models import Vuelo
from django.views.generic import ListView

class VueloList(ListView):
	model = Vuelo