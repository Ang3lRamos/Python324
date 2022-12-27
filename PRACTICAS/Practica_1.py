#Un restaurante ofrece un descuento del 10% para consumos de hasta $100 y un descuento del
#20% para consumos mayores, para ambos casos se aplican un impuesto del 19%.
#Determinar el monto del descuento y el importe a pagar.

#Añadir un descuento del 30% por un consumo mayor a $200
#Analisis
# Para la solucion de este problema se requiere que el usuario ingrese el consumo y el sistema 
# verifica y calcula en monto del descuento,impuesto y el total a pagar

print("="*31)

print("==========Bienvenido===========")

cuenta = float(input("Digite el valor de la cuenta: "))

if cuenta <= 0:
    print("===============================")
    print("Vuelva pronto")
    print("===============================")
elif cuenta <= 100:
    print("===============================")
    print("Su descuento es del 10%")
    print("===============================")
    dcto = cuenta * 0.1
    iva = cuenta * 0.19
    subTotal = cuenta - dcto
    total = subTotal + iva
    print((f"Iva: ${iva:.2f}"))
    print((f"Descuento ${dcto:.2f}"))
    print(f"Subtotal: ${subTotal:.2f}")
    print(f"Total: ${total:.2f}")
elif cuenta > 200:
    print("===============================")
    print("Su descuento es del 30%")
    print("===============================")
    dcto = cuenta * 0.3
    iva = cuenta * 0.19
    subTotal = cuenta - dcto
    total = subTotal + iva
    print((f"Iva: ${iva:.2f}"))
    print((f"Descuento ${dcto:.2f}"))
    print(f"Subtotal: ${subTotal:.2f}")
    print(f"Total: ${total:.2f}")
elif cuenta > 100:
    print("===============================")
    print("Su descuento es del 20%")
    print("===============================")
    dcto = cuenta * 0.2
    iva = cuenta * 0.19
    subTotal = cuenta - dcto
    total = subTotal + iva
    print((f"Iva: ${iva:.2f}"))
    print((f"Descuento ${dcto:.2f}"))
    print(f"Subtotal: ${subTotal:.2f}")
    print(f"Total: ${total:.2f}")


print("=====Gracias por su compra=====")
print("="*31)