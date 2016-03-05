from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.VueloList.as_view(), name='listavuelo'),
]