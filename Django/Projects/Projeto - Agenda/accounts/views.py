from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

# Create your views here.

def login(request):

    if request.method !=  'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou Senha Inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login Feito com Sucesso !')
        return redirect('dashboard')
    

def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def cadastro(request):

    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2: # validando campos em branco
        messages.error(request, 'Nenhum Campo Pode Estar Vázio ! ')
        return render(request, 'accounts/cadastro.html') 
    
    try:
        validate_email(email) # validando email

    except:
        messages.error(request, 'Email Inválido !')
        return render(request, 'accounts/cadastro.html') 
    
    if len(senha) < 6:
        messages.error(request, 'Senha Precisa ter 6 ou Mais Caracteres !') # validando senha
        return render(request, 'accounts/cadastro.html') 
    
    if len(usuario) < 6:
        messages.error(request, 'Usuário Precisa ter 6 ou Mais Caracteres !') # validando usuario
        return render(request, 'accounts/cadastro.html') 
    
    if senha != senha2: # validando senhas
        messages.error(request, 'Senhas não Conferem ! ')
        return render(request, 'accounts/cadastro.html') 
    
    if User.objects.filter(username=usuario).exists(): # checando existencia do usuario
        messages.error(request, 'Usuário já Existe ! ')
        return render(request, 'accounts/cadastro.html') 
    
    if User.objects.filter(email=email).exists(): # checando existencia do email
        messages.error(request, 'Email já Existe ! ')
        return render(request, 'accounts/cadastro.html') 

    messages.success(request, 'Registrado com Sucesso ! Faça o Login. ') # tudo certo

    user = User.objects.create_user(username=usuario,email=email,password=senha,first_name=nome,last_name=sobrenome)
    user.save()

    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):

    if request.method != 'POST':
        form = FormContato
        return render(request, 'accounts/dashboard.html',{ 'form': form})
    
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao Enviar Formulário')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html',{ 'form': form})
    
    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Descrição Precisa ter Mais de 5 Caracteres')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html',{ 'form': form})
    
    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} Salvo !')
    return redirect('dashboard')