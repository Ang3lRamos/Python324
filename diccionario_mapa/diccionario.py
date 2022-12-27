numeros = {
    "Uno": 1,
    "Dos": 2,
    "Tres": 3,
    "Cuatro": 4,
    "Cinco": 5
}

print(numeros)

print(numeros["Cuatro"])

numeros["Cinco"] = 5 #Agregar un elemento

print(numeros)

print(numeros.get("Cuatr", "No se encontro")) #Para buscar un elemento

#Si encuentra la clave devuelve el valor si no devuelve el mensaje
#Si no hay mensaje no arroja error sino devulve none

print(numeros.keys()) #Retorna las claves del diccionario

print(numeros.values()) #Retorna los valores del diccionario

print(numeros.items()) #Retorna clave y valor del diccionario
print(" ")
print(numeros.pop("Cinco","No esta ese elemento")) #Elimina el elemento

print(numeros) 

for clave,valor in numeros.items():
    print(clave,"=",valor)

numeros.clear() #Elimina todo del diccionario

print(numeros)