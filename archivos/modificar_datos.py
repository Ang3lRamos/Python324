from io import open
from os import path

def modificar_datos():
    if path.isfile("texto.txt"):#verifica si el archivo existe
        archivo = open('texto.txt',"r+")#para leerlo con r y en modo escritura + = r+
        texto = archivo.readlines()
        print(texto)
        texto[1] = "Bo\n"
        print(texto)
        archivo.seek(0)#el puntero se ubica en el numero que le indiquemos, son caracteres
        archivo.writelines(texto)
        archivo.close()
        print(texto)
    else:
        print("No existe el archivo")

modificar_datos()