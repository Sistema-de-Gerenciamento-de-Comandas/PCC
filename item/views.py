from django.shortcuts import render
from .models import Item

def listar_itens(request):
    itens = Item.objects.all()
    itens_unicos = []

    # Dicionário para rastrear os nomes dos itens já adicionados
    nomes_adicionados = set()

    for item in itens:
        # Verifica se o nome do item já foi adicionado anteriormente
        if item.nome not in nomes_adicionados:
            itens_unicos.append(item)
            nomes_adicionados.add(item.nome)

    return render(request, 'listar_itens.html', {'itens': itens_unicos})