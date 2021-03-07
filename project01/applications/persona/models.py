from django.db import models

# Create your models here.

# FOREING KEYS

from applications.departamento.models import Departamento


class Empleado(models.Model):
    """ Modelo para tabla empleado """

    # choice
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')
    )
    first_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Aoellidos", max_length=60)
    job = models.CharField("Trabajo", max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # imagen = models.ImageField(, upload_to=None, height_field=None, width_field=None)

    def __str__(self):
        return f"{str(self.pk)} - {self.first_name} - {self.last_name}"
