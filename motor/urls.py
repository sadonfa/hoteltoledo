from django.urls import path
from . import views

urlpatterns = [
    path('disponibilidad/', views.disponibilidad, name='dispon'),
]
