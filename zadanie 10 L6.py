n = int(input("Podaj liczbe"))
a, b = 0, 1
print("wyraz", 1, a)
print("wyraz", 2, b)
for i in range(1, n - 1):
    a, b = b, a + b
    print("wyraz", i + 2, b)
