tasa_interes = float(input("Digite la tasa de interes: "))
periodo = float(input("Digite el periodo: "))
capital = float(input("Digite el capital: "))

interes_compuesto = ((1+tasa_interes/100)**periodo)*capital
interes = (interes_compuesto-capital)


print(f"El interes es {interes:.2f} y el monto es {interes_compuesto:.2f}")