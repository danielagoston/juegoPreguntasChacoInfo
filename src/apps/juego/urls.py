from django.urls import path
from . import views

urlpatterns = [
	path('partidas/', views.ListaDePartidas.as_view(), name='partidas'),
	path('partidas/nueva-partida/', views.CrearPartida.as_view(), name='nueva_partida'),    
	path('partida/<int:pk>/', views.JugandoPartida.as_view(), name='juego'),
]