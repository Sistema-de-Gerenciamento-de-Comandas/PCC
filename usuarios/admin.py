from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'telefone', 'data_de_criacao', 'data_nascimento')

admin.site.register(Usuario, UsuarioAdmin)
