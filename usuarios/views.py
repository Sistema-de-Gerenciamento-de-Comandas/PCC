from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Usuario
from item.models import Item
from django.http import  HttpResponse, HttpResponseRedirect
from .forms import UsuarioEditForm, UsuarioForm
from django.core.exceptions import ValidationError



def index(request):
    itens = Item.objects.all()
    return render(request, "usuarios/index.html", {'itens': itens})

# Listar dados da CONTA
def gerenciar_conta(request):
    if request.user.is_authenticated:  # Verifica se o usuário está autenticado
        try:
            usuario = Usuario.objects.get(username=request.user)
        except Usuario.DoesNotExist:  # Trata o caso em que o usuário não possui um registro
            usuario = None  # Define o usuário como None para indicar que não há registro
        
        return render(request, 'usuarios/gerenciar-conta.html', {'usuario': usuario})
    else:
        # Se o usuário não está autenticado, não há registro
        return render(request, 'usuarios/gerenciar-conta.html', {'usuario': None})

# Criar CONTA
def criar_conta(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Cleaned(normalized) data
            password = form.cleaned_data['password']
            
            #  Use set_password here
            user.set_password(password)
            user.save()

            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, "registration/criar-conta.html", {'form': form})


# Editar dados da CONTA
@login_required
def editar_dados(request, id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuarios/gerenciar-conta/?mensagem=Salvo')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar-dados.html', {'form': form, 'id_usuario':id_usuario})

# Excluir CONTA
@login_required
def deletar_conta(request, id_usuario):
    Usuario.objects.get(pk=id_usuario).delete()
    if Usuario.objects.count() == 0:
        return HttpResponseRedirect("/usuarios/login?mensagem=Deletado")  # Redireciona para a página de login
    return HttpResponseRedirect("/usuarios/gerenciar-conta?msg=Deletado")


@login_required

def confirmar_exclusao_dados(request, id_usuario):
    # Recupere o objeto Usuario com base no id_usuario
    usuario = get_object_or_404(Usuario, pk=id_usuario)

    if request.method == 'POST':
        usuario.delete()
        return redirect('index.html')  # Ou qualquer URL para onde você deseja redirecionar após a exclusão

    return render(request, 'usuarios/confirmar-exclusao-dados.html', {'usuario': usuario})

