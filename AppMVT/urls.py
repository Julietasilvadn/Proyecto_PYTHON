from django.contrib import admin
from django.urls import path, include
from AppMVT.views import *
from msilib.schema import AdminExecuteSequence
from django.contrib import admin
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inicio/', Inicio.as_view(), name='inicio'),
    path('perfil/', Perfil.as_view(), name='perfil'),
    path('reserva/', reserva_formulario, name='reserva'),
    path('about/', About.as_view(), name='about'),

    path('login/', views.login_request, name="login"),
    path('registrar/', views.register, name='registrar'), 
    path('logout/', LogoutView.as_view(template_name='AppMVT/logout.html'), name='logout'),
    
    path('crear_mascota', views.CrearMascotas.as_view(), name='crear_mascota'),
    path('listar_mascotas/', views.ListarMascotas.as_view(), name='listar_mascotas'), 
    path('detalle_mascota/<pk>/', views.DetalleMascotas.as_view(), name='detalle_mascota'),
    path('modificar_mascota/<pk>/', views.ModificarMascotas.as_view(), name='modificar_mascota'),
    path('borrar_mascota/<pk>/', views.BorrarMascotas.as_view(), name='borrar_mascota'),

    path('listar_usuarios/', views.ListarUsuarios.as_view(), name='listar_usuarios'), 
    path('detalle_usuario/<pk>/', views.DetalleUsuarios.as_view(), name='detalle_usuario'),
    path('modificar_usuario/<pk>/', views.ModificarUsuarios.as_view(), name='modificar_usuario'),


    ]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)