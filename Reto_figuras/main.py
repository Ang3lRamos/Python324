from figuras import Rectangulo,Circulo,probar_figura

def main():
    while True:
        opc = input("1: Para rectangulo, 2: Para circulo, 3: Para salir: ")
        if opc == "1":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            rectangulo = Rectangulo("Rectangulo",base,altura)
            probar_figura(rectangulo)
        elif opc == "2":
            radio = float(input("Digite el radio: "))
            circulo = Circulo("Ciruclo",radio)
            probar_figura(circulo)
        elif opc == "3":
            break
        else:
            print("Opcion invalida")
if __name__ == "__main__":
    main()