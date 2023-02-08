from persona import Cliente, Empleado

# cliente1 = Cliente("Angel",18)

# cliente2 = Cliente("Francisco",19)

# cliente1.detalle_persona()

# print(cliente2)


empleado1 = Empleado("Angel",18,3500000)
empleado2 = Empleado("Francisco",20,6500000)
 
empleado1.detalle_persona() #al yo llamar este metodo no me muestra el sueldo ya que no se ha 
#definido en esta funcion

empleado2.detalle_empleado()

print(empleado2)