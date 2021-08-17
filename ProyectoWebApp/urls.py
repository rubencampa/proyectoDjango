from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    # path('admin/', admin.site.urls), ---> El panel del admin va en las urls del proyecto
    path('', views.home, name="Home"),
    path('servicios/', views.servicios, name="Servicios"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto, name="Contacto"),
]
