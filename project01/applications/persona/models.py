from django.db import models

# Create your models here.

# FOREING KEYS

from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidades = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = "habilidad"
        verbose_name_plural = "habilidades Empleados"

    def __str__(self):
        return f"{str(self.id)} - {self.first_habilidad}"


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
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = " Empleados de la empresa"
        # ordenacion descendente por el primer nombre
        ordering = ['-first_name', 'departamento']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return f"{str(self.pk)} - {self.first_name} - {self.last_name}"
