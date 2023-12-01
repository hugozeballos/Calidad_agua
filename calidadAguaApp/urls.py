from django.urls import path
from calidadAguaApp import views

urlpatterns = [
    path('', views.home,name="Home"),
    path('agregar/', views.agregar,name="Agregar"),
    path('ver/', views.ver,name="Ver"),
    path('historial/', views.historial,name="Historial"),
    path('calendario/', views.calendario,name="Calendario"),
    path('ajustes/', views.ajustes,name="Ajustes"),
    #path('gracias/', views.gracias,name="Gracias"),
    
]