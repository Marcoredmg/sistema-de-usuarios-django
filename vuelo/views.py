from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Vuelo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class VueloList(ListView):
	model = Vuelo