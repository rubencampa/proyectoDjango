from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def home(request):
    
    return render(request,"../templates/ProyectoWebApp/home.html")

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request,"../templates/ProyectoWebApp/servicios.html",{"servicios" : servicios})

def tienda(request):
    
    return render(request,"../templates/ProyectoWebApp/tienda.html")

def blog(request):
    
    return render(request,"../templates/ProyectoWebApp/blog.html")

def contacto(request):
    
    return render(request,"../templates/ProyectoWebApp/contacto.html")
