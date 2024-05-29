from django.contrib import admin
from .models import Mesa

class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'status')

admin.site.register(Mesa, MesaAdmin)


