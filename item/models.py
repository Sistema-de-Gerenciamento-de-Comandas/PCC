from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Item(models.Model):

    BEBIDAS = 'Bebidas'
    HAMBURGUERES = 'Hambúrgueres'
    PIZZAS = "Pizzas"

    CATEGORIA_CHOICES = [
        (BEBIDAS, 'Bebidas'),
        (HAMBURGUERES, 'Hambúrgueres'),
        (PIZZAS, 'Pizzas'),
    ]

    nome = models.CharField(max_length=30)
    preco  = models.FloatField(null=False, default=0.0)
    descricao = models.CharField(max_length=256)
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, default=BEBIDAS)

    def __str__(self):
        return self.nome #pega o titulo e mostra no painel administrativo de itens 

    