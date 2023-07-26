from django.shortcuts import render
from rooms.models import Rooms
# Create your views here.

def home(request):
    rooms = Rooms.objects.all()
    
    return render(request, 'home.html',{
        'title': 'Inicio',
        'rooms': rooms
    })

def planes(request):
    return render(request, 'planes.html',{
        'title': 'Plantes'
    })

def gallery(request):
    return render(request, 'gallery.html',{
        'title': 'Galeria'
    })