div = 0
try:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    div = a/b
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("No se puede dividir entre una cadena")
except Exception as error:
    print("Ha ocurrido un error no previsto: " + type(error).__name__)#devuelve el nombre de la clase
    

print(f"La division es: {div}")