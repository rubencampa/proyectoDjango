from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def home(request):
    servicios=Servicio.objects.all()
    return render(request,"../templates/ProyectoWebApp/home.html",{"servicios" : servicios})

def servicios(request):
    
    return render(request,"../templates/ProyectoWebApp/servicios.html")

def tienda(request):
    
    return render(request,"../templates/ProyectoWebApp/tienda.html")

def blog(request):
    
    return render(request,"../templates/ProyectoWebApp/blog.html")

def contacto(request):
    
    return render(request,"../templates/ProyectoWebApp/contacto.html")
