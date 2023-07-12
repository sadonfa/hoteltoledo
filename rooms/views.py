from django.shortcuts import render
from .models import Rooms

# Create your views here.

def rooms(request):

    rooms = Rooms.objects.all()

    return render(request, 'rooms.html',{
        'title': 'Habitaciones',
        'rooms': rooms
    })