from django.db import models
from mesa.models import Mesa
from item.models import Item

class Comanda(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    obs = models.CharField(max_length=200)

    def pedidos(self):
        pedidos_info = []
        total_comanda = 0
        for pedido in self.pedido_set.all():
            total_pedido = sum(item.preco for item in pedido.itens.all())
            total_comanda += total_pedido
            info_pedido = f"Mesa {pedido.mesa.numero}: {', '.join([item.nome for item in pedido.itens.all()])} - Total: R${total_pedido:.2f}"
            pedidos_info.append(info_pedido)
        return pedidos_info, total_comanda

    def __str__(self):
        pedidos_info, total_comanda = self.pedidos()
        return f"{', '.join(pedidos_info)} - Total da Comanda: R${total_comanda:.2f}"
   