#Dado dos números enteros diferentes, devolver el número Mayor.

num = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if num > num2:
    print(f"{num} es mayor que {num2}")
elif num < num2:
    print(f"{num2} es mayor que {num}")
else:
    print("Son iguales")
