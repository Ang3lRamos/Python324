#Dado un número, determinar la cantidad de dígitos pares que contiene.

num = int(input("Digite un numero: "))

suma_digitos = 0
producto = 0
recorrido = 0
while num > 0:
    producto = num % 10
    if producto % 2 == 0:
        suma_digitos +=1
    num //= 10
print(suma_digitos)