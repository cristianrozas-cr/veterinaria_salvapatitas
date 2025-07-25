"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from pacientes import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from pacientes.views import CustomLoginView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.seleccion_area, name='seleccion_area'),
    path('home/', views.home, name='home'),
    path('registrar/', views.registrar_mascota, name='registrar_mascota'),
    path('registro-exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
    path('mascotas/<int:mascota_id>/', views.detalle_mascota, name='detalle_mascota'),
    path('mascotas/<int:mascota_id>/consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('mascotas/<int:mascota_id>/vacuna/', views.agregar_vacuna, name='agregar_vacuna'),
    path('consulta/<int:consulta_id>/editar/', views.editar_consulta, name='editar_consulta'),
    path('consulta/<int:consulta_id>/eliminar/', views.eliminar_consulta, name='eliminar_consulta'),
    path('vacuna/<int:vacuna_id>/editar/', views.editar_vacuna, name='editar_vacuna'),
    path('vacuna/<int:vacuna_id>/eliminar/', views.eliminar_vacuna, name='eliminar_vacuna'),
    path('consulta/<int:consulta_id>/', views.detalle_consulta, name='detalle_consulta'),
    path('vacuna/<int:vacuna_id>/', views.detalle_vacuna, name='detalle_vacuna'),
    path('mascotas/<int:mascota_id>/editar/', views.editar_mascota, name='editar_mascota'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('peluqueria/', views.peluqueria_home, name='peluqueria_home'),
    path('peluqueria/registrar/', views.registrar_servicios_peluqueria, name='registrar_servicios_peluqueria'),
    path('peluqueria/servicios/', views.listar_servicios_peluqueria, name='listar_servicios_peluqueria'),
]
