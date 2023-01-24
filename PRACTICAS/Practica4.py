#crear una funcion que determine si el numero ingresado por consola es primo o no

def primalidad(num):
    cont = 0

    for i in range(1, num +1):
        if i == 1 or i == num:
            continue

        #Divide y si es modulo de 0 aumenta en uno el contador
        if num % i == 0:
            cont +=1
    if cont == 0:
        print(f"{num} es primo")
    else:
        print(f"{num} no es primo")
    



numero = int(input("Digite un numero: "))
primalidad(numero)