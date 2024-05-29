from django.contrib import admin
from item.models import Item 

class ItemAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome', 'preco', 'descricao', 'categoria')  #esses campos serão mostrados para facilitar a amostragem
    list_filter = ('categoria',)  # Adiciona um filtro para categorias
    search_fields = ('nome', 'descricao')  # Adiciona campos de busca

admin.site.register(Item, ItemAdmin) #permite o gerenciamento/administração dos "itens" no painel de administrador django


