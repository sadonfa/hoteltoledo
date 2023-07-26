from django.shortcuts import render
from .models import Rooms

# Create your views here.

def rooms(request):

    rooms = Rooms.objects.all()

    return render(request, 'rooms.html',{
        'title': 'Habitaciones',
        'rooms': rooms
    })

def room(request, id):

    room = Rooms.objects.get(id=id)

    return render(request, 'room.html',{
        'title': 'Habitaciones',
        'room': room
    })