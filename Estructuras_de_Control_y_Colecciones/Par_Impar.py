#recorrido de 0 a 20 diciendo si es par o impar
for i in (0,20):
    while i < 21:
        if i != 0: 
            if i % 2 == 0:
                print(f"{i} es par")
            else:
                print(f"{i} es impar")
        else:
            print(f"{i} es neutro")
        i += 1

#corroborar si un numero es par o impar
num = int(input("Digite el numero: "))

if num != 0: 
        if num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
else:
    print(f"{num} es neutro")