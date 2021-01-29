import random

tab1 = []
tab2 = []
powt = 0
x = int(input("Podaj początek zakresu: "))
z = int(input("Podaj koniec zakresu: "))
for a in range(x,z + 1):
    tab1.append(a)
print(tab1)
print(tab1[-3])
k = int(input("Podaj element, który chcesz usunąć: "))
tab1.pop(k)
for a in range(x,z):
    tab2.append(a)
tabsum = tab1 + tab2
print(tabsum)
for i in range(len(tabsum) + 1):
    if tabsum.count(i) > 1:
        powt += 1
    i += 1
print(len(tabsum))
print(powt)
