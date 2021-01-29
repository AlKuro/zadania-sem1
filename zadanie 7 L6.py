import random
q = 0
o = 0
tablica = []
liczby = list(range(1,49))
while(o<6):
    x = int(input("podaj liczbe pomiędzy 1 a 49: "))
    if x in liczby and x not in tablica:
        tablica.append(x)
        o = o+1
    else:
        print("podaj prawidlowa liczbe")
for z in range(0,6):
    p = random.randint(0,49)
    if p in tablica:
        q = q+1
if q<3:
    print("nic nie wygrales")
elif q == 3:
    print("wygrales 100zl")
elif q == 4:
    print("wygrales 10 000zl")
elif q ==5:
    print("wygrales 500 000zl")
elif q ==6:
    print("wygrales 10 000 000zl")
