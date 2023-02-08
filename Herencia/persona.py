class Persona():

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def detalle_persona(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}" #muestra el estado del objeto por 
        #consola al llamar una instancia

#clase cliente que hereda de persona
class Cliente(Persona):
    pass

#clase empleado que hereda de persona

# class Empleado(Persona):

#     def __init__(self,nombre,edad,sueldo):
#         super().__init__(nombre,edad)#para traer lo del constructor d ela clase persona
#         self.sueldo = sueldo

#     def detalle_empleado(self):
#         super().detalle_persona()
#         print(f"Sueldo: {self.sueldo}")
    
#     def __str__(self):
#         return super().__str__() + f"\nSueldo: {self.sueldo}"

#herencia sin super

class Empleado(Persona):

    def __init__(self,nombre,edad,sueldo):
        Persona.__init__(self,nombre,edad)
        self.sueldo = sueldo

    def detalle_empleado(self):
        Persona.detalle_persona(self)
        print(f"Sueldo: {self.sueldo}")
    
    def __str__(self):
        return Persona.__str__(self) + f"\nSueldo: {self.sueldo}"


