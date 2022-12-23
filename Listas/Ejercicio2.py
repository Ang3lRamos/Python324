#Ingrese 12 número en 3 listas (en cada lista con 4 números), y obtenga la suma de cada lista.

lista1 = []
lista2 = []
lista3 = []

cont1 = 0

while cont1 < 4:
    dig_num = int(input("Digite los numeros lista 1: "))
    lista1.append(dig_num)
    cont1 += 1
print("=======================================")
cont1 = 0
while cont1 < 4:
    dig_num = int(input("Digite los numeros lista 2: "))
    lista2.append(dig_num)
    cont1 += 1
print("=======================================")
cont1 = 0
while cont1 < 4:
    dig_num = int(input("Digite los numeros lista 3: "))
    lista3.append(dig_num)
    cont1 += 1
print("=======================================")
print(f"La suma de la primer lista es: {sum(lista1)}")
print(f"La suma de la segunda lista es: {sum(lista2)}")
print(f"La suma de la tercera lista es: {sum(lista3)}")
print(f"La suma de las listas es: {sum(lista1 + lista2 + lista3)}")
