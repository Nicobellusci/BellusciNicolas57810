from django import forms #modulo que para crear formularios y contienen clases como los models.

from django.contrib.auth.models import User #tabla donde se van guardando todos los usuarios del sistema
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #creo mi formulario pero heredo de otros formularios que son UserCreationForm y UserChangeForm


#_____CLASES FORM_____
#_____Entradas
class EntradasForm(forms.Form): #este formulario va a tener los datos que le voy a pedir al usuario.
    nombre = forms.CharField(max_length=50, required=True) #como este dato es obligario le agrego el requerido=True
    ingredientes = forms.CharField(max_length=100, required=True)

#_____Pizzas
class PizzasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    ingredientes = forms.CharField(max_length=100, required=True)

#_____Burgers
class BurgersForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    ingredientes = forms.CharField(max_length=100, required=True)
    tipo_pan = forms.CharField(max_length=50, required=True)

#_____Empanadas
class EmpanadasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    ingredientes = forms.CharField(max_length=100, required=True)
    coccion = forms.CharField(max_length=50, required=True)


#_____Registro de usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True) # email, password1, password2 son campos dentro del modelo "User"
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) #widget es un formato de campo para enmascarar la clave y el widget que resuelve eso es PasswordInput.
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta: #creo una clase Meta porque el modelo del cual vamos crear y guardar estos datos, es User.
                #los campos que quiero que aparezcan son ["username"first_name""last_name""email""password1""password2"]
        model = User
        fields = ["username", "email", "password1", "password2"]


#_____Editar Perfil de usuario:
class UserEditForm(UserChangeForm): #genero UserEditForm que va a heredar de UserChangeForm.
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    
    #asocio este usuario al modelo User y puede cambiar el email, el first_name y el last_name
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        

#______AVATAR_________________________________________________________________________________________
class AvatarForm(forms.Form):
     imagen = forms.ImageField(required=True)
    
#_____________________________________________________________________________________________________