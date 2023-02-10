from io import open
from os import path

def agregar_datos():
    if path.isfile("texto.txt"):#verifica si el archivo existe
        archivo = open('texto.txt',"a")#para agregar datos usamos la a
        archivo.write("\nHola Angel")
        archivo.close()
    else:
        print("No existe el archivo")

agregar_datos()  