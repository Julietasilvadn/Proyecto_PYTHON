from django.db import models
from django.contrib.auth.models import User


class Mascota(models.Model):
    nombre= models.CharField(max_length=30)
    nacimiento= models.DateTimeField()
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Nacimiento: {self.nacimiento}"


class Reserva(models.Model):
    mascota= models.CharField(max_length=40)
    dia= models.CharField(max_length=10)

    def __str__(self):
        return f"Mascota: {self.mascota} - Dia: {self.dia}"

class Avatar(models.Model):
    user = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} tiene una imagen cargada"