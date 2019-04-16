# -*- coding: utf-8 -*-
from django.shortcuts import render
import django.contrib.auth.hashers as encriptador
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.
from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404,redirect
from Foro.models import Tema, Comentario
from Foro.forms import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View
def show_dashboard(request):
    return render(request, 'loggedin.html', {})

def list_temas(request):
    return render(request,"listar_temas.html", {"temas": Tema.objects.all()})

class add_tema(View):

	def get(self,request):
		form = TemaForm(request.POST or None)
		aux = Usuario.objects.get(id=request.user.id)	
		form.fields['usuario_fk'].initial = request.user.id	
		return render(request, 'crear_tema.html', {'form': form})
	def post(self,request):
		form = TemaForm(request.POST or None)
		aux = Usuario.objects.get(id=request.user.id)	
		form.fields['usuario_fk'].initial = request.user.id	
		print(form.is_valid())
		if form.is_valid():
			form.save()
			return redirect('list_temas')
		

class ver_tema(View):
	def get(self,request,pk):
		tema = Tema.objects.get(id=pk)
		form = ComentarioForm(request.POST or None)
		form.fields['tema_fk'].initial = pk
		return render(request, 'ver_tema.html', {'tema': tema,'form': form, 'comentarios': Comentario.objects.filter(tema_fk=pk)})
	
	def post(self,request,pk):
		tema = Tema.objects.get(id=pk)
		form = ComentarioForm(request.POST or None)
		form.fields['tema_fk'].initial = pk
		if form.is_valid():
			if form.is_valid():
				form.save()
			return render(request, 'ver_tema.html', {'tema': tema,'form': form, 'comentarios': Comentario.objects.filter(tema_fk=pk)})

def home(request):
    return render(request, 'home.html')

def login(request):
	#c = {}
	#c.update(csrf(request))
	return render(request , 'login.html')

def ver(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return redirect('dashboard')
	else:
		return  redirect('invalid')

def loggedin(request):
	return redirect('dashboard')

def invalid(request):
	return render_to_response('invalid.html')

class CrearUsuario(View):	
	def get(self,request):	
		form = CrearUsuarioForm()
		#return redirect(reverse('apps.Carrito_Ventas.views.login'))
		return render(request,'crearusuario.html',{'form':form})
	def post(self,request):
		form = CrearUsuarioForm(request.POST)
		if form.is_valid():
			#form.save()
			v = form.save(commit = False)

			v.tipo = True #Indico que es un usuario normal
			v.password = encriptarpassword(v.password) #Veo si tengo que encriptar la contraseña
			v.save()
		else:
			print("ERROR")
		return redirect(reverse('login'))

def logout(request):
	auth.logout(request)
	return redirect(reverse('login'))
def encriptarpassword(password):
	#Verifica si la contrasea ya está encriptada
	#if encriptador.is_password_usable(password):
	#	return password #Si ya está encriptada regreso la misma contraseña
	#else:
	#	return encriptador.make_password(password,salt=None,hasher='default')

    #Siempre voy a encriptar
    return encriptador.make_password(password,salt=None,hasher='default')