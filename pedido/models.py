from django.db import models
from mesa.models import Mesa
from item.models import Item
from comanda.models import Comanda

class Pedido(models.Model):

    CHOICES = [
        ('preparo', 'Em preparo'),
        ('finalizado', 'Finalizado'),
    ]

    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, blank=True)
    itens = models.ManyToManyField(Item)
    status = models.CharField(max_length=128, choices=CHOICES)

    def save(self, *args, **kwargs):
        if not self.pk:  # Verifica se o pedido é novo
            # Gera a comanda automaticamente se ainda não estiver definida
            if not self.comanda:
                comanda = Comanda.objects.create(obs=f"Comanda da mesa {self.mesa.numero}")
                self.comanda = comanda
        super().save(*args, **kwargs)

    def __str__(self):
        return (self.mesa.numero + "/" + self.status)



