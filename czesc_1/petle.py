ilosc = input()
ilosc = int(ilosc)

for i in range(ilosc):
	print(i)

wartosc = 0
while (wartosc < ilosc):
	tmp = 1
	wartosc = wartosc + tmp
	print("dodano do wartosc")

print(wartosc, tmp)
