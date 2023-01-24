def saludar():
    nombre = "Angel"
    edad = 18
    altura = 1.75
    return "Hola",nombre,edad,altura

angel = saludar()

saludo,nombre,edad,altura = saludar() #en el return hay 4 espacios por asi decirlo
#dependiendo de como ubiquemos las variables estas van a tomar los valores en orden de
#la funcion saludad

print(angel)

print(saludo)

print(nombre,edad)

#########################RECUERDA QUE DESPUES DEL RETURN DEJA DE LEER EL CODIGO############