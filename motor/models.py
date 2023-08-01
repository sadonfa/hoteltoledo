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
    name = models.CharField(max_length=100, verbose_name="Nombre")
    amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Cantidad")
    date_start = models.DateField(verbose_name="Fecha Inicial")
    date_end = models.DateField(verbose_name="Fecha Final")
    disponible = models.BooleanField(verbose_name="Disponible")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    def __str__(self):
        return f"{self.name}"
