from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import MascotaForm, ConsultaForm, VacunaForm
from .models import Mascota, Consulta, Vacuna

# Create your views here.

def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pacientes/registro_exitoso.html')
    else:
        form = MascotaForm()
    
    return render(request, 'pacientes/registrar_mascota.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'pacientes/registro_exitoso.html')

def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'pacientes/listar_mascotas.html', {'mascotas': mascotas})

def detalle_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    consultas = mascota.consultas.all()
    vacunas = mascota.vacunas.all()
    return render(request, 'pacientes/detalle_mascota.html', {
        'mascota': mascota,
        'consultas': consultas,
        'vacunas': vacunas,
    })

""" Consultas """
def agregar_consulta(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.mascota = mascota
            consulta.save()
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
            return redirect('detalle_mascota', mascota_id=consulta.mascota.id)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'pacientes/editar_consulta.html', {'form': form, 'consulta': consulta})

def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    mascota_id = consulta.mascota.id

    if request.method == 'POST':
        consulta.delete()
        return redirect('detalle_mascota', mascota_id=mascota_id)

    return render(request, 'pacientes/eliminar_consulta.html', {'consulta': consulta})

from django.shortcuts import render, get_object_or_404

def detalle_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    return render(request, 'pacientes/detalle_consulta.html', {'consulta': consulta})


""" Vacunas """
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
            return redirect('detalle_mascota', mascota_id=vacuna.mascota.id)
    else:
        form = VacunaForm(instance=vacuna)
    return render(request, 'pacientes/editar_vacuna.html', {'form': form, 'vacuna': vacuna})

def eliminar_vacuna(request, vacuna_id):
    vacuna = get_object_or_404(Vacuna, id=vacuna_id)
    mascota_id = vacuna.mascota.id

    if request.method == 'POST':
        vacuna.delete()
        return redirect('detalle_mascota', mascota_id=mascota_id)

    return render(request, 'pacientes/eliminar_vacuna.html', {'vacuna': vacuna})

def detalle_vacuna(request, vacuna_id):
    vacuna = get_object_or_404(Vacuna, id=vacuna_id)
    return render(request, 'pacientes/detalle_vacuna.html', {'vacuna': vacuna})


def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
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
            return redirect('detalle_mascota', mascota_id=consulta.mascota.id)
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'pacientes/editar_consulta.html', {'form': form, 'consulta': consulta})



def home(request):
    return render(request, 'home.html')