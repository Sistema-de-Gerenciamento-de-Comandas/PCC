from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(User):
    cpf = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex='^\d{11}$', message='CPF inválido')], verbose_name="Infome seu CPF")
    telefone = PhoneNumberField(verbose_name="Telefone (99) 9999-9999")
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    data_nascimento = models.DateField(null=True, blank=True)

    # Renomear os campos para evitar conflitos
    #grupos = models.ManyToManyField('auth.Group', related_name='usuario_grupos')
    #permissoes = models.ManyToManyField('auth.Permission', related_name='usuario_permissoes')


