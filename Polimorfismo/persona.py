class Persona(object):
    def __init__(self,nombre):
        self.nombre = nombre

    def moverse(self):
        print(f"{self.nombre}, Persona caminando")

class Atleta(Persona):
    
    def moverse(self):
        print(f"{self.nombre}, Atleta corriendo")

class Ciclista(Persona):

    def moverse(self):
        print(f"{self.nombre}, Ciclista montando cicla")