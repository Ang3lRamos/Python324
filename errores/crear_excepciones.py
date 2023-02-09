class Operador_excepcion(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)


def dividir(a,b):
    if b == 0:
        raise Operador_excepcion("No se puede dividir entre zero")
    else:
        return a / b

dividir(0,0)