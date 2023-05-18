from multiprocessing import context
from django.shortcuts import render, redirect
from AppMVT.models import *
from AppMVT.forms import  *
from urllib import request
from urllib.request import Request
from django.http import HttpResponse
from datetime import date, datetime 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView, View
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

"""BASE"""

class BaseView(View):
    context={}

class About(BaseView, TemplateView):
    template_name = "AppMVT/about.html"

class Inicio(BaseView, TemplateView):
    template_name = "AppMVT/inicio.html"

class Perfil( BaseView, TemplateView):
    template_name = "AppMVT/perfil.html"

class DetallePersona(BaseView, TemplateView):
    template_name = "AppMVT/detalle_persona.html"

# @login_required
# def dummy(request):
#     render(request, "")

# class SignUpView(SuccessMessageMixin, CreateView):
#   template_name = 'AppMVT/registrarse_form.html'
#   success_url = reverse_lazy('inicio')
#   form_class = UserRegisterForm
#   success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class PanelLogin(LoginView):
    template_name = 'AppMVT/login.html'
    next_page = reverse_lazy('inicio')

class PanelLogout(LogoutView):
    template_name = 'AppMVT/logout.html'

def reserva_formulario(request):
    if request.method == "POST":
        miReserva = ReservaFormulario(request.POST)
        print(miReserva)
        if miReserva.is_valid:
            informacion = miReserva.cleaned_data
            reserva = Reserva(mascota=informacion['mascota'], dia=informacion['dia'])
            reserva.save()
            return render(request, "AppMVT/inicio.html")
    else:
        miReserva=ReservaFormulario()
    return render(request, "AppMVT/reserva.html", {"miReserva":miReserva})




"""USUARIO"""

class ListarUsuarios(ListView):
    model = User
    template_name = "AppMVT/listar_usuarios.html"
   
class DetalleUsuarios(DetailView):
    model= User
    template_name = "AppMVT/detalle_usuario.html"

class ModificarUsuarios(UpdateView):
    model= User
    success_url="/listar_usuarios/"
    fields = ['first_name','last_name','email']
    template_name = "AppMVT/modificar_usuarios.html"

"""MASCOTA"""


class ListarMascotas(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Mascota
    template_name = "AppMVT/listar_mascotas.html"

class CrearMascotas(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Mascota
    success_url="/listar_mascotas/"
    
    fields = ['nombre', 'nacimiento', 'imagen']
    template_name = "AppMVT/crear_mascota.html"
    
class DetalleMascotas(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model= Mascota
    template_name = "AppMVT/detalle_mascota.html"

class ModificarMascotas(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model= Mascota
    success_url="/listar_mascotas/"
    fields = ['nombre', 'nacimiento', 'imagen']
    template_name = "AppMVT/modificar_mascota.html"

class BorrarMascotas(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model= Mascota
    success_url="/listar_mascotas/"
    template_name = "AppMVT/borrar_mascota.html"


def login_request(request):

    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                login (request, user)

                return render(request, 'AppMVT/inicio.html', {"mensaje":f"Bienvenido {user.get_username()} 😄!!"})
            else:
                return render(request, 'AppMVT/inicio.html', {'mensaje':'Error, ha ingresado incorrectamente los datos 🤔'})
        else:
            return render(request, 'AppMVT/inicio.html', {'mensaje':'Error, no existe el usuario 😭'})
    form = AuthenticationForm()

    return render(request, 'AppMVT/login.html', {'form':form})


def register(request):

    if (request.method == "POST"):

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppMVT/inicio.html",   {"mensaje": "Se ha creado exitosamente su usuario, Bienvenido a bordo marinero 😎"} )

    else:
        form = UserRegisterForm()


    return render(request,"AppMVT/registro.html" ,  {"form":form})