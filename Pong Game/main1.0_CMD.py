import django
import os
from datetime import datetime,date
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_oo.settings')
django.setup()
from objects_app.models import *
from subprocess import call
    
def data_hora():
    global data_atual,data_str,hora_atual
    data_atual = date.today()
    data_str = "{}/{}/{}".format(data_atual.day, data_atual.month,data_atual.year)
    hora_atual = datetime.now().strftime('%H:%M:%S')

def loginUser():
    if Velocidades.objects.exists() or Dificuldades.objects.exists() or Cores.objects.exists():
        pass
    else:
        call(["python", "config_tables.py"])
        
    global email_login,nome_display,get_userName
    print('\n\n\t\tFIVE PONG\n\n Antes de Iniciar, Entre com seu Usuário ou Realize um Cadastro !\n')
    
    opcao = int(input('\n1 - Fazer Login\t\t 2 - Cadastro de Usuário\n\n = '))
    
    if opcao == 1:
        email_login = str(input('Digite seu Email : '))
        senha_login = str(input('Digite sua Senha : '))
        
        if Usuario.objects.filter(email__exact=email_login,senha__exact=senha_login):
            data_hora()
            get_userName = Usuario.objects.filter(email__exact=email_login).values_list('nome',flat=True)[0]
            nome_display = str(get_userName)
            log_login = Log(text=(f'O Usuário {get_userName} fez o Login '),data=data_str,hora=hora_atual)
            log_login.save()
            menu()
        else:
            if Usuario.objects.filter(email__exact=email_login):
                print(f'\n - Senha para Conta {email_login} Incorreta , Tente Novamente o Login !')
                loginUser()
            else:
                print('\nUsuário não Encontrado , Deseja Cadastrar ? !\n')
                login_error_choice = int(input('0 - CADASTRO DE USUÁRIO \n' '1 - TENTAR NOVAMENTE' '\n= '))
                if login_error_choice == 1:
                    loginUser()
                else:
                    cadastroUser()   
                
    elif opcao == 2:
        cadastroUser()
    else:
        loginUser()

def menu():
    print(f'\n\tOlá {get_userName} ! Escolha uma Opção : \n')
    opcoes = int(input('1 - Iniciar Jogo\n''2 - Históricos de Jogo\n''3 - Cadastrar Novo Usuário\n''4 - Logs de Jogo\n' '5 - Esqueci Minha Senha\n''6 - Sair''\n= '))
    print('\n\n')
    if opcoes == 1:
        iniciarJogo()
    elif opcoes == 2:
        historico()
    elif opcoes == 3:
        cadastroUser()
    if opcoes == 4:
        logs()
    elif opcoes == 5:
        redefineSenha()
    elif opcoes == 6:
        logoff()
    else:
        menu()
        
def logoff():
    loginUser()
    
def logs(): 
    while True:
        print('\n\t##### LOGS DE JOGO #####\n')
        option = int(input('1 - Cadastrar um Log\n' '2 - Visualizar Logs\n' '3 - Voltar\n''\n= '))
        if option == 1:
            data_hora()
            log = Log(text=input("Digite seu Log\n\n = "),data=data_str,hora=hora_atual)
            print('\n Log Cadastrado !')
            log.save()
        elif option == 2:
            print("--------------------------------------------------------------------\nLogs no Banco de Dados: \n")
            logs = Log.objects.all()
            for log in logs:
                print(f"{log.pk}: {log.text} , {log.data}  {log.hora}\n")
        else:
            menu()
            

def historico():
    print('\n\t##### HISTÓRICOS DE JOGO #####\n')
    HistoricoJogo = Historico_jogo.objects.all()
    print('JOGO   PLAYER\t       DIFICULDADE \t     VELOCIDADE\t       COR DE JOGO \n')
    for Historico in HistoricoJogo:
        print(f"{Historico.pk}: \t{Historico.usuario_nome} \t\t{Historico.dificuldade} \t\t{Historico.velocidade} \t\t{Historico.cor}")
        

def cadastroUser():
    print('\n\t##### CADASTRO DE USUÁRIO #####\n')
    nome = str(input('Digite seu Nome : '))
    email = str(input('Digite seu Email : '))
    
    while Usuario.objects.filter(email__exact=email):
        print('\n - Já existe um Usuário Cadastrado com Este Email, Use Outro !\n')
        cadastroUser()
    else:
        senha = str(input('Digite sua Senha : '))
        senha_confirm = str(input('Confirme sua Senha : '))
        
        while True:
            if senha != senha_confirm:
                senha_confirm = input('\n - As Senhas não Batem , Tente Novamente !\n Confirme sua Senha : ')
            else:
                user = Usuario(nome=nome,senha=senha,email=email)
                user.save()
                data_hora()
                log_user = Log(text=(f'O Usuário {nome} foi Cadastrado'),data=data_str,hora=hora_atual)
                log_user.save()
                print(f'\nUsuário cadastrado com sucesso !\n\n')
                loginUser()



def redefineSenha():
     print(f'\t ##### {nome_display} ESQUECEU A SENHA #####\n') 
     if Usuario.objects.filter(email__exact=email_login):
        nova_senha = str(input('Digite sua Nova Senha : '))
        confirme = str(input('Confirme sua Nova Senha : '))
        while nova_senha != confirme:
            print('\n\n - As Senhas não Batem, Tente Novamente !\n\n')
            redefineSenha()
        Usuario.objects.filter(email__exact=email_login).update(senha=nova_senha)
        print('\n\n - Senha Alterada com Sucesso !')
        data_hora()
        get_userName = Usuario.objects.filter(email__exact=email_login).values_list('nome',flat=True)[0]
        log_senha = Log(text=(f'O Usuário {get_userName} Alterou a Senha '),data=data_str,hora=hora_atual)
        log_senha.save()
        loginUser()
    
def iniciarJogo():
    log_game = Log(text=(f'O Usuário {get_userName} Iniciou uma Rodada de Pong '),data=data_str,hora=hora_atual)
    log_game.save()
    get_userID = Usuario.objects.filter(email__exact=email_login).values_list('id',flat=True)[0]
    userID = Usuario.objects.get(pk=get_userID)
    historico_db = Historico_jogo(usuario_nome=nome_display,usuario=userID)
    historico_db.save()
    call(["python", "game.py"])

loginUser()
