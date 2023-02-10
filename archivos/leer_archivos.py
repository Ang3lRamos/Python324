from io import open
from os import path

def leer_archivo():
    if path.isfile("texto.txt"):#verifica si el archivo existe
        archivo = open('texto.txt',"r")#para leerlo con r
        # texto =  archivo.read()
        texto =  archivo.readline()#lee una linea, la primera
        texto2 = archivo.readlines()#lee todas las lineas y retorna una lista
        print(texto)
        print(texto2)
        archivo.close()
    else:
        print("No existe el archivo")

leer_archivo()