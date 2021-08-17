from django.contrib import admin
from servicios.models import servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

admin.site.register(servicio,ServicioAdmin)

