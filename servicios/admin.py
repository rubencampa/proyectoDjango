from django.contrib import admin
from .models import Ser
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio , ServicioAdmin);




    

