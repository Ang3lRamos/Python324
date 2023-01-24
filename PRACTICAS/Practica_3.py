#Crear un sistema que detecte s una palabra es palindroma

#Para solucionar este problema el usuario tiene que ingresar por pantalla una palabra y el
#sistema verifica si es palindromo

#Una palabra palindromo se lee igual de izquierda a derecha y al reves

def palindromo(palabra):
    palabra.replace(" ", "")
    palabra.upper()

    if palabra == palabra[::-1]:
        print(f"{palabra} es un palindromo")
    else:
        print(f"{palabra} no es un palindromo")

palabra = input("Digite una palabra o frase: ")

palindromo(palabra)