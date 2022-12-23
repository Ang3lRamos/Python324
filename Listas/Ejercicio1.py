#Ingrese 6 números en una lista y obtenga el número mayor y menor ingresado.

numeros = []

cont = 0

while cont < 6:
    dig_numeros = int(input("Digite los numeros: "))
    numeros.append(dig_numeros)
    cont += 1

num_min = num_max = numeros[0]

for numeros in numeros:
    if numeros < num_min:
        num_min = numeros
    elif numeros > num_max:
        num_max = numeros
print(num_max, num_min)
