from turtle import *


t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(3)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x,  y)
    t.pendown()

def setGreen():
    t.color('green')

def setRed():
    t.color('red')

def setBlue():
    t.color('blue')

def setYellow():
    t.color('yellow')

def setPurple():
    t.color('purple')

def stepRight():
    t.goto(t.xcor() +5, t.ycor())

def stepLeft():
    t.goto(t.xcor() -5, t.ycor())

def stepUp():
    t.goto(t.xcor(), t.ycor() +5)

def stepDown():
    t.goto(t.xcor(), t.ycor() -5)

def begin():
    t.begin_fill()

def end():
    t.end_fill()



t.ondrag(draw)
scr = t.getscreen()
scr.onscreenclick(move)
scr.listen()
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'f')
scr.onkey(setPurple, 'd')
scr.onkey(setRed, 's')
scr.onkey(setYellow, 'a')
scr.onkey(stepRight, 'Right')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(begin, 'w')
scr.onkey(end, 'e')
