#Devolver la operación de los dos números según el operador ingresado.
operador = input('Operador: ')

numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))


if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    resultado = numero1 / numero2
else:
    resultado = "Error"
print(resultado)