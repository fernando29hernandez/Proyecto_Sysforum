from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Create your models here.

class Usuario(AbstractUser):
    tipo = models.BooleanField(default=False)     
    def __str__(self):     	
        return '{} {}'.format(self.id,self.username)
class Tema(models.Model):
    usuario_fk = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=255)
    Titulo = models.CharField(max_length=100)
    def __str__(self):
        return 'Id:{} Titulo:{}'.format(self.id,self.Titulo)
    

class Comentario(models.Model):
    contenido = models.CharField(max_length = 200)
    tema_fk = models.ForeignKey(Tema,on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
