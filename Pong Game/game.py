import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_oo.settings')
django.setup()
from objects_app.models import *
from freegames import vector
from random import *
from turtle import *
import turtle
import keyboard
from freegames import vector
import time 

# gravar historico de partida no banco
def grava_historico():
    get_lastid = Historico_jogo.objects.last().id
    Historico_jogo.objects.filter(id__exact=get_lastid).update(dificuldade=dificuldade_str,cor=corStr,velocidade=get_vel_str)

# Função que gera a tela para escolher a velocidade do game

def definir_velocidade():
    global velocidade,get_vel_str
    getVelPK1 = Velocidades.objects.filter(pk=1).values_list('velocidade',flat=True)[0]
    getVelPK2 = Velocidades.objects.filter(pk=2).values_list('velocidade',flat=True)[0]
    getVelPK3 = Velocidades.objects.filter(pk=3).values_list('velocidade',flat=True)[0]
    get_velocidade = int(numinput(f'VELOCIDADE DE JOGO', f'1 - {getVelPK1},' f'      2 - {getVelPK2},' f'     3 - {getVelPK3}',default=1,minval=1,maxval=3))
    get_vel_str = ''
    
    if get_velocidade == 1:
        velocidade = 45
        get_vel_str = 'LENTO'
    elif get_velocidade == 2:
        velocidade = 35
        get_vel_str = 'MÉDIO'
    else:
        velocidade = 20
        get_vel_str = 'RÁPIDO'

# função que define a dificuldade de jogo. Dificuldade altera o tamanho dos retângulos

def definir_dificuldade():
    global Tamanho_Ret,dificuldade_str,dificuldade
    getdifPK1 = Dificuldades.objects.filter(pk=1).values_list('dificuldade',flat=True)[0]
    getdifPK2 = Dificuldades.objects.filter(pk=2).values_list('dificuldade',flat=True)[0]
    getdifPK3 = Dificuldades.objects.filter(pk=3).values_list('dificuldade',flat=True)[0]
    getdifPK4 = Dificuldades.objects.filter(pk=4).values_list('dificuldade',flat=True)[0]
    Tamanho_Ret = 40 ## tamanho padrão
    dificuldade = int(numinput('\tDIFICULDADE DE JOGO',f'1 - {getdifPK1} ;     ' f'2 - {getdifPK2} ;  ' f'3 - {getdifPK3} ;    ' f'4 - {getdifPK4}',default=4,minval=1,maxval=4))
    dificuldade_str = ''
    
    if dificuldade == 1:
        Tamanho_Ret = 55
        dificuldade_str = 'FÁCIL'
    elif dificuldade == 2:
        Tamanho_Ret = 35
        dificuldade_str = 'MÉDIO'
    elif dificuldade == 3:
        Tamanho_Ret = 23
        dificuldade_str = 'DIFÍCIL'
    else:
        listaRet = [55,35,23]
        Tamanho_Ret = choice(listaRet)
        dificuldade_str = 'ALEATÓRIO'

def definir_cor():
    global cor,corStr
    getcorPK1 = Cores.objects.filter(pk=1).values_list('cor',flat=True)[0]
    getcorPK2 = Cores.objects.filter(pk=2).values_list('cor',flat=True)[0]
    getcorPK3 = Cores.objects.filter(pk=3).values_list('cor',flat=True)[0]
    getcorPK4 = Cores.objects.filter(pk=4).values_list('cor',flat=True)[0]
    corNum = int(numinput('CORES DO JOGO',f'1 - {getcorPK1} ;    ' f'2 - {getcorPK2} ;   '  f'3 - {getcorPK3} ;  ' f'4 - {getcorPK4}',default=4,minval=1,maxval=4))
    listaCores = ['#deb649','#d12300','#245bff'] # cores aleatórias
    corStr = ''
    
    if corNum == 1:
        cor = '#deb649' ## padrão amarelo
        corStr = 'AMARELO'
    elif corNum == 2:
        cor = '#d12300' # vermelho
        corStr = 'VERMELHO'
    elif corNum == 3:
        cor = '#245bff'
        corStr = 'AZUL' # azul
    else:
        cor = choice(listaCores)
        corStr = 'ALEATÓRIA'

# Função que gera as informações antes do game iniciar

def escrita_Tela():
    global mensagem,estilo,font
    
    estilo = font =('Times New Roman',15,'bold')
    mensagem = Turtle()
    
    mensagem.hideturtle()
    mensagem.color(cor)
    
    for i in range(3,0,-1):
        mensagem.goto(-132,0)
        mensagem.write(f'O JOGO VAI COMEÇAR EM {i}s !\n\n\n',move='True',font=estilo)
        time.sleep(.2)
        mensagem.clear()
        time.sleep(.5)
        
    vel = mensagem
    vel.up()
    vel.goto(-80,0)
    vel.color(cor)
    vel.write(f'Velocidade = {get_vel_str}',move='False',align='left',font=estilo)
    
    modo = mensagem
    modo.goto(-100,-60)
    modo.color(cor)
    modo.write(f'Modo de Jogo : {dificuldade_str}',move='False',align='left',font=estilo)
    
# pontuação dos players - tentativa de fazer funfar
# atualização : dá não.

def placar():    
    
    count1 = 0
    count2 = 0
    
    player1 = mensagem
    player1.up()
    player1.goto(-190,180)
    player1.write(f'{count1}',move='False',align='left',font=estilo)
    
    player2 = mensagem
    player2.up()
    player2.goto(170,180)
    player2.write(f'{count2}',move='False',align='left',font=estilo)

        
def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}

def move(player, change):
    """Move player position by change."""
    
    if state[player] >= -180: 
      state[player] += change
    else:
        state[player] = -175

    if state[player] < 178:
        state[player] += change
    else:
        state[player] = 175

def rectangle(x, y, width, height):
    """Draw rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    down()
    color('white',cor)
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    """Draw game and move pong ball."""
    clear()
    rectangle(-200, state[1], 10, Tamanho_Ret) #facil = 55, medio = 35, difícil = 23
    rectangle(185, state[2], 10, Tamanho_Ret)
    bgcolor('black')
    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(14) # tamanho da bola
    update()

    
    if y < -200 or y > 200:
        aim.y = -aim.y
            
    if x < -185: 
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
    
    if x > 185: 
        low = state[2]
        high = state[2] + 50
        
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    ontimer(draw, velocidade)
    
    if keyboard.is_pressed('esc'):
        exit()
     
sc = turtle.Screen()
sc.setup(420, 420, None, None)
sc.title('Five Pong')
definir_velocidade()
definir_dificuldade()
definir_cor()
grava_historico()
escrita_Tela()
time.sleep(1.5)
hideturtle()
tracer(False)
mensagem.clear()
draw()
listen()
#placar()
onkeypress(lambda: move(1, 15), 'w')
onkeypress(lambda: move(1, -15), 's')
onkeypress(lambda: move(2, 15), 'Up')
onkeypress(lambda: move(2, -15), 'Down')
done()