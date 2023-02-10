from io import open

def escribir_archivo():
    archivo = open("texto.txt","w")#open sirve para abrir un archivo, si no existe lo crear 
    #con w vamos a indicar que vamos a escribir
    archivo.write("Hola")
    archivo.write("\nAdios")
    archivo.close()


escribir_archivo() 
