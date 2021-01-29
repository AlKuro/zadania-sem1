xd = []
def średnia():
    liczba = int(input("Podaj ilość wprowadzonych liczb: "))
    while True:
        a = int(input("Podaj liczbę dodatnią: "))
        if float (a) < 0:
            break
xd.append(a)
średnia = sum (xd) / liczba
print ("twoja srednia to %f ") % srednia()
