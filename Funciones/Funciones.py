def saludar():
    global nombre #definir una variable para que sea global dentro de una funcion

    nombre = "Angel"
    print("Holaaa",nombre)

saludar()
print("Holaaa",nombre) #para que se pueda usar la variable dentro de la funcion se debe haber 
#invocado la funcion(creo, 80% seguro)


# def variables():
#     global hola
#     hola = 2

# variables()
# print(hola + hola)    

