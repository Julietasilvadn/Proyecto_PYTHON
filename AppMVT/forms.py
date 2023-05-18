from distutils.command.build_scripts import first_line_re
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UsuarioFormulario(forms.Form):
    nombre=forms.CharField()
    apellido= forms.CharField()
    dni= forms.IntegerField()
    email= forms.EmailField()
    contraseña= forms.CharField()
    
class MascotaFormulario(forms.Form):
    nombre= forms.CharField()
    nacimiento= forms.DateField()
    imagen= forms.ImageField()

class ReservaFormulario(forms.Form):
    mascota= forms.CharField()
    dia= forms.CharField()

class UserRegisterForm(UserCreationForm):
    
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label= 'Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}