import django
import os
import PySimpleGUI as sg
import re
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_oo.settings')
django.setup()
from datetime import datetime,date
from objects_app.models import *
from subprocess import call
from random import choice

email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # formatação correta para validar o email, feito usando o módulo RE (regex)

def data_hora(): # função que pega a data e hora atual do sistema
    global data_atual,data_str,hora_atual
    data_atual = date.today()
    data_str = "{}/{}/{}".format(data_atual.day, data_atual.month,data_atual.year)
    hora_atual = datetime.now().strftime('%H:%M:%S')
    

def menu():
    layout_titulo = [
        [sg.Text(f'Olá, {nome_display}',font='Arial 16 bold')],
    ]
    
    layout_menu = [
        [sg.Text('1 - ',font='Arial 14'),sg.Button('INICIAR JOGO',font='arial 12',size=(13,2))],
        [sg.Text('2 - ',font='Arial 14'),sg.Button('HISTÓRICO',font='arial 12',size=(13,2))],
        [sg.Text('4 - ',font='Arial 14'),sg.Button('LOGS',font='arial 12',size=(13,2))],
        [sg.Text('5 - ',font='Arial 14'),sg.Button('MUDAR SENHA',font='arial 12',size=(13,2))],
        [sg.Text('6 - ',font='Arial 14'),sg.Button('CONFIGS',font='arial 12',size=(13,2))],
        [sg.Text('7 - ',font='Arial 14'),sg.Button('SAIR',font='arial 12',size=(13,2))],
        [sg.Text('')]
    ]
    
    layout_geral = [
        [sg.Column(layout_titulo,justification='center',element_justification='center')],
        [sg.Column(layout_menu,justification='center',element_justification='center')],
    ]
    
    menu = sg.Window('Menu',element_padding=(0,10),size=(400,600),finalize=True,layout=layout_geral)
    
    while True:
        global values
        event, values = menu.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'INICIAR JOGO':
            menu.hide()
            IniciarJogo()
        elif event == 'HISTÓRICO':
            menu.hide()
            Historico()  
        elif event == 'SAIR':
            Usuario_Logado.objects.filter(pk=1).update(usuario_email='',logado='N')
            menu.hide()
            loginUser()
        elif event == 'LOGS':
            menu.hide()
            logs()
        elif event == 'MUDAR SENHA':
            menu.hide()
            redefineSenha()    
        elif event == 'CONFIGS':
            menu.hide()
            configuracoes_ui()
    
def loginUser():
    
    global layout_cor
    
    # esse if abaixo valida se existem dados nas tabelas, se tiver, ele não faz nada. Caso as tabelas estejam vazias, ele roda um outro arquivo python para inserir esses dados
	
    if Velocidades.objects.exists() or Dificuldades.objects.exists() or Cores.objects.exists() or Cores_UI.objects.exists() or Numero_Logs_Historicos.objects.exists() or Usuario_Logado.objects.exists():
        pass
    else:
        call(["python", "config_tables.py"])
    
    getcor = Cores_UI.objects.filter(pk=4).values_list('coresUI',flat=True)[0] # pega a cor que está salva no id 4 do banco e altera no layout
    layout_cor = sg.change_look_and_feel(getcor)
        
    layout_titulo = [
        [sg.Text('      LOGIN DE USUÁRIO',font='Arial 15 bold'),sg.Text('            ')]
    ]
    
    layout_login_inputs = [
        [sg.Text('EMAIL',font='Arial 12 bold')],
        [sg.Text('@  ',font='Arial 15'),sg.Input(key='email_login',font='arial 12')],
        [sg.Text('SENHA',font='arial 12 bold')],
        [sg.Text('🔒  ',font='Arial 16'),sg.Input(key='senha_login',password_char='*',font='arial 12')]
    ]
    
    layout_botoes = [
        [sg.Button('Login',font='arial 12',size=(10,1)),sg.Text('       '),sg.Button('Cadastrar',font='arial 12',size=(10,1))],
    ]
    
    layout_message = [
        [sg.Text('',key='return_login',font='arial 12 bold')]
    ]
    
    layout_geral = [
        [sg.Column(layout_titulo,justification='center',element_justification='center')],
        [sg.Column(layout_login_inputs,justification='center',element_justification='center')],
        [sg.Column(layout_botoes,justification='center',element_justification='center')],
        [sg.Column(layout_message,justification='center',element_justification='center')]
    ]
    
    loginWindow = sg.Window('Login de Usuário',element_padding=(0,10),finalize=True,layout=layout_geral)
    
    while True:
        global get_userName,nome_display,email_login,email_logado,get_userNameLogado
        
        event, values = loginWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Login':
            email_login = values['email_login']
            senha_login = values['senha_login']
            
	    # if abaixo valida o formato do email do regex e compara com o email inserido, também valida se o email digitado bate com algum email cadastrado no banco de dados
	    
            if not re.match(email_format,email_login) or not Usuario.objects.filter(email__exact=email_login):
                pass

            # se estiver tudo ok ele cai nesse else, onde vai pegar o nome do usuário para mostrar na tela de menu             

            else:
                get_userName = Usuario.objects.filter(email__exact=email_login).values_list('nome',flat=True)[0]
                nome_display = str(get_userName)

            # esse if abaixo valida o email e senha do banco para fazer o login, se estiver tudo certo ele faz um update na tabela do usuário logado com esse email e 'logado' = 'S'

            if Usuario.objects.filter(email__exact=email_login,senha__exact=senha_login):
                data_hora()
                Usuario_Logado.objects.filter(pk=1).update(usuario_email=email_login,logado='S')
                email_logado = Usuario_Logado.objects.filter(pk=1).values_list('usuario_email',flat=True)[0]
                get_userNameLogado = Usuario.objects.filter(email__exact=email_logado).values_list('nome',flat=True)[0]
                loginWindow.hide()
                menu()

           # se der problema no login ele gera as mensagens na tela avisando...

            else:
                if Usuario.objects.filter(email__exact=email_login):
                    loginWindow['return_login'].update(f'Senha para Conta " {nome_display} " Incorreta , Tente Novamente !')
                    loginWindow.find_element('senha_login').update('')
                else:
                    loginWindow['return_login'].update(f'Usuário Não Encontrado , Use o Botão "Cadastrar" ! ')
                    loginWindow.find_element('senha_login').update('')
                    loginWindow.find_element('email_login').update('')
        

	# botão para ativar o evento da função de cadastro de usuário
             
        elif event == 'Cadastrar':
            loginWindow.hide()
            cadastroUser()

def cadastroUser():
    
    layout_titulo = [
        [sg.Text('      CADASTRO DE USUÁRIO',font='Arial 15 bold'),sg.Text('            ')]
    ]
    
    layout_cadastro = [
                [sg.Text('NOME',font='Arial 11 bold')],
                [sg.Text('    '),sg.Input(key='nome_cad'),sg.Text('           ')],
                [sg.Text('EMAIL',font='Arial 11 bold')],
                [sg.Text('@ ',font='12'),sg.Input(key='email_cad'),sg.Text('          ')],
                [sg.Text('SENHA',font='Arial 11 bold')],
                [sg.Text('🔒 ',font=16),sg.Input(key='senha_cad',password_char='*'),sg.Text('          ')],
                [sg.Text('CONFIRMAR SENHA',font='Arial 11 bold')],
                [sg.Text('🔐 ',font=16),sg.Input(key='senha_conf',password_char='*'),sg.Text('          ')]
            ]
    
    layout_botoes = [
        [sg.Button('Cadastrar',font='arial 12',size=(10,1)),sg.Text('       '),sg.Button('Voltar',font='arial 12',size=(10,1))]]
    
    layout_message = [
        [sg.Text('',key='return_cad',font='arial 12 bold')]
    ]
    
    layout_geral = [
        [sg.Column(layout_titulo,justification='center',element_justification='center')],
        [sg.Column(layout_cadastro,justification='center',element_justification='center')],
        [sg.Column(layout_botoes,justification='center',element_justification='center')],
        [sg.Column(layout_message,justification='center',element_justification='center')]
    ]
    
    cadastroWindow = sg.Window('Cadastro de Usuário',element_padding=(0,10),finalize=True,layout=layout_geral)
    
    
    while True:
        event, values = cadastroWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Cadastrar':
            nome = values['nome_cad']
            email = values['email_cad']
            senha = values['senha_cad']
            senha_confirm = values['senha_conf']
            
            if len(nome) > 27: # esse if valida o tamanho do nome (não pode ser maior que 27)
                cadastroWindow['return_cad'].update('Digite um Nome Menor !')
                cadastroWindow.find_element('nome_cad').update('')

            elif not re.match(email_format,email): # valida o formato do email de acordo com o email_format (regex)
                cadastroWindow['return_cad'].update('Digite um Email com Formato Válido !')
                cadastroWindow.find_element('email_cad').update('')

            else: # se o email não estiver correto, ou as senhas forem diferentes, ou tiver algum campo vazio, ele gera as mensagens de erro

                if nome == '' or email == '' or senha == '' or senha_confirm == '':
                    cadastroWindow['return_cad'].update('Preencha Todos os Campos !')
                elif senha != senha_confirm:
                    cadastroWindow['return_cad'].update('As Senhas não Batem , Tente Novamente !')
                    cadastroWindow.find_element('senha_conf').update('')
                elif Usuario.objects.filter(email__exact=email):
                    cadastroWindow['return_cad'].update('Um Outro Usuário já Está Usando este Email !')
                    cadastroWindow.find_element('email_cad').update('')
	
                # se tudo estiver ok, ele cai nesse else, onde vai registrar o log no banco, registrar o cadastro do usuario e etc

                else:
                    user = Usuario(nome=nome,senha=senha,email=email)
                    user.save()
                    data_hora()
                    log_user = Log(text=(f'O Usuario {nome} foi Cadastrado'),data=data_str,hora=hora_atual)
                    log_user.save()
                    sg.Window('', [[sg.T(f'Usuário {nome} Cadastrado com Sucesso !')], [sg.OK(s=10)]],element_justification='center',disable_close=True).read(close=True)
                    cadastroWindow.hide()
                    loginUser()
        else:
            cadastroWindow.hide()
            loginUser()
        
def redefineSenha():
    
    layout_titulo = [
        [sg.Text(f'     ALTERAÇÃO DE SENHA',font='Arial 15 bold'),sg.Text('            ')]
    ]
    
    layout_alter = [
                [sg.Text(' NOVA SENHA',font='Arial 11 bold')],
                [sg.Text('🔒 ',font=16),sg.Input(key='senha_alter',password_char='*'),sg.Text('          ')],
                [sg.Text('CONFIRMAR SENHA',font='Arial 11 bold')],
                [sg.Text('🔐 ',font=16),sg.Input(key='senha_alterconf',password_char='*'),sg.Text('          ')]
            ]
    
    layout_botoes = [
        [sg.Button('Confirmar',font='arial 12',size=(10,1)),sg.Text('       '),sg.Button('Voltar',font='arial 12',size=(10,1))]]
    
    layout_message = [
        [sg.Text('',key='return_alter_err',font='arial 12 bold')]
    ]
    
    layout_geral = [
        [sg.Column(layout_titulo,justification='center',element_justification='center')],
        [sg.Column(layout_alter,justification='center',element_justification='center')],
        [sg.Column(layout_botoes,justification='center',element_justification='center')],
        [sg.Column(layout_message,justification='center',element_justification='center')]
    ]
    
    senhaWindow = sg.Window('Alterar Senha',element_padding=(0,10),finalize=True,layout=layout_geral)
    
    
    while True:
        event, values = senhaWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Voltar':
            senhaWindow.hide()
            menu()
        elif event == 'Confirmar':
            senha_alter = values['senha_alter']
            senha_alter_confirm = values['senha_alterconf']
            

            # valida se as senhas estão preenchidas e se estão iguais
	    	
            if senha_alter == '' or senha_alter_confirm == '':
                senhaWindow['return_alter_err'].update(f'Preencha Todos os Campos !')
            elif senha_alter != senha_alter_confirm:
                senhaWindow['return_alter_err'].update(f'As Senhas não Batem, Tente Novamente !')
                senhaWindow.find_element('senha_alterconf').update('')

            # se estiver tudo certo ele da um update na senha de acordo com o email do usuário      

            else:
                Usuario.objects.filter(email__exact=email_logado).update(senha=senha_alter)
                data_hora()
                log_senha = Log(text=(f'O Usuario {nome_display} Alterou a Senha '),data=data_str,hora=hora_atual)
                log_senha.save()
                Usuario_Logado.objects.filter(pk=1).update(usuario_email='',logado='N')
                sg.Window('', [[sg.T(f'Senha Alterada !')], [sg.OK(s=10)]],element_justification='center',disable_close=True).read(close=True)
                senhaWindow.hide()
                loginUser()
                
    
def IniciarJogo():
    
    layout_start_inputs = [
        [sg.Text('NOME DO ADVERSÁRIO : ',font='Arial 12 bold')],
        [sg.Text('  ',font='Arial 15'),sg.Input(key='adversario',font='arial 12')]
    ]
    
    layout_botoes = [
        [sg.Button('Jogar',font='arial 12',size=(10,1)),sg.Text('       '),sg.Button('Voltar',font='arial 12',size=(10,1))]]
    
    layout_message = [
        [sg.Text('',key='return_err',font='arial 12 bold')]
    ]
    
    layout_geral = [
        [sg.Column(layout_start_inputs,justification='center',element_justification='center')],
        [sg.Column(layout_botoes,justification='center',element_justification='center')],
        [sg.Column(layout_message,justification='center',element_justification='center')],]
    
    gameWindow = sg.Window('Iniciar JOGO',element_padding=(0,10),finalize=True,layout=layout_geral)
    
    while True:
        event, values = gameWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Voltar':
            gameWindow.hide()
            menu()
        elif event == 'Jogar':
            adv_nome = values['adversario']
            

            # valida se o nome está vázio ou se é maior que 20 caracteres

            if adv_nome == '':
                gameWindow['return_err'].update(f'O Nome não Poder ser Vazio !')
            else:
                if len(adv_nome) > 20:
                    gameWindow['return_err'].update(f'Use um Nome Menor !')

                # se estiver tudo ok ele faz o insert do id do usuário que iniciou o game na tabela de histórico e gera um log desse jogo

                else:
                    data_hora()
                    get_userID = Usuario.objects.filter(email__exact=email_logado).values_list('id',flat=True)[0]
                    userID = Usuario.objects.get(pk=get_userID)
                    historico_db = Historico_jogo(usuario_nome=nome_display,usuario=userID)
                    historico_db.save()
                    get_lastid = Historico_jogo.objects.last().id
                    Historico_jogo.objects.filter(pk=get_lastid).update(adversario_nome=adv_nome)
                    log_game = Log(text=(f'O Usuario : {get_userNameLogado} Iniciou uma Rodada de Pong Contra : {adv_nome}'),data=data_str,hora=hora_atual)
                    log_game.save()
                    call(["python", "game.py"])
                    gameWindow.find_element('adversario').update('')


def Historico():
    
    if Historico_jogo.objects.exists():
    
        layout_titulo = [
            [sg.Text('      HISTÓRICO DE JOGO    ',font='Arial 15 bold')],
        ]
        
        HistoricoJogo = Historico_jogo.objects.all()
        
        for Historico in HistoricoJogo:
            ultima_partida = (f'Jogo : {Historico.pk},  Player : {Historico.usuario_nome},  Adversário : {Historico.adversario_nome},  Dificuldade: {Historico.dificuldade},  Velocidade: {Historico.velocidade},  Cor: {Historico.cor}')
            
        layout_hist = [
            [sg.Text('Ultimo Registro :',font='Arial 12 bold')],
            [sg.Text(f'{ultima_partida}',font='Arial 11')],
            ]
        
        layout_botoes = [
            [sg.Button('Voltar',font='Arial 12',size=(12,1)),sg.Text('       '),sg.Button('Gerar Histórico',font='arial 12',size=(12,1))]
        ]
        
        layout_geral = [
            [sg.Column(layout_titulo,justification='center',element_justification='center')],
            [sg.Column(layout_hist,justification='center',element_justification='center')],
            [sg.Column(layout_botoes,justification='center',element_justification='center')],
        ]
        
        historicoWindow = sg.Window('Historico',element_padding=(0,10),size=(900,300),finalize=True,layout=layout_geral)
        
        while True:
            global values
            event, values = historicoWindow.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Voltar':
                historicoWindow.hide()
                menu()

            # pega o numero de historico gerado no banco e aumenta em 1, assim, ele gera um novo txt ao invés de escrever sempre no mesmo.
 
            elif event == 'Gerar Histórico':
                historico_numero = Numero_Logs_Historicos.objects.filter(pk=2).values_list('numeroHistoricos',flat=True)[0]
                historico_adicional = historico_numero + 1
                Numero_Logs_Historicos.objects.filter(pk=2).update(numeroHistoricos=historico_adicional)
                sg.Window('', [[sg.T(f'Históricos Gerados em "txts/historico{historico_adicional}.txt"')], [sg.OK(s=10)]],element_justification='center',disable_close=True).read(close=True)
                Historico = Historico_jogo.objects.all()
                for Historico in HistoricoJogo:
                    with open(f'txts/historico{historico_adicional}.txt','a') as f:
                        f.write(f"Jogo : {Historico.pk} ;  Player : {Historico.usuario_nome}  ; Adversário : {Historico.adversario_nome}  ; Dificuldade: {Historico.dificuldade}  ; Velocidade: {Historico.velocidade}  ; Cor: {Historico.cor}\n")
    else:
        sg.Window('', [[sg.T(f'Jogue Uma Partida Antes de Acessar o Histórico !')], [sg.OK(s=10)]],element_justification='center',disable_close=True).read(close=True)
        menu()

def logs():
    
    layout_titulo = [
         [sg.Text('      LOG DE JOGO    ',font='Arial 15 bold')],
    ]
    
    logs = Log.objects.all()
    for log in logs:
        ultimoLog = (f"{log.pk}: {log.text} , {log.data}  {log.hora}")
        
    layout_log = [
        [sg.Text('Ultimo Registro de Log :',font='Arial 12 bold')],
        [sg.Text(f'{ultimoLog}',font='Arial 11')],
        ]
    
    layout_botoes = [
        [sg.Button('Voltar',font='arial 12',size=(10,1)),sg.Text('       '),sg.Button('Gerar Logs',font='arial 12',size=(10,1))]
    ]
    
    layout_geral = [
        [sg.Column(layout_titulo,justification='center',element_justification='center')],
        [sg.Column(layout_log,justification='center',element_justification='center')],
        [sg.Column(layout_botoes,justification='center',element_justification='center')],
    ]
    
    logsWindow = sg.Window('Logs',element_padding=(0,10),size=(750,300),finalize=True,layout=layout_geral)
    
    while True:
        global values
        event, values = logsWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Voltar':
            logsWindow.hide()
            menu()

        # pega o numero de logs gerados no banco e aumenta em 1, assim, ele gera um novo txt ao invés de escrever sempre no mesmo.

        elif event == 'Gerar Logs':
            log_numero = Numero_Logs_Historicos.objects.filter(pk=2).values_list('numeroLogs',flat=True)[0]
            log_adicional = log_numero + 1
            Numero_Logs_Historicos.objects.filter(pk=2).update(numeroLogs=log_adicional)
            sg.Window('', [[sg.T(f'Logs Gerados em "txts/logs{log_adicional}.txt"')], [sg.OK(s=10)]],element_justification='center',disable_close=True).read(close=True)
            logs = Log.objects.all()
            for log in logs:
                with open(f'txts/logs{log_adicional}.txt','a') as f:
                    f.write(f"{log.pk}: {log.text} , {log.data}  {log.hora}\n")


def configuracoes_ui():
    
    global layout_cor
    
    layout_titulo = [
         [sg.Text('      COR DO LAYOUT    ',font='Arial 15 bold')],
    ]
    
    corpadrao = Cores_UI.objects.filter(pk=1).values_list('coresUI',flat=True)[0]
    corDark = Cores_UI.objects.filter(pk=2).values_list('coresUI',flat=True)[0]
    corAleatoria = Cores_UI.objects.filter(pk=3).values_list('coresUI',flat=True)[0]
    ListaCores = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey', 'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
    
    layout_cores = [
        [sg.Button(f'{corpadrao}',font='arial 12',size=(11,2))],
        [sg.Button(f'{corDark}',font='arial 12',size=(11,2))],
        [sg.Button(f'{corAleatoria}',font='arial 12',size=(11,2))],
        [sg.Text('')],
        [sg.Button(f'Voltar',font='arial 12',size=(11,2))],
    ]
    
    layout_geral = [
        [sg.Column(layout_titulo,justification='center',element_justification='center')],
        [sg.Column(layout_cores,justification='center',element_justification='center')],
    ]
    
    
    configsWindow = sg.Window('Configurações',element_padding=(0,10),size=(400,400),finalize=True,layout=layout_geral)   
    
    while True:
        global values
        event, values = configsWindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Voltar':
            configsWindow.hide()
            menu()
        elif event == corDark:
            Cores_UI.objects.filter(pk=4).update(coresUI='DarkBlue1')
            configsWindow.hide()
            layout_cor = sg.change_look_and_feel('DarkBlue1')
            menu()
        elif event == corpadrao:
            Cores_UI.objects.filter(pk=4).update(coresUI='DefaultNoMoreNagging')
            configsWindow.hide()
            layout_cor = sg.change_look_and_feel('DefaultNoMoreNagging')
            menu()
        elif event == corAleatoria:
            Aleatorio = choice(ListaCores)
            Cores_UI.objects.filter(pk=4).update(coresUI=f'{Aleatorio}')
            configsWindow.hide()
            layout_cor = sg.change_look_and_feel(f'{Aleatorio}')
            menu()

# valida se o usuário estava logado de acordo com a tabela usuário logado, se não estiver ele inicia na tela de login
          
if Usuario_Logado.objects.filter(usuario_email='') or Usuario_Logado.objects.filter(logado='N') or not Usuario_Logado.objects.exists():
    loginUser()

# caso a tabela de usuario logado tenha algum email, ele vai abrir o jogo já no menu logado com aquele usuário que está no banco

else:
    global email_logado,get_userNameLogado
    layout_cor = sg.change_look_and_feel(Cores_UI.objects.filter(pk=4).values_list('coresUI',flat=True)[0])
    email_logado = Usuario_Logado.objects.filter(pk=1).values_list('usuario_email',flat=True)[0]
    get_userNameLogado = Usuario.objects.filter(email__exact=email_logado).values_list('nome',flat=True)[0]
    nome_display = str(get_userNameLogado)
    menu()
