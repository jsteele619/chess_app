from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('chess_stats', views.chess_stats, name='chess_stats')]
