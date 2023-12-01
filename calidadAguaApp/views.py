from django.shortcuts import render, HttpResponse
from calidadAguaApp.forms import formularioAgregar

# Create your views here.

def home(request):
    return render(request, "calidadAguaApp/home.html")
    
#def login(request):
#    return HttpResponse("login")

def agregar(request):
    if request.method=="POST":
        miformulario=formularioAgregar(request.POST)
        if miformulario.is_valid():
            infForm=miformulario.cleaned_data
            return render(request, "calidadAguaApp/gracias.html")
    else:
        miformulario=formularioAgregar()
    
    return render(request, "calidadAguaApp/agregar.html",{"form":miformulario})

def ver(request):
    return render(request, "calidadAguaApp/ver.html")

# def gracias(request):
#     return render(request, "calidadAguaApp/gracias.html")

def ajustes(request):
    return render(request, "calidadAguaApp/ajustes.html")

def calendario(request):
    return render(request, "calidadAguaApp/calendario.html")

def historial(request):
    return render(request, "calidadAguaApp/historial.html")