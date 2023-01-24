#crear una funcion que convierta de moneda nacional a dolares

#en este caso de pesos colombianos a dolares

def conver_moneda():
    dinero = float(input("Digite la cantidad de pesos a convertir: "))

    total = dinero * 0.00022

    return print(f"Tiene {total} dolares")

if __name__ == "__main__":
    conver_moneda()