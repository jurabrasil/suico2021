from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('jogos/', views.jogos, name='jogos'),
        path('placar_jogos/', views.placar_jogos, name='placar_jogos'),
        path('lista_jogos/', views.lista, name='lista'),
]