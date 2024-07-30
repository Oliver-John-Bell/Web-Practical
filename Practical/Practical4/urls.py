# Practical4/urls.py
from django.urls import path
from . import views

app_name = 'Practical4'

urlpatterns = [
    path('studentform/', views.student_form, name='student_form'),
    path('viewdatabase/', views.view_database, name='view_database'),
]