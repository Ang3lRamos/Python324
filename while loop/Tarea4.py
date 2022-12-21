#Dado un número, determinar cuantos dígitos tiene.

num = int(input("Digite un numero: "))

suma_digitos = 0

while num != 0:
    num //= 10
    suma_digitos +=1
print(suma_digitos)