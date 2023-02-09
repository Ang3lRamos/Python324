c = 0
suma = 0

while c < 3:
    try:
        n = int(input("Ingrese un numero: "))
        suma += n
        c += 1
    except:
        print("Error")
    else:
        print("Todo funciona")
    finally: #se ejecuta al final de la ejecucion
        print("Fin de la ejecucion")


print(f"La suma total es: {suma}")
