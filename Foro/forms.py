from django import forms
from django.utils.safestring import mark_safe

from django.forms import ModelForm, Textarea, TextInput, URLInput, PasswordInput, EmailInput
from Foro.models import *



class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = ['Titulo', 'Descripcion','usuario_fk']
        labels={
            'Titulo': 'Ingrese nombre de tema a discusion',
            'Descripcion': 'Brinde una descripcion de ayuda ',
    
        }
        widgets = {
            'Titulo': TextInput(attrs={'class':'form-control'}),
            'Descripcion': TextInput(attrs={'class':'form-control'}),
            'usuario_fk' : forms.HiddenInput(),           
                
        }

class TemaForm1(ModelForm):
    class Meta:
        model = Tema
        fields = ['Titulo', 'Descripcion','usuario_fk']
        labels={
            'Titulo': 'Ingrese nombre de tema a discusion',
            'Descripcion': 'Brinde una descripcion de ayuda ',
        }
        widgets = {
            'Titulo': TextInput(attrs={'class':'form-control'}),
            'Descripcion': TextInput(attrs={'class':'form-control'}),
            
        }
         

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido','tema_fk' ]
        widgets = {
            'contenido': TextInput(attrs = {'class':'form-control'}),
            'tema_fk' : forms.HiddenInput(),           
        }
        labels={
            'contenido': 'Ingrese aqui su respuesta/opinion',
        }
class CrearUsuarioForm(ModelForm):
     class Meta:
         model = Usuario
         fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
         ]
         labels = {
            'username':'Nombre de usuario',
            'password':'Contraseña',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Correo electrónico',
         }
         widgets = {
            'username':TextInput(attrs={'class':'form-control'}),
            'password':PasswordInput(attrs={'class':'form-control'}),
            'first_name':TextInput(attrs={'class':'form-control'}),
            'last_name':TextInput(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
         }