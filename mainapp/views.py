from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html',{
        'title': 'Inicio'
    })

def planes(request):
    return render(request, 'planes.html',{
        'title': 'Plantes'
    })

def gallery(request):
    return render(request, 'gallery.html',{
        'title': 'Galeria'
    })