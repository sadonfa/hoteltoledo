from django.db import models

# Create your models here.

class Booking(models.Model):

    name = models.CharField(max_length=200, verbose_name="Nombre")
    lastname = models.CharField(max_length=200, verbose_name="Apellidos")
    phone  = models.TextField(max_length=100, verbose_name="Nombre")
    mail = models.EmailField(max_length=200, verbose_name="Correo")
    contry  = models.CharField(max_length=200, verbose_name="Pais")
    city  = models.CharField(max_length=200, verbose_name="Ciudad")
    adults  = models.CharField(max_length=100, verbose_name="Adultos")
    childre  =models.CharField(max_length=100, verbose_name="Niños")
    checkin = models.CharField(max_length=100, verbose_name="Check-in")
    checkout = models.CharField(max_length=100, verbose_name="Check-Out")
    rooms = models.CharField(max_length=100, verbose_name="Habitaciones")
    cash = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Valor", default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="total", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")

    def __str__(self):
        return f'{self.name}' 
    
    def get_id_formateado(self):
        return str(self.pk).zfill(6)