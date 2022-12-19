precio = float(input("Difite el valor del producto: "))

iva = precio * 0.19
iva_producto = precio + iva 

print("="*25)
print("----FACTURA----")
print(f"El iva es {iva}")
print(f"El precio del producto es {precio}")
print(f"El precio final del producto es {iva_producto}")
print("---------------")
print("="*25)