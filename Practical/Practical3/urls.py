# Practical3/urls.py
from django.urls import path
from . import views

app_name = 'Practical3'

urlpatterns = [
    path('counting-game/<int:number>/', views.counting_game, name='counting_game'),
    path('download-stars/<int:number>/', views.download_stars, name='download_stars'),
]
