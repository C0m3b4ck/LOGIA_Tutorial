import turtle as t
from turtle import *

def narysuj_kwadrat(dlugosc_boku, kolor_wnetrza, kolor_scian):
	t.color(kolor_scian)
	t.fillcolor(kolor_wnetrza)
	t.begin_fill()
	for i in range(4):
		t.right(90)
		t.forward(dlugosc_boku)
	t.end_fill()
	print("Zakonczono kwadrat!", dlugosc_boku, " ", kolor_wnetrza, " ", kolor_scian)

t.pensize(3)
narysuj_kwadrat(100, "brown", "green")
narysuj_kwadrat(50, "blue", "yellow")
narysuj_kwadrat(25, "green", "black")

t.hideturtle()
t.done()
