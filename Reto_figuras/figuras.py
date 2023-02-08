import math
class Figuras():

    def __init__(self,nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass
    
    def __str__(self):
        return self.nombre


class Rectangulo(Figuras):
    def __init__(self,nombre,base,altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self):
        perimetro = 2 * self.base + 2 * self.altura
        return perimetro

    def __str__(self):
        return f"Nombre: {self.nombre}[Base: {self.base} Altura: {self.altura}]"

class Circulo(Figuras):
    def __init__(self,nombre,radio):
        super().__init__(nombre)
        self.radio = radio
    
    def area(self):
        area = math.pi * self.radio ** 2
        return f"El area del circulo es {area}"
    
    def perimetro(self):
        perimetro = math.pi * 2 * self.radio
        return f"El perimetro del circulo es {perimetro}"

    def __str__(self):
        return f"Nombre: {self.nombre}[Base: {self.base} Altura: {self.altura}]"
        
def probar_figura(figura):
    print(figura)
    print("Area: ",figura.area())
    print("Perimetro: ",figura.perimetro())