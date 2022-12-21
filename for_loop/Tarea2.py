#Crea un algoritmo que indique si un número es perfecto o no.

num = int(input("Digite el numero: "))

suma = 0
for i in range(1,num):
    if num % i == 0:
        suma += i
    if num == suma:
        contar = "Perfecto"
    else:
        contar = "No perfecto"
print(contar)