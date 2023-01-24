text = "   Hola mundo   "

print(text.upper())#Mayusculas

print(text.lower())#Minusculas

print(text.capitalize())#COnvierte la primera en mayuscula

print(text.title()) #El primer caracter de cada palabra lo pone en mayuscula    

print(text.count("o")) #Cuenta la cantidad de caracteres especificos

print(text.replace("o","0")) #Modifica caracteres

print(text.strip()) #Quita los espacios al princio y final

text = "----Hola-mundo----"

print(text.strip("-")) #o lo que se le diga

print(text.split())#Convierte la cadena de caracteres en una lista sepaparada por los espacios

text = "Hola,Mundo,Desde,Python"

print(text.split(","))#Le podemos indicar bajo que parametros puede separar

print(text.islower()) #Retorna un booleano si todas son minusculas

print(text.isupper()) #Retorna un booleano si todas son minusculas

print(text.istitle()) #Retorna un booleano si su primera letra es mayuscula

print(text.isspace()) #Retorna un booleano si la cadena es de solo espacios

text = "   "

print(text.isspace())