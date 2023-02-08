class Persona:
    __nombre = None #__ es para atributos privados
    __edad = None
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __metodo_privado(self):
        print('Soy un método privado')

    def get_nombre(self): #metodos usados para acceder a objetos privados los gets
        return self.__nombre

    def set_nombre(self, nombre): #metodos para modificar el valor de objetos privados los sets
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}'