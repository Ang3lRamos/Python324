#Suma de los numeros anteriores al ingresado

num = int(input("Digite el numero: "))

suma = 0
num_menor = 0

while num_menor < num:
    suma += num_menor
    num_menor +=1
print(suma)