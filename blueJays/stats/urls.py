from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team/<int:pk>', views.team, name="team"),
    path('player/<int:pk>', views.player, name="player"),
]