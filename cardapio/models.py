from django.db import models
from item.models import Item

class Cardapio(models.Model):
    itens = models.ManyToManyField(Item, related_name='itens_do_cardapio')

    def __str__(self):
        return f"Cardápio {self.id}"


