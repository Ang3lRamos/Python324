def saludar(nombre):    
    return f"Hola {nombre} desde la funcion saludar"

def sumar(a,b):
    return a + b

def restar(a = None,b = None):#Valores por defecto
    if a == None or b == None:
        return "Error"
    return a - b

#Los valores por defecto nos ayudan a que si al invocar la funcion no se envian parametros
#no va a mandar error

resta = restar(a= -10)#parametros por pocision
nombre = "Angel"
print(saludar(nombre))  

print(f"La suma es {sumar(10,20)}")

print(restar(10,20))