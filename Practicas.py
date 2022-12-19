# name = "Jhon"
# print(name[-3]) #Funciona de atras para adelante sin contar desde cero
# print(len(name))

"""
Enunciado: Dado un número de 5 dígitos, devolver el número en orden inverso.

Análisis: Para la solución de este problema, se requiere que el usuario ingrese un número n, 
luego el sistema procesa y obtiene el número inverso ni, realizando 4 divisiones sucesivas 
entre 10, para acumular el residuo y el último cociente. 
"""
# num = int(input("Digite el numero: "))

# #1
# residuo = num % 10
# num = num // 10
# numInverso = residuo * 10
# #2
# residuo = num % 10
# num = num // 10 
# numInverso = (numInverso + residuo) * 10
# #3
# residuo = num % 10
# num = num // 10 
# numInverso = (numInverso + residuo) * 10
# #4
# residuo = num % 10
# num = num // 10
# numInverso = (numInverso + residuo) * 10

# numInverso = numInverso + num

# print(f"Inverso: {numInverso}")

