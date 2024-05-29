from django.db import models

class Mesa(models.Model):

    CHOICES = [
        ('reservada', 'Esta mesa já está reservada'),
        ('não reservada', 'Esta mesa ainda não está reservada'),
    ]

    numero = models.CharField(max_length=3)
    status = models.CharField(max_length=128, choices=CHOICES)

    def __str__(self):
        return self.numero

