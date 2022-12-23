#Almacene en una lista 6 números y obtenga la cantidad de pares e impares.

lista = []

cont = 0

par = 0
impar = 0

while cont < 6:
    dig_num = int(input("Digite los numeros lista: "))
    lista.append(dig_num)
    cont += 1

for i in lista:
    if i % 2 == 0:
        par+=1
    else:
        impar +=1

print(f"La lista tiene {par} pares y {impar} impares.")