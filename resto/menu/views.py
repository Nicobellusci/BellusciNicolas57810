from django.shortcuts import render, redirect

from django.urls import reverse_lazy # Class-Based Views

from menu.models import *
from menu.forms import *

# Class-Based Views
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Aplicacion Auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

# Decoradores y mixines
from django.contrib.auth.mixins import LoginRequiredMixin # los mixines trabajan sobre las clases
from django.contrib.auth.decorators import login_required # los decoradores trabajan sobre las funciones


# Create your views here.
def home(request):
    return render(request, "menu/home.html") #cambie el index por home para poder hacer distinta la pagina inicial, del index se llevan los demas html.

def acerca(request):
    return render(request, "menu/Acerca.html")


#####---FORMULARIOS

#______ENTRADAS_______________________________________________________________________________________________
@login_required
def entradas(request):
    contexto = {"Entradas": Entradas.objects.all()}
    return render(request, "menu/Entradas.html", contexto)

@login_required
def entradasForm(request):
    if request.method == "POST": #pregunto si el requerimiento es POST (osea si ya vienen los datos cargados).
        miForm = EntradasForm(request.POST)
        if miForm.is_valid():
            entradas_nombre = miForm.cleaned_data.get("nombre")
            entradas_ingredientes = miForm.cleaned_data.get("ingredientes")
            entradas = Entradas(nombre=entradas_nombre, ingredientes=entradas_ingredientes)
            entradas.save()
            contexto = {"Entradas": Entradas.objects.all()}
            return render(request, "menu/Entradas.html", contexto)
    else: #si es else quiere decir que es la primera vez que pide el formulario. Entonces voy a crear un formulario vacio.
        miForm = EntradasForm() #Creo el fomulario miForm desde EntradasForm (que es la clase creada).
    return render(request, "menu/EntradasForm.html", {"form": miForm}) #Agrego el html que va a resolver y envio el formulario como un dicconario que va a tener como clave: "form" y como valor miForm.

#______UPDATE ENTRADAS
@login_required
def entradasUpdate(request, id_entrada):
    entradas = Entradas.objects.get(id=id_entrada)
    if request.method == "POST":
        miForm = EntradasForm(request.POST)
        if miForm.is_valid():
            entradas.nombre = miForm.cleaned_data.get("nombre") #cambio entradas_nombre por entradas.nombre porque es con el objeto que estoy trabajando.
            entradas.ingredientes = miForm.cleaned_data.get("ingredientes") #cambio entradas_ingredientes por entradas.ingredietnes porque es con el objeto que estoy trabajando.
            # borro esta entrada / entradas = Entradas(nombre=entradas_nombre, ingredientes=entradas_ingredientes)
            entradas.save()
            contexto = {"Entradas": Entradas.objects.all()}
            return render(request, "menu/Entradas.html", contexto)
    else:
        miForm = EntradasForm(initial={"nombre": entradas.nombre, "ingredientes": entradas.ingredientes})
    return render(request, "menu/EntradasForm.html", {"form": miForm})

#______DELETE ENTRADAS
@login_required
def entradasDelete(request, id_entrada):
    entradas = Entradas.objects.get(id=id_entrada)
    entradas.delete()
    contexto = {"Entradas": Entradas.objects.all()}
    return render(request, "menu/Entradas.html", contexto)

#_____________________________________________________________________________________________________________


#______PIZZAS_________________________________________________________________________________________________
@login_required
def pizzas(request):
    contexto = {"Pizzas": Pizza.objects.all()}
    return render(request, "menu/Pizzas.html", contexto)

@login_required
def pizzasForm(request):
    if request.method == "POST":
        miForm = PizzasForm(request.POST)
        if miForm.is_valid():
            pizzas_nombre = miForm.cleaned_data.get("nombre")
            pizzas_ingredientes = miForm.cleaned_data.get("ingredientes")
            pizzas = Pizza(nombre=pizzas_nombre, ingredientes=pizzas_ingredientes)
            pizzas.save()
            contexto = {"Pizzas": Pizza.objects.all()}
            return render(request, "menu/Pizzas.html", contexto)
    else:
        miForm = PizzasForm()
    return render(request, "menu/PizzasForm.html", {"form": miForm})

#______UPDATE PIZZAS
@login_required
def pizzasUpdate(request, id_pizza):
    pizzas = Pizza.objects.get(id=id_pizza)
    if request.method == "POST":
        miForm = PizzasForm(request.POST)
        if miForm.is_valid():
            pizzas.nombre = miForm.cleaned_data.get("nombre")
            pizzas.ingredientes = miForm.cleaned_data.get("ingredientes")
            pizzas.save()
            contexto = {"Pizzas": Pizza.objects.all()}
            return render(request, "menu/Pizzas.html", contexto)
    else:
        miForm = PizzasForm(initial={"nombre": pizzas.nombre, "ingredientes": pizzas.ingredientes})
    return render(request, "menu/PizzasForm.html", {"form": miForm})

#______DELETE PIZZAS
@login_required
def pizzasDelete(request, id_pizza):
    pizzas = Pizza.objects.get(id=id_pizza)
    pizzas.delete()
    contexto = {"Pizzas": Pizza.objects.all()}
    return render(request, "menu/Pizzas.html", contexto)
#_______________________________________________________________________________________________________________


#______BURGERS__________________________________________________________________________________________________
@login_required
def burgers(request):
    contexto = {"Burgers": Burger.objects.all()}
    return render(request, "menu/Burgers.html", contexto)

@login_required
def burgersForm(request):
    if request.method == "POST":
        miForm = BurgersForm(request.POST)
        if miForm.is_valid():
            burgers_nombre = miForm.cleaned_data.get("nombre")
            burgers_ingredientes = miForm.cleaned_data.get("ingredientes")
            burgers_tipo_pan = miForm.cleaned_data.get("tipo_pan")
            burgers = Burger(nombre=burgers_nombre, ingredientes=burgers_ingredientes, tipo_pan=burgers_tipo_pan)
            burgers.save()
            contexto = {"Burgers": Burger.objects.all()}
            return render(request, "menu/Burgers.html", contexto)
    else:
        miForm = BurgersForm()
    return render(request, "menu/BurgersForm.html", {"form": miForm})

#______UPDATE BURGERS
@login_required
def burgersUpdate(request, id_burger):
    burgers = Burger.objects.get(id=id_burger)
    if request.method == "POST":
        miForm = BurgersForm(request.POST)
        if miForm.is_valid():
            burgers.nombre = miForm.cleaned_data.get("nombre")
            burgers.ingredientes = miForm.cleaned_data.get("ingredientes")
            burgers.tipo_pan = miForm.cleaned_data.get("tipo_pan")
            burgers.save()
            contexto = {"Burgers": Burger.objects.all()}
            return render(request, "menu/Burgers.html", contexto)
    else:
        miForm = BurgersForm(initial={"nombre": burgers.nombre, "ingredientes": burgers.ingredientes, "tipo_pan": burgers.tipo_pan})
    return render(request, "menu/BurgersForm.html", {"form": miForm})

#______DELETE BURGERS
@login_required
def burgersDelete(request, id_burger):
    burgers = Burger.objects.get(id=id_burger)
    burgers.delete()
    contexto = {"Burgers": Burger.objects.all()}
    return render(request, "menu/Burgers.html", contexto)
#__________________________________________________________________________________________________________________


#______EMPANADAS___________________________________________________________________________________________________
@login_required
def empanadas(request):
    contexto = {"Empanadas": Empanadas.objects.all()}
    return render(request, "menu/Empanadas.html", contexto)

@login_required
def empanadasForm(request):
    if request.method == "POST":
        miForm = EmpanadasForm(request.POST)
        if miForm.is_valid():
            empanadas_nombre = miForm.cleaned_data.get("nombre")
            empanadas_ingredientes = miForm.cleaned_data.get("ingredientes")
            empanadas_coccion = miForm.cleaned_data.get("coccion")
            empanadas= Empanadas(nombre=empanadas_nombre, ingredientes=empanadas_ingredientes, coccion=empanadas_coccion)
            empanadas.save()
            contexto = {"Empanadas": Empanadas.objects.all()}
            return render(request, "menu/Empanadas.html", contexto)
    else:
        miForm = EmpanadasForm()
    return render(request, "menu/EmpanadasForm.html", {"form": miForm})

#______UPDATE EMPANADAS
@login_required
def empanadasUpdate(request, id_empanada):
    empanadas = Empanadas.objects.get(id=id_empanada)
    if request.method == "POST":
        miForm = EmpanadasForm(request.POST)
        if miForm.is_valid():
            empanadas.nombre = miForm.cleaned_data.get("nombre")
            empanadas.ingredientes = miForm.cleaned_data.get("ingredientes")
            empanadas.coccion = miForm.cleaned_data.get("coccion")
            empanadas.save()
            contexto = {"Empanadas": Empanadas.objects.all()}
            return render(request, "menu/Empanadas.html", contexto)
    else:
        miForm = EmpanadasForm(initial={"nombre": empanadas.nombre, "ingredientes": empanadas.ingredientes, "coccion": empanadas.coccion})
    return render(request, "menu/EmpanadasForm.html", {"form": miForm})

#______DELETE EMPANADAS
@login_required
def empanadasDelete(request, id_empanada):
    empanadas = Empanadas.objects.get(id=id_empanada)
    empanadas.delete()
    contexto = {"Empanadas": Empanadas.objects.all()}
    return render(request, "menu/Empanadas.html", contexto)
#___________________________________________________________________________________________________________________


#______BUSCAR_______________________________________________________________________________________________________
@login_required
def buscarEntradas (request):
    return render(request, "menu/buscarEntradas.html") #renderiza un formulario buscarEntradas solo para ingresar el pataron a buscar.

def encontrarEntradas (request):
    if request.GET["buscar"]: #aplico el filtro, si viene algo en el campo name="buscar" del buscarEntradas.html <p> Ingrese el patrón de búsqueda: <input type="text" name="buscar" id="buscar"></p> .
        patron = request.GET["buscar"] #mi patron va a ser el dato ingresado
        entradas =Entradas.objects.filter(nombre__icontains=patron) #creo un obtejo entradas invocando a la class Entradas.objects.filter(), donde le digo que el nombre contenga el patron ingresado.
        contexto = {"Entradas": entradas} #devuelve todos los objetos que cumplen con el filtro.
    else:
        contexto = {"Entradas": Entradas.objects.all()} #si no se pone un patron de busqueda devuelve todas las Entradas.
    
    return render(request, "menu/Entradas.html", contexto)
#____________________________________________________________________________________________________________________


#______LOGIN /REGISTRACION___________________________________________________________________________________________
def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"] #obtengo los datos del formulario.
        clave = request.POST["password"] #obtengo los datos del formulario.
        user = authenticate(request, username=usuario, password=clave)  #creo un objeto user utilizando la funcion/motodo importado authenticate y validar si el usuario esta creado en la app
                                                                        #si el usuario y clave corresponden la funcion devuelve un objeto en "user"
        if user is not None: 
            login(request, user) #si no es nulo, loguea / login es funcion importada
            
            #__________________Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________    

            return render(request, "menu/home.html")
        else: #si el usuario no coincide, entra en este else
            return redirect(reverse_lazy('login'))  #redirecciono al login / reverse_lazy resuelve la clave login (que la tengo que generar en urls.py)
                                                    #el redirect lo importe desde from django.shortcuts import render, redirect
    else:
        miForm = AuthenticationForm()
    return render(request, "menu/login.html", {"form": miForm})


#______REGISTRO_______________________________________________________________________________________________________
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username") queda sin uso porque va todo dentro de fomulario.
            miForm.save()
            return redirect(reverse_lazy('login')) #luego de registrarse redirecciono al login.
    else:
        miForm =RegistroForm()
    return render(request, "menu/register.html", {"form": miForm})
#_____________________________________________________________________________________________________________________


#______EDITAR PERFIL__________________________________________________________________________________________________
@login_required # agrego el decorador para permitir la edicion de perfil solo si el usaurio esta logueado.
def editProfile(request):
    usuario = request.user #tomo los datos del usuario.
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)   #busco el objeto de la base de datos cuando el username es = al usuario.
                                                        #modifico los datos con los datos que recupero del formulario. 
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("Home")) #lo devuelvo a la ruta Home.
    else:
        miForm = UserEditForm(instance=usuario) #genero un formulario con los datos del usaurio si es la primera vez (instance=usuario)
    return render(request, "menu/editarPerfil.html", {"form": miForm})

#______CAMBIAR CLAVE con Class-Based Views____________________________________________________________________________
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "menu/cambiar_clave.html"
    success_url = reverse_lazy("Home")
#_____________________________________________________________________________________________________________________


#______AVATAR__________________________________________________________________________________________________________
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]

            #__________Borrar Avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________    

            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            
            #__________Enviar la imagen al Home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________
            return redirect(reverse_lazy("Home"))
    else:
        miForm = AvatarForm()
    return render(request, "menu/agregarAvatar.html", {"form": miForm})
#_____________________________________________________________________________________________________________________
