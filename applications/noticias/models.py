from django.db import models


#from applications.usuario.models import Usuarios

from applications.categorias.models import Categorias
# Create your models here.
class Noticia(models.Model):
    

    
    categorias = models.ForeignKey(Categorias,related_name= 'categorias', on_delete=models.CASCADE)
    #id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=50)
    #fecha_noticia =
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    #fecha_publicacion =
    subtitulo_detalles = models.CharField('Subtitulo', max_length=100)
    texto = models.TextField('Texto', max_length=2000)
        
    def __str__(self) -> str:
        x= str(self.titulo) + str(self.id_categoria) + str(self.subtitulo_detalles)
        return x

   