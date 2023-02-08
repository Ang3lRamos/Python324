import Mi_paquete.funciones_aritmeticas as arit
def main():
    suma = arit.suma(1,2,3,4,5)
    resta = arit.restar(34,12)
    potencia = arit.potencia(2,4)

    print(f"La suma es {suma}")
    print(f"La resta es {resta}")
    print(f"La potencia es {potencia}")

if __name__ == '__main__':
    main()