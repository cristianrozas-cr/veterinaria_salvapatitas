from django import forms
from .models import Mascota, Consulta, Vacuna
from .models import ServicioPeluqueria

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'sexo', 'nombre_dueno', 'telefono_dueno']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'nombre_dueno': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_dueno': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['fecha', 'motivo', 'diagnostico', 'tratamiento']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tratamiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = ['fecha', 'tipo_vacuna', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tipo_vacuna': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class ServicioPeluqueriaForm(forms.ModelForm):
    nombre_mascota = forms.CharField(label="Nombre de la mascota")

    class Meta:
        model = ServicioPeluqueria
        fields = ['nombre_mascota', 'fecha_servicio', 'tipo_servicio', 'descripcion', 'precio', 'estado', 'encargado']

    def clean_nombre_mascota(self):
        nombre = self.cleaned_data['nombre_mascota']
        try:
            mascota = Mascota.objects.get(nombre__iexact=nombre.strip())
        except Mascota.DoesNotExist:
            raise forms.ValidationError("No se encontró una mascota con ese nombre.")
        return mascota  # devolvemos la instancia

    def save(self, commit=True):
        # Sobrescribimos para asignar la mascota encontrada
        mascota = self.cleaned_data['nombre_mascota']
        instance = super().save(commit=False)
        instance.mascota = mascota
        if commit:
            instance.save()
        return instance
    
ServicioPeluqueriaFormSet = forms.formset_factory(ServicioPeluqueriaForm, extra=3)