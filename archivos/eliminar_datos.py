from io import open
from os import path

def eliminar_datos():
    archivo = open("texto.txt","w")
    archivo.close()

eliminar_datos()