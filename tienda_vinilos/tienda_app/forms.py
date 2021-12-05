#Archivo para los formatos de los formularios de los modelos de la base de datos

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario, Producto
from .models import *
from django.forms import MultiWidget, TextInput

#Formato del Formulario de creacion de usuario para login

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(max_length=20)
    first_name=forms.CharField(max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2= forms.CharField(widget=forms.PasswordInput())

    def clean_first_name(self):
        first_name=self.cleaned_data.get("first_name")
        if first_name.isalpha():
            return first_name
        else:
            raise ValidationError("Nombre no valido")


    class Meta:
        model=User
        fields = ['username','email','first_name','password1','password2']


#Formato de extension a la creacion de usuario
       
class Perfilform(forms.ModelForm):
    choices = [
        ('argentina', 'Argentina'),
        ('peru', 'Perú'),
        ('brasil', 'Brasil'),
        ('chile', 'Chile'),
        ('ecuador', 'Ecuador'),
        ('otro', 'Otro')
    ]
    pais = forms.ChoiceField(choices=choices)

    class Meta:
        model= PerfilUsuario
        fields=['pais']

#Formato del Formulario para la edicion de Usuario

class Modform(forms.ModelForm):
    direccion=forms.CharField(max_length=50)
    edad=forms.IntegerField(max_value=100, min_value=15)
    celular=forms.CharField(max_length=9,min_length=9)
    choices = [
        ('argentina', 'Argentina'),
        ('peru', 'Perú'),
        ('brasil', 'Brasil'),
        ('chile', 'Chile'),
        ('ecuador', 'Ecuador'),
        ('otro', 'Otro'),
    ]
    pais = forms.ChoiceField(choices=choices)


    def clean_celular(self):
        celular=self.cleaned_data.get("celular")
        if celular.isdigit():
            return celular
        else:
            raise forms.ValidationError("Numero de celular no valido")

            

    class Meta:
        model=PerfilUsuario
        fields=['celular','direccion','edad','pais']

#Formato del formulario de datos del producto

class Productoform(forms.ModelForm):
    precio=forms.IntegerField(min_value=1,max_value=1000)
    stock=forms.IntegerField(min_value=0, max_value=200)
    class Meta:
        model=Producto
        fields= '__all__'

#Formato del formulario de Genero del producto

class Generoform(forms.ModelForm):
    nombre=forms.CharField(max_length=15)

    def clean_nombre(self):
        nombre=self.cleaned_data.get("nombre")
        if nombre.isdigit():
            raise forms.ValidationError("Genero no valido")
        else:
            return nombre


    class Meta:
        model=Genero
        fields= '__all__'

#Formato del formulario de Artista del producto

class Artistaform(forms.ModelForm):
    class Meta:
        model=Artista
        fields= '__all__'