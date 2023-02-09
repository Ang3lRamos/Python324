def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre zero")
    else:
        return a / b

dividir(0,0)