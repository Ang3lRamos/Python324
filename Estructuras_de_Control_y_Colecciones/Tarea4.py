num = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

if num > num2 and num > num3:
    print(f"{num} es mayor")
elif num2 > num and num2 > num3:
    print(f"{num2} es mayor")
elif num3 > num and num3 > num2:
    print(f"{num3} es mayor")
else:
    print("Son iguales")