from django.contrib import admin
from comanda.models import Comanda

class ComandaAdmin(admin.ModelAdmin):

    list_display = ('id', 'mesa_numero', 'itens_pedidos', 'total', 'total_da_comanda')

    def mesa_numero(self, obj):
        return obj.pedido_set.first().mesa.numero if obj.pedido_set.first() else None

    def itens_pedidos(self, obj):
        itens = ", ".join([item.nome for pedido in obj.pedido_set.all() for item in pedido.itens.all()])
        return itens if itens else None

    def total(self, obj):
        total_comanda = sum(sum(item.preco for item in pedido.itens.all()) for pedido in obj.pedido_set.all())
        return total_comanda if total_comanda else None

    def total_da_comanda(self, obj):
        return sum(sum(item.preco for item in pedido.itens.all()) for pedido in obj.pedido_set.all()) if obj.pedido_set.all() else None

    mesa_numero.short_description = 'Mesa'
    itens_pedidos.short_description = 'Itens Pedidos'
    total.short_description = 'Total'
    total_da_comanda.short_description = 'Total da Comanda'

admin.site.register(Comanda, ComandaAdmin)
