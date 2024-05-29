from django.contrib import admin
from pedido.models import Pedido

class PedidoAdmin(admin.ModelAdmin):

    list_display = ('id', 'status')  #esses campos serão mostrados para facilitar a amostragem

admin.site.register(Pedido, PedidoAdmin) #permite o gerenciamento/administração dos "itens" no painel de administrador django