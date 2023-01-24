#Son funciones anonimas que son usadas para una epresion pequeña o cortas

#def sumar(a,b): #En casos asi podemos usar las funciones lambda ya que son expresiones cortas
#    return a + b

sumar = lambda a,b: a + b

duplicar = lambda a: a*2

par_impar = lambda a: a % 2 == 0 #nos retorna un booleano

revertir_cadena = lambda a: a[::-1]
print(sumar(10,20))

print(duplicar(4))

print(par_impar(5))

print(revertir_cadena("Hola"))