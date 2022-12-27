a = set(
)

a = {"a","b","c"}

print(a)

a = {"a","b","c","a"} #No se permiten elementos repetidos, asi que a la hora de mostrar
#los elementos solo muestra un dato
print(a)

a = set("abracadabra1")

print(a,"elementos de a")

b = set("alakazam1")

print(b,"elementos de b")    

print(a - b, "elementos de a que no estan en b")

print(a|b,"letras de a y b")

print(a & b,"elementos en comun de a y b")

print(a ^ b,"muestra los elementos de a y b que no tienen ambos")   

a.add("Hola") #añadir elementos 
a.add("a")#si se añade un elemento que ya esta no lo agrega solo lo obvea
print(a)

a.discard("Hola")#elimina elementos
#si no se encuentra no manda error
print(a)

# a.clear() #eliminar todos los elementos del conjunto

print(a)