#Crear dos lista y una tupla que tendra numeros del 1 al 9.La primera lista se llamara
#pares y la segunda impar, ambos estaran vacios. Despues multiplica cada uno de los numeros
#de la tupla por un numero aleatorio entre 1 y 100, si el resultado es par guarda ese numero
# en la lista de pares y si es impar en la lista de impares. Muestra por consola la 
#multiplicacion que se produce junto con su resultado con el formato 2x3 = 6 y la lista de pares
#e impares

import random

par = []
impar = []

numeros = (1,2,3,4,5,6,7,8,9)


for i in numeros:
    numRandom = random.randrange(0,100)
    numMulti = i * numRandom
    if numMulti % 2 == 0:
        print(f"Multiplicacion {i} x {numRandom} = {numMulti}")
        par.append(numMulti)
    else:
        print(f"Multiplicacion {i} x {numRandom} = {numMulti}")
        impar.append(numMulti)

print(f"La lista de pares es: {par}")

print(f"La lista de impares: {impar}")

