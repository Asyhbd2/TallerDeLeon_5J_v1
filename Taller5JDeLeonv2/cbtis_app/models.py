from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    APaterno = models.CharField(max_length=50,verbose_name="apellido paterno")