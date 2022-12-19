#Dado un número, devolver el doble si el número no es par, caso contrario el triple.
num = int(input("Digite el numero: "))

if num % 2 == 0:
    num *= 3
    print(num)
else:
    num *= 2
    print(num)