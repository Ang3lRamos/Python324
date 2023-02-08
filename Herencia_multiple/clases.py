class Clase():
    def __init__(self):
        print("Soy la clase principal")

    def a(self):
        print("Metodo de la clase principal")

class Clase2():
    def __init__(self):
        print("Soy la segunda clase")

    def b(self):
        print("Metodo de la clase 2")

# class Clase3(Clase,Clase2):#el orden en que ponemos las clases afecta ya que la izquierda
#     #va a ser prioridad
#     def c(self):
#         print("Metodo de la clase 3")

class Clase3(Clase2,Clase):#el orden en que ponemos las clases afecta ya que la izquierda
    #va a ser prioridad
    def c(self):
        print("Metodo de la clase 3")