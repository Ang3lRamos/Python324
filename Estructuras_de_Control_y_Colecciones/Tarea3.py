#Determinar si un número entero es par o impar.

num = int(input("Digite el numero: "))

if num != 0: 
        if num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
else:
    print(f"{num} es neutro")