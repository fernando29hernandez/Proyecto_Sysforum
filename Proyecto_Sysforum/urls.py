"""Proyecto_Sysforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from Foro.views import list_temas, add_tema, ver_tema, show_dashboard,home,login,logout,loggedin,invalid,ver
from django.conf.urls import include, url
from Foro import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^dashboard',show_dashboard, name="dashboard" ),
    url(r'^tema/list/', list_temas, name='list_temas'), #listado
    url(r'^tema/add/', add_tema, name='add_tema'), #formulario para añadir
    url(r'^ver/(?P<pk>\d+)$', ver_tema, name='ver'), 
    url(r'^$',home,name='home'),
    url(r'^accounts/login/$',login,name='login'),
	url(r'^accounts/auth/$', ver,name='ver_auth'),
	url(r'^accounts/logout/$', logout,name='logout'),
	url(r'^accounts/loggedin/', loggedin,name='loggedin'),
	url(r'^accounts/invalid/$', invalid,name='invalid'),
    url(r'^crearUsuario/', views.CrearUsuario, name="CrearUsuario"), 
]

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
