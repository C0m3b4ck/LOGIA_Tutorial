import turtle as t
from turtle import *

def narysuj_kwadrat(kolor, grubosc, szerokosc):
	t.pensize(grubosc)
	t.fillcolor(kolor)
	t.begin_fill()
	for i in range(4):
		t.right(90)
		t.forward(szerokosc)
	t.end_fill()

ilosc = int(input())

kolory = []
grubosci = []
szerokosci = []

for i in range(ilosc):
	kolor, grubosc, szerokosc = input().split()
	grubosc = int(grubosc)
	szerokosc = int(szerokosc)

	kolory.append(kolor)
	grubosci.append(grubosc)
	szerokosci.append(szerokosc)

for i in range(ilosc):
	narysuj_kwadrat(kolory[i], grubosci[i], szerokosci[i])

t.done()
