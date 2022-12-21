#Dado un rango de números enteros num. inicial y num. final, obtener la cantidad de números 
# positivos y negativos que existen en el rango.

num = int(input("Digite el numero a: "))
num2 = int(input("Digite el numero b: "))

contPos = 0
contNeg = 0
nulo = 0

for i in range(num,num2):
    if i > 0:
        contPos +=1
    elif i < 0:
        contNeg +=1
    elif i == 0:
        nulo += 1
print(f"Hay {contPos} positivos,Hay {contNeg} negativos,Hay {nulo} nulos.")