# Hallar cuantos múltiplos de M hay en un rango de números enteros.
num = int(input("Digite el numero a: "))
num2 = int(input("Digite el numero b: "))
mult = int(input("Digite el numero multiplo: "))

contMult = 0

for i in range(num, num2):
    if i % mult == 0:
        contMult += 1
print(f"El numero {mult} en el rango {num} y {num2} tiene {contMult} multiplos")

