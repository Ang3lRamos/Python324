#Obtener la suma de pares e impares de los primeros N números enteros positivos.

num = int(input("Digite un numero: "))

num += 1
par = 0
impar = 0
for i in range(1,num):
    if i % 2 == 0:
        par = i + par
    else:
        impar = i + impar
print(par)
print(impar)

