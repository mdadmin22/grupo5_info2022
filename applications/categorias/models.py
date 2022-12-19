from django.db import models


#from applications.categorias.models import Categorias
# Create your models here.
from django.db import models



# Create your models here.
class Categorias(models.Model):
    
    nombre_categoria = models.CharField('' , max_length=50)
   
    def __str__(self) -> str:
        return str(self.id) + '-' +  self.nombre_categoria
