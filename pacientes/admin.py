from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Mascota, Consulta, Vacuna, ServicioPeluqueria

admin.site.register(Mascota)
admin.site.register(Consulta)
admin.site.register(Vacuna)
admin.site.register(ServicioPeluqueria)