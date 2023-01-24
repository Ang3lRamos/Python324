#Un solo asterisco es para denominar argumentos por posicion y dos es para argumentos 
# por nombre
def sumar(*args, **kwargs):#Se pone el asterisco para definir que son argumentos indefinidos
    suma = 0
    for i in args:
        suma+=i
    return suma,kwargs

print(sumar(1,2,3,4,4,nombre = "Angel",edad = 17))#Aqui se ven los argumentos 
#por pocision y por nombre

#El args es una tupla y el kwargs es un diccionario