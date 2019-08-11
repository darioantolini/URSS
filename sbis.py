import turtle
from turtle import Turtle,Screen
import winsound

sfondo=Screen()
sfondo.colormode(255)
R=255
G=0
B=0
sfondo.bgcolor((R,G,B))
tarta=Turtle()
g=216
tarta.color((R,g,B))
tarta.width(2)

winsound.PlaySound("nfis",winsound.SND_ASYNC)
tarta.begin_fill()
tarta.left(120)
tarta.forward(25)
tarta.right(90)
tarta.forward(35) #sbis
tarta.right(90)
tarta.forward(75)
tarta.right(45)
tarta.forward(35*1.41) #sbis
tarta.right(135)
tarta.forward(37.5)
tarta.left(90)
tarta.forward(75)
tarta.left(90)
tarta.circle(125,90)
tarta.right(90)
tarta.forward(80)
tarta.right(90)
tarta.forward(25)
tarta.right(90)
tarta.forward(60)
tarta.right(90)
tarta.circle(150,-90)
tarta.right(90)
tarta.forward(50)
tarta.right(90)
tarta.forward(40)
tarta.right(90)
tarta.forward(50)
tarta.right(90)
tarta.circle(150,-135)
tarta.circle(123.5,145)
tarta.left(78.5)
tarta.forward(81.5)
tarta.end_fill()
turtle.done()
winsound.PlaySound(None,winsound.SND_NOWAIT)