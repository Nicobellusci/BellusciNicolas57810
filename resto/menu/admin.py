from django.contrib import admin
from menu.models import *

#_____Modelos
class EntradasAdmin(admin.ModelAdmin): #Genero la clase EntradasAdmin que eredad de admin.modelsAdmin para generar las columnas nombre e ingredientes en el panel de vista admin.
    list_display = ("nombre", "ingredientes")

class BurgerAdmin(admin.ModelAdmin): #Genero la clase BurgerAdmin que eredad de admin.modelsAdmin para generar las columnas nombre e ingredientes en el panel de vista admin.
    list_display = ("nombre", "ingredientes")

class PizzaAdmin(admin.ModelAdmin): #Genero la clase PizzaAdmin que eredad de admin.modelsAdmin para generar las columnas nombre e ingredientes en el panel de vista admin.
    list_display = ("nombre", "ingredientes")

class EmpanadasAdmin(admin.ModelAdmin): #Genero la clase EmpanadasAdmin que eredad de admin.modelsAdmin para generar las columnas nombre e ingredientes en el panel de vista admin.
    list_display = ("nombre", "ingredientes")


#_____Admin
admin.site.register(Entradas, EntradasAdmin) #agrego la clas EntradasAdmin de arriba.
admin.site.register(Burger, BurgerAdmin) #agrego la clas EntradasAdmin de arriba.
admin.site.register(Pizza, PizzaAdmin) #agrego la clas EntradasAdmin de arriba.
admin.site.register(Empanadas, EmpanadasAdmin) #agrego la clas EntradasAdmin de arriba.
