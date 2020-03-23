from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('adventure/', views.adventure_games),
    path('action/', views.action_games),
    path('strategy/', views.strategy_games)
]
