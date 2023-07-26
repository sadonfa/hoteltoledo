
from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.rooms, name='rooms'),
    path('habitacion/<int:id>/', views.room, name='room'),
]
