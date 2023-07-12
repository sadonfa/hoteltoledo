from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Rooms(models.Model):

    title =  models.CharField(max_length=100, verbose_name="Titulo")
    description = RichTextField(verbose_name="Descripcion")
    image = models.ImageField(default="null", upload_to="rooms", verbose_name="Imagen")
    cash = models.CharField(max_length=100, verbose_name="Precios")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado" )
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return f"{self.title}"