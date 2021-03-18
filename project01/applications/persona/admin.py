from django.contrib import admin

from .models import Empleado, Habilidades

# Register your models here.


admin.site.register(Habilidades)

class EmpleadosAdmin(admin.ModelAdmin):
	list_display = (
		'first_name',
		'las_name',
		'departamento',
		'job',

		)

admin.site.register(Empleado, EmpleadosAdmin)