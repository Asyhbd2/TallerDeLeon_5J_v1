from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    APaterno = models.CharField(max_length=50,verbose_name="apellido paterno")
    AMaterno = models.CharField(max_length=50,verbose_name="apellido materno")
    Nombres = models.CharField(max_length=100,verbose_name="Nombre(s)")
    Fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento",null=False,blank=False)
    Fecha_ingreso = models.DateField(verbose_name="Fecha Ingreso",null=False,blank=False)