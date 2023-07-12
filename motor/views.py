from django.shortcuts import render
from .models import Disponibilidad

# Create your views here.

def disponibilidad(request):

    dispon = Disponibilidad.objects.all()

    return render(request, 'disponibilidad.html',{
        'disponibilidad': dispon
    })