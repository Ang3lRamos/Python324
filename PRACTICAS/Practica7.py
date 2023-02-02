#Adivina el numero
#crear un juego donde el sistema genere un numero aleatorio y el jugador intente adivinar
#el numero aleatorio

import random


def juego_Numero(vidas):

    numero_random = random.randint(0,100)#Elegimos el rango para elegir el numero
    numero_elegido = None #Variable para que el usuario elija un numero

    while numero_random != numero_elegido:
        numero_elegido = int(input("Digite un numero entre 0 y 100: "))

        if numero_random < numero_elegido:
            print("Pruebe un numero mas pequeño")
            vidas -= 1
        elif numero_random > numero_elegido:
            print("Pruebe un numero mas grande")
            vidas -= 1
        if vidas == 0:
            print("Game Over :(")
            print(f"El numero era {numero_random}")
            break
        print(f"Te quedan {vidas} vidas")
    if numero_elegido == numero_random:
        print("Muy bien has acertado :D")

def main():
    while True:
        menu = """
        Niveles
        Facil = 1
        Intermedio = 2
        Dificil = 3
        Salir = 4
        Digite una opcion: """
        opc = input(menu)
        if opc == "1":
            juego_Numero(7)
        elif opc == "2":
            juego_Numero(5)
        elif opc == "3":  
            juego_Numero(3)
        elif opc == "4":
            print("Adios")
            break
        else: print("Error")

if __name__ == "__main__":
    main()


