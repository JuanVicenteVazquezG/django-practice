from django.contrib import admin

from .models import Empleado, Habilidades

# Register your models here.


admin.site.register(Habilidades)


# atributo que mostrara todos los registros de este modelo
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',

    )
    search_fields = ('first_name',)
    list_filter = ('job',)


admin.site.register(Empleado, EmpleadosAdmin)
