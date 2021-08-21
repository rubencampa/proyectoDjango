from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request,"../templates/ProyectoWebApp/home.html")


def tienda(request):
    
    return render(request,"../templates/ProyectoWebApp/tienda.html")

def blog(request):
    
    return render(request,"../templates/ProyectoWebApp/blog.html")

def contacto(request):
    
    return render(request,"../templates/ProyectoWebApp/contacto.html")
