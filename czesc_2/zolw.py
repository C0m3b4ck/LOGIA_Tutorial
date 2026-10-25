from turtle import *
import turtle as t

t.speed(3)
t.color("brown")

t.forward(100)
t.backward(50)
t.right(90)
t.forward(100)
t.left(90)

t.pu()
t.penup()
t.forward(100)
t.pd()
t.pendown()
t.forward(100)

t.goto(100, 50)
t.forward(100)

t.home()
t.setheading(90)
t.forward(100)
t.circle(50)

t.forward(100)
t.dot(10)

t.fillcolor("blue")
t.colormode(255)
t.color(0, 0, 255)

t.begin_fill()
t.forward(100)

for i in range(3):
	t.right(90)
	t.forward(100)

t.end_fill()

t.done()

