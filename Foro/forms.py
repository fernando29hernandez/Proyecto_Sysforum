from django import forms
from django.utils.safestring import mark_safe

from django.forms import ModelForm, Textarea, TextInput, URLInput, PasswordInput, EmailInput
from Foro.models import *



class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = ['Titulo', 'Descripcion']
        widgets = {
            'titulo': TextInput(attrs={'class':'form-control'}),
            'descripcion': TextInput(attrs={'class':'form-control'}),
            
        }
        labels={
            'titulo': 'Nombre',
            'descripcion': 'Descripcion',
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
            'contenido': 'Contenido',
        }
