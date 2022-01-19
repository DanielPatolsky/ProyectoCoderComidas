from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormuRestaurantes(forms.Form):
    pais =forms.CharField(max_length=100)
    nombre =forms.CharField(max_length=100)

class FormuComidas(forms.Form):
    pais =forms.CharField(max_length=100)
    comida =forms.CharField(max_length=100)

class FormuCiudades(forms.Form):
    pais =forms.CharField(max_length=100)
    continente =forms.CharField(max_length=100)

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 

        

class UserRegisterForm(UserCreationForm):
  
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 