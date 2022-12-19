from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuarios(AbstractUser):

    #tipo = models.BooleanField()
    #nombres = models.CharField('nombres', max_length=50)
    #apellidos = models.CharField('apellidos', max_length=50)
    #telefonos_fijo = models.IntegerField('telefono_fijo',max_length=10)
    #celular = models.IntegerField('celular',max_length=10)
    #edad = 
    #fecha_de_nacimiento =
    #e_mail =
    #password =
    #fecha_registro =
    #hora_registro = 



   def str(self) -> str:
      return str(self.id) + '-' +  self.nombres