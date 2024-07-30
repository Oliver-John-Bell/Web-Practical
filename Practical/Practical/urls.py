# main urls.py (e.g., project_name/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practical3/', include('Practical3.urls')),
    path('practical4/', include('Practical4.urls')),
    path('practical5/', include('Practical5.urls')),
    path('practical6/', include('Practical6.urls')),
    path('practical7/', include('Practical7.urls')),
    path('practical8/', include('Practical8.urls')),
    path('practical9/', include('Practical9.urls')),
]
