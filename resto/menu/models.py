from django.db import models
from django.contrib.auth.models import User


#______Modelos del menu:

class Entradas(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["nombre"] #ordena ascendente por nombre los items dentro del panel de adminitracion.
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
    
    def __str__(self):
	    return f"{self.nombre}"
   
class Burger(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=100)
    tipo_pan = models.CharField(max_length=50)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Burger"
        verbose_name_plural = "Burgers"

    def __str__(self):
       return f"{self.nombre}"

class Pizza(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["nombre"]
        verbose_name = "Pizzas"
        verbose_name_plural = "Pizzas"    

    def __str__(self):
	    return f"{self.nombre}"
          
class Empanadas(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=100)
    coccion = models.CharField(max_length=50)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Empanada"
        verbose_name_plural = "Empanadas"

    def __str__(self):
	    return f"{self.nombre}"
    
#______AVATAR_________________________________________________________________________________________
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

#_____________________________________________________________________________________________________
     