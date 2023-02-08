import sys #Recupera lo que se envia como argumento a la hora de ejecutar el script
# en una lista

if len(sys.argv) == 3:
    texto = sys.argv[1]
    cantidad = sys.argv[2]

    cont = 0
    while cont < cantidad:
        print(texto)
        cont+=1
else:
    print("Error, Argumentos invalidos")
    print("Ejemplo: entrada_datos_script 'Texto' 5")