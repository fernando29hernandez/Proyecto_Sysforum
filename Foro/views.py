# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from Sysforum.models import Tema, Comentario
from Sysforum.forms import *
from django.http import HttpResponse

def show_dashboard(request):
    return render(request, 'dashboard.html', {})

def list_temas(request):
    return render(request,"listar_temas.html", {"temas": Tema.objects.all(), "messages": messages.get_messages(request)})


def add_tema(request):
    form = TemaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/tema/list/")
    return render(request, 'crear_tema.html', {'form': form})

def ver_tema(request, pk):
    tema = Tema.objects.get(id=pk)
    form = ComentarioForm(request.POST or None)
    form.fields['tema_fk'].initial = pk
    if request.method == 'POST':
        if form.is_valid():
            if form.is_valid():
                form.save()
            return HttpResponseRedirect("/tema/list/")
    return render(request, 'ver_tema.html', {'tema': tema,'form': form, 'comentarios': Comentario.objects.filter(tema_fk=pk)})

