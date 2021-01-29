from random import randint
los = randint(1, 100)
while True:
    try:
        number = input("Zgadnij liczbę z zakresu od 1 do 100: ")
        number = int(number)
        if type(number) == int:
            if number < los:
                print("Za mało!")
            elif number > los:
                print("Za dużo!")
            else:
                print("Zgadłeś")
                break
    except ValueError:
        print("To nie jest liczba")