#Esto es una funcion recursiva y lo que hace es ejecutarse a si misma ya que dentro de
# esta funcion esta ella misma
def factorial(n):
    if n > 1:
        n = n * factorial(n - 1)
    return n

n = int((input("Digite un numero: ")))
print(f"El factorial de {n} es {factorial(n)}")
