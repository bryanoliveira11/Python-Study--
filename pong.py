from random import choice, random
from turtle import *
import turtle

from freegames import vector


def value():    
    """ valores aleatórios que mudam a velocidade da bola """
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


def move(player, change):
    """Move player position by change."""
    state[player] += change


def rectangle(x, y, width, height):
    """Draw rectangle at (x, y) with given width and height."""
    up()
    turtle.bgcolor('#F5AA8A')
    color('white','blue')
    goto(x,y)
    down()
    begin_fill()
    for count in range(10):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()


def draw():
    """Draw game and move pong ball."""
    clear()
    rectangle(-200, state[1], 15, 55)
    rectangle(190, state[2], 15, 55)
    #rectangle(620, state[1], 23,75)
    #rectangle(-653, state[2], 23,75)

    ball.move(aim)
    x = ball.x
    y = ball.y 

    up()
    goto(x,y)
    dot(23)
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

    ontimer(draw, 50)
    pen = Turtle()
    pen.goto(-110,0)
    pen.hideturtle()
    pen.write('INCRÍVEL MENSAGEM DE TESTE !',move='True',align='left',font=8)

setup(420, 420, 370, 0)
#screen = turtle.Screen()
#screen.setup(width = 1.0, height = 1.0)
hideturtle()
tracer(False)
listen()
onkeypress(lambda: move(1, 23), 'w')
onkeypress(lambda: move(1, -23), 's')
onkeypress(lambda: move(2, 23), 'i')
onkeypress(lambda: move(2, -23), 'k')
draw()
done()
