from django.urls import path, include
from menu.views import *

# Class-Based Views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name="Home"),
    path('Acerca/', acerca, name="Acerca"),


#####---FORMULARIOS

    #_____ENTRADAS
    path('Entradas/', entradas, name="Entradas"),
    path('EntradasForm/', entradasForm, name="EntradasForm"), #resuelve entradasForm y la clave el name="EntradasForm" que podria poner en un href para referanciar este link.
    path('EntradasUpdate/<id_entrada>/', entradasUpdate, name="EntradasUpdate"), #creo el entradasUpdate y le agrego a la ruta el id
    path('EntradasDelete/<id_entrada>/', entradasDelete, name="EntradasDelete"),


    #_____PIZZAS
    path('Pizzas/', pizzas, name="Pizzas"),
    path('PizzasForm/', pizzasForm, name="PizzasForm"),
    path('PizzasUpdate/<id_pizza>/', pizzasUpdate, name="PizzasUpdate"),
    path('PizzasDelete/<id_pizza>/', pizzasDelete, name="PizzasDelete"),


    #_____BURGERS
    path('Burgers/', burgers, name="Burgers"),
    path('BurgersForm/', burgersForm, name="BurgersForm"),
    path('BurgersUpdate/<id_burger>/', burgersUpdate, name="BurgersUpdate"),
    path('BurgersDelete/<id_burger>/', burgersDelete, name="BurgersDelete"),


    #_____EMPANADAS
    path('Empanadas/', empanadas, name="Empanadas"),
    path('EmpanadasForm/', empanadasForm, name="EmpanadasForm"),
    path('EmpanadasUpdate/<id_empanada>/', empanadasUpdate, name="EmpanadasUpdate"),
    path('EmpanadasDelete/<id_empanada>/', empanadasDelete, name="EmpanadasDelete"),

    
    #_____BUSCAR
    path('buscarEntradas/', buscarEntradas, name="buscarEntradas"),
    path('encontrarEntradas/', encontrarEntradas, name="encontrarEntradas"),


    #_____LOGIN / LOGOUT / REGISTRACION
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="menu/logout.html"), name="logout"),
    path('register/', register, name="register"),


    #_____EDICION PERFIL / AVATAR
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="camiarClave"), #<int:pk> represta al 1/ en ruta 1/password/. Para resolver vamos a usar una class bv "class CambiarClave" en views.py
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]