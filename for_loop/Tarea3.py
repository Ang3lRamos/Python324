#Dado 2 números diga si son amigos o no, recuerde que dos números son amigos si la suma de sus 
# divisores de uno de ellos es igual al otro y viceversa, por ejemplo 220 y 284 son amigos.

num = int(input("Digite el numero a: "))
num2 = int(input("Digite el numero b: "))

cont1 = 0
resultado = 0

cont2 = 0
resultado2 = 0
for i in range(1,num):
    resultado = num % i
    if resultado == 0:
        cont1 += i

for i in range(1,num2):
    resultado2 = num2 % i
    if resultado2 == 0:
        cont2 += i
        
if num == cont2 and num2 == cont1:
    resultado = "Son amigos"
else:
    resultado = "No son amigos"

print(resultado)