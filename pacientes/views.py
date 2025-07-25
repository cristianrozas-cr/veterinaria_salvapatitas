from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import MascotaForm, ConsultaForm, VacunaForm
from .models import Mascota, Consulta, Vacuna
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import ServicioPeluqueriaForm
from .models import ServicioPeluqueria
from django.forms import formset_factory

# Create your views here.


# Registro de Mascotas
@login_required
def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota registrada exitosamente.')
            return redirect('listar_mascotas')
        else:
            messages.error(request, 'Error al registrar la mascota.')
    else:
        form = MascotaForm()
    return render(request, 'pacientes/registrar_mascota.html', {'form': form})
    
    return render(request, 'pacientes/registrar_mascota.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'pacientes/registro_exitoso.html')

# Listado de Mascotas
@login_required
def listar_mascotas(request):
    query = request.GET.get('q', '')
    if query:
        mascotas = Mascota.objects.filter(
            Q(nombre__icontains=query) | 
            Q(especie__icontains=query) | 
            Q(raza__icontains=query)
        )
    else:
        mascotas = Mascota.objects.all()
    return render(request, 'pacientes/listar_mascotas.html',
                {'mascotas': mascotas, 'query': query})

# Detalle de Mascota
def detalle_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    consultas = mascota.consultas.all()
    vacunas = mascota.vacunas.all()
    return render(request, 'pacientes/detalle_mascota.html', {
        'mascota': mascota,
        'consultas': consultas,
        'vacunas': vacunas,
    })


# Consultas y Vacunas
def agregar_consulta(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.mascota = mascota
            consulta.save()
            messages.success(request, 'Consulta agregada exitosamente.')
            return redirect('detalle_mascota', mascota_id=mascota.id)
    else:
        form = ConsultaForm()
    return render(request, 'pacientes/agregar_consulta.html', {'form': form, 'mascota': mascota})

def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta actualizada exitosamente.')
            return redirect('detalle_mascota', mascota_id=consulta.mascota.id)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'pacientes/editar_consulta.html', {'form': form, 'consulta': consulta})

def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    mascota_id = consulta.mascota.id

    if request.method == 'POST':
        consulta.delete()
        messages.success(request, 'Consulta eliminada exitosamente.')
        return redirect('detalle_mascota', mascota_id=mascota_id)

    return render(request, 'pacientes/eliminar_consulta.html', {'consulta': consulta})


def detalle_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    return render(request, 'pacientes/detalle_consulta.html', {'consulta': consulta})

# Vacunas
def agregar_vacuna(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = VacunaForm(request.POST)
        if form.is_valid():
            vacuna = form.save(commit=False)
            vacuna.mascota = mascota
            vacuna.save()
            return redirect('detalle_mascota', mascota_id=mascota.id)
    else:
        form = VacunaForm()
    return render(request, 'pacientes/agregar_vacuna.html', {'form': form, 'mascota': mascota})

from .models import Vacuna
from .forms import VacunaForm

def editar_vacuna(request, vacuna_id):
    vacuna = get_object_or_404(Vacuna, id=vacuna_id)
    if request.method == 'POST':
        form = VacunaForm(request.POST, instance=vacuna)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vacuna actualizada exitosamente.')
            return redirect('detalle_mascota', mascota_id=vacuna.mascota.id)
    else:
        form = VacunaForm(instance=vacuna)
    return render(request, 'pacientes/editar_vacuna.html', {'form': form, 'vacuna': vacuna})

def eliminar_vacuna(request, vacuna_id):
    vacuna = get_object_or_404(Vacuna, id=vacuna_id)
    mascota_id = vacuna.mascota.id

    if request.method == 'POST':
        vacuna.delete()
        messages.success(request, 'Vacuna eliminada exitosamente.')
        return redirect('detalle_mascota', mascota_id=mascota_id)

    return render(request, 'pacientes/eliminar_vacuna.html', {'vacuna': vacuna})

def detalle_vacuna(request, vacuna_id):
    vacuna = get_object_or_404(Vacuna, id=vacuna_id)
    return render(request, 'pacientes/detalle_vacuna.html', {'vacuna': vacuna})

# Edición de Mascotas y Consultas
def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota actualizada exitosamente.')
            return redirect('detalle_mascota', mascota_id=mascota.id)
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'pacientes/editar_mascota.html', {'form': form, 'mascota': mascota})

def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta actualizada exitosamente.')
            messages.success(request, 'Consulta actualizada exitosamente.')
            return redirect('detalle_mascota', mascota_id=consulta.mascota.id)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'pacientes/editar_consulta.html', {'form': form, 'consulta': consulta})


# Area de Selección
@login_required
def seleccion_area(request):
    return render(request, 'seleccion_area.html')


# Home Page
@login_required
def home(request):
    total_mascotas = Mascota.objects.count()
    return render(request, 'home.html', {'total_mascotas': total_mascotas})

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'registro/login.html'

    def form_valid(self, form):
        messages.success(self.request, '¡Has iniciado sesión exitosamente! 🎉')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos. Intenta de nuevo.')
        return super().form_invalid(form)
    
# Servicio de Peluquería
def peluqueria_home(request):
    return render(request, 'peluqueria/home.html')



def registrar_servicios_peluqueria(request):
    ServicioFormSet = formset_factory(ServicioPeluqueriaForm, extra=1)  # un formulario visible por defecto
    if request.method == 'POST':
        formset = ServicioFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:  # evita guardar formularios vacíos
                    form.save()
            messages.success(request, "¡Servicios registrados correctamente!")
            return redirect('peluqueria_home')
    else:
        formset = ServicioFormSet()

    return render(request, 'peluqueria/registrar_servicios.html', {'formset': formset})

def listar_servicios_peluqueria(request):
    servicios = ServicioPeluqueria.objects.select_related('mascota').all().order_by('-fecha_servicio')
    return render(request, 'peluqueria/listar_servicios.html', {'servicios': servicios})