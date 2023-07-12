from django.db import models

# Create your models here.


class Rooms(models.Model):
    id_rooms = models.CharField(max_length=50, verbose_name="Id")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    # class Meta:
    #     verbose_name = "Habitacion"
    #     verbose_name_plural = "Habitaciones"

    def __str__(self): 
        return f"{self.id_rooms}"


class Plan(models.Model):
    id_plan = models.CharField(max_length=50, verbose_name="Id")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    # class Meta:
    #     verbose_name = "Plan"
    #     verbose_name_plural = "Planes"

    def __str__(self):
        return f"{self.id_plan}"


class Disponibilidad(models.Model):
    checkin = models.DateField(verbose_name="start")
    checkout = models.DateField(verbose_name="end")
    rooms = models.ManyToManyField(Rooms, verbose_name="Habitacion")
    plan = models.ManyToManyField(Plan, verbose_name="Plan")
    disponible = models.BooleanField(verbose_name="Disponibilidad")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    def __str__(self):
        return f"{self.checkin}"
