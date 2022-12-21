#Dado un rango de números enteros, obtener la cantidad de números pares que contiene.

num = int(input("Digite el numero inicial: "))
num2 = int(input("Digite el numero final: "))

suma = 0
rango = 0

rango = 1 + num
while rango < num2:
    if rango % 2 == 0:
        suma +=1
    rango+=1
print(suma) 