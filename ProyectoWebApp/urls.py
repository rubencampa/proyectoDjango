from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls), ---> El panel del admin va en las urls del proyecto
    path('', views.home, name="Home"),
    path('tienda/', views.tienda, name="Tienda"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)