from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Evento

# View para a tela inicial
def tela_inicial(request):
    return render(request, 'events/tela_inicial.html')

# View para o painel de controle
@login_required  # Garante que o usuário esteja autenticado para acessar
def painel_controle(request):
    eventos = Evento.objects.filter(usuario=request.user)
    return render(request, 'events/painel_controle.html', {'eventos': eventos})

# View para o cadastro de usuário
def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário
            login(request, user)  # Faz o login automaticamente após o cadastro
            return redirect('tela_inicial')  # Redireciona para a tela inicial após o cadastro
    else:
        form = UserCreationForm()  # Cria o formulário em GET
    return render(request, 'events/cadastro.html', {'form': form})
