#Modulo de numeros de fibonacci
def fibo(n):
    a,b = 0,1
    while a < n:
        print(a, end=' ') #El end no permite el salto de linea sino que imprime todo en una linea
        a,b = b, a + b
        #La secuencia de fibonacci suma el ultimo numero con el anterior y lo vuelve un nuevo valor
        #y asi sucesivamente
    print()

def fibo2(n):
    lista = []
    a,b = 0,1
    while a < n:
        lista.append(a)
        a,b = b, a + b
    return lista
