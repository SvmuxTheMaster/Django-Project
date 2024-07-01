from django.db import models


# Create your models here.


class Servicio(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to = 'servicios')
    unidades = models.IntegerField()
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        verbose_name = "control de productos"
        verbose_name_plural = "administrador de productos"

    def __str__(self):
        return self.titulo
