#Obtener la cantidad de los primeros números múltiplos de 5.

num = int(input("Digite el numero: "))

recorrido = 0
suma = 0

while recorrido <= num:
    recorrido += 1
    if recorrido % 5 == 0:
        suma += 1
print(suma)
