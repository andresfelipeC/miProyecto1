import turtle
import math
from builtins import range

def makewindow(col,tit,x,y):
    turtle.setup(x,y)
    wn=turtle.Screen()
    wn.title(tit)
    wn.bgcolor(col)
    return wn
def maketurtle(col,sz):
    t=turtle.Turtle()
    t.color(col)
    t.pensize(sz)
    return t
    
def BEEPPERS1(x1,y1):
    beeper1.penup()
    beeper1.goto(x1,y1)
def BEEPER2(x2,y2):
    beeper2.penup()
    beeper2.goto(x2,y2)
    
def MundoKarel(t,lx):
    t.pendown()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    
    for i in range(4):
        t.forward(lx)
        t.left(90)
    t.penup()
    
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.pendown()
    for i in range(4):
        t.forward(320)
        t.left(90)
    t.penup()
    
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.pendown()
    
    for i in range(4):
        t.forward(240)
        t.left(90)
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.pendown()
    for i in range(4):
        t.forward(160)
        t.left(90)
        
    t.penup()
    
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.pendown()
    
    for i in range(4):
        t.forward(80)
        t.left(90)
    t.penup()
    
    t.forward(240)
    t.right(90)
    t.forward(160)
    t.right(90)
    t.forward(40)
    t.right(90)
    
    t.pendown()
    
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    #medio giro
    t.right(180)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(400) 
    t.penup()   
    t.left(90)
    t.forward(360)
    t.left(90)
    t.forward(40)
    t.color("black")
    t.pensize(10)
    
#BEGIINIG OF EXCECUTION
beeper1 = turtle.Turtle()
beeper1.color("black")
beeper1.pensize(1)
beeper1.shape("circle")

beeper2 = turtle.Turtle()
beeper2.color("black")
beeper2.pensize(1)
beeper2.shape("circle")

wn=makewindow("white", "KAREL EL ROBOT",500, 500)
t=maketurtle("blue", 3)
interfaz=MundoKarel(t, 400)
beeper1 = turtle.Turtle()
beeper1.color("black")
beeper1.pensize(1)
beeper1.shape("circle")

#Conectamos un click sobre la ventana

wn.onclick(BEEPPERS1)
wn.onclick( BEEPER2)
turtle.mainloop()




