from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cars', views.cars, name='cars'),
    path('rent', views.rent, name='rent')
]