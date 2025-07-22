from django.db import models

# Create your models here.

class Mascota(models.Model):
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]
    
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    nombre_dueno = models.CharField(max_length=100)
    telefono_dueno = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} ({self.nombre_dueno})"

class Consulta(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='consultas')
    fecha = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)

    def __str__(self):
        return f"Consulta de {self.mascota.nombre} el {self.fecha}"

class Vacuna(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='vacunas')
    fecha = models.DateField()
    tipo_vacuna = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo_vacuna} aplicada a {self.mascota.nombre} el {self.fecha}"