#Obtener la suma de pares e impares de los primeros N números enteros positivos.

num = int(input("Digite un numero: "))
par = 0
impar = 0
for i in range(num):
    if i % 2 == 0:
        par += 1
    else:
        impar += 1