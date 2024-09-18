from django.urls import path
from Meteo import views

app_name = 'Meteo'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]