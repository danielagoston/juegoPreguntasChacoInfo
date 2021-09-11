
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.usuarios.urls')), 
    path('usuarios/', include('django.contrib.auth.urls')), 
    path('', include('apps.pages.urls')), 
    path('partidas/', include('apps.juego.urls')), 
]
