import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_oo.settings')
django.setup()
from objects_app.models import *

def add_default_vel():
    v1 = Velocidades(velocidade='LENTO')
    v1.save()

    v2 = Velocidades(velocidade='MEDIO')
    v2.save()

    v3 = Velocidades(velocidade='RAPIDO')
    v3.save()


def add_default_dificulty():
    d1 = Dificuldades(dificuldade='FACIL')
    d1.save()

    d2 = Dificuldades(dificuldade='MEDIO')
    d2.save()

    d3 = Dificuldades(dificuldade='DIFICIL')
    d3.save()
    
    d4 = Dificuldades(dificuldade='ALEATORIO')
    d4.save()
  
  
def add_default_cor():  
    c1 = Cores(cor = 'AMARELO')
    c1.save()
    
    c2 = Cores(cor = 'VERMELHO')
    c2.save()
    
    c3 = Cores(cor = 'AZUL')
    c3.save()
    
    c4 = Cores(cor = 'ALEATORIO')
    c4.save()

def add_ui_cor():
    ui_color1 = Cores_UI(coresUI='Padrao')
    ui_color1.save()
    
    ui_color2 = Cores_UI(coresUI='DarkMode')
    ui_color2.save()
    
    ui_color3 = Cores_UI(coresUI='Aleatorio')
    ui_color3.save()
    
    ui_colorChoice = Cores_UI(coresUI='DefaultNoMoreNagging')
    ui_colorChoice.save()

def add_counter():
    counterLog = Numero_Logs_Historicos(numeroLogs= 0)
    counterLog.save()
    
    counterHist = Numero_Logs_Historicos(numeroHistoricos= 0)
    counterHist.save()
    
def user_logado():
    logou = Usuario_Logado(usuario_email='',logado='N')
    logou.save()
    
add_default_vel()
add_default_dificulty()
add_default_cor()
add_ui_cor()
add_counter()
user_logado()