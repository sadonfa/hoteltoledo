from django.shortcuts import render, get_object_or_404
# from tours.models import  Tours
# from reserve.models import Reserver
from .models import Booking
from rooms.models import Rooms
from datetime import datetime

# Create your views here.

def check(request, id=False):
    # d_reserve = Reserver.objects.all()

    if id == False and request.method == 'POST':
        # det_booking = get_object_or_404(Reserver, pk=id)
        det_booking = {
            "name" : request.POST['name'],
            "cash": request.POST['value'],
            "origen" : request.POST['origen'],
            "destino": request.POST['destino'],
            "date" : request.POST['date'],
            "time": request.POST['time'],
            "opcion": "transporte"
        }
        
    else:
        print(id) 
        

        # print(tour.cash)
    return render(request, 'check.html',{
        'title': 'Informacion de reserva',
        'det_booking': det_booking,
        # 'd_reserve': d_reserve
    })

def det_booking(request):

    # tour = Tours.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname'] 
        phone  = request.POST['phone']
        mail = request.POST['mail']
        contry  = request.POST['contry']
        city  = request.POST['city']
        cash  = request.POST['cash']   
        adults  = request.POST['adults']
        childre  = request.POST['children']    
        checkin  = request.POST['checkin']   
        checkout  = request.POST['checkout']   
        rooms  = request.POST['rooms']   
        cupon  = request.POST['cupon']  
        year_children  = request.POST['year-children']  
       
        
        date_checkin = datetime.strptime(checkin, "%m/%d/%Y")
        date_checkout = datetime.strptime(checkout, "%m/%d/%Y")
        day_checkin = date_checkin.day
        day_checkout = date_checkout.day

        cant_noches =  int(day_checkout) - int(day_checkin)

        if int(year_children) >= 2:
            cash_childre = int(childre)* 50000
            # total_pagar = int(cash) + cash_childre 
        else:
            cash_childre = 0        

        if cupon == "TOLAGOS23":
            sub_total = int(cash) - ((int(cash) * 10 )/ 100)
            total_pagar = (int(sub_total) + cash_childre ) * cant_noches
        else:
            total_pagar =  (int(cash) + cash_childre ) * cant_noches

    booking = Booking(
        name = name,
        lastname = lastname,
        phone  = phone,
        mail = mail,
        contry  = contry,
        city  =  city,
        cash = cash,
        adults  =  adults,
        childre  = childre,
        rooms = rooms,
        checkin = checkin,
        checkout = checkout
    ) 

    booking.save()      
       

    return render(request, 'det_booking.html',{
        'title': 'Detalles de Reserva',  
        'booking': booking,
        'cash_childre': cash_childre,
        'total_pagar': total_pagar,
        'cant_noches': cant_noches
    })

def inf_booking(request, id):

    room = Rooms.objects.get(id=id)

    if request.method == 'POST':
        checkin = request.POST['checkin']
        checkout = request.POST['checkout'] 
        rooms  = request.POST['rooms']
        adults = request.POST['adults']
        children  = request.POST['children']
    else:
        print("No se puede validar la informacioin")
    
   
    return render(request, 'info_booking.html',{
        'checkin': checkin,
        'checkout': checkout,
        'rooms': rooms,
        'adults': adults,
        'children': children,
        # 'booking': booking,
        'room': room
    })