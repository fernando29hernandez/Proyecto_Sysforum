from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Create your models here.
class Tema(models.Model):
    Descripcion = models.CharField(max_length=255)
    Titulo = models.CharField(max_length=100)
    def __str__(self):
        return 'Id:{} Titulo:{}'.format(self.id,self.Titulo)
    

class Comentario(models.Model):
    contenido = models.CharField(max_length = 200)
    tema_fk = models.ForeignKey(Tema,on_delete=models.CASCADE)

class Usuario(AbstractUser):
    tipo = models.BooleanField(default=False)     
    def __str__(self):     	
        return '{} {}'.format(self.id,self.username)