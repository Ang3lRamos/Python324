import sys


if len(sys.argv) == 4:
    nombre = sys.argv[1]
    edad = sys.argv[2]
    altura = sys.argv[3]

    # print(f"Nombre: \n{nombre}, \nEdad: {edad}, \nAltura: {altura}")
    # print("Nombre: {}, \nEdad: {}, \nAltura: {}".format(nombre, edad, altura))
    # print("Nombre: {n}, \nEdad: {e}, \nAltura: {a}".format(a = altura ,n = nombre, e = edad ))
    print("Nombre: %s {nombre}, \nEdad: %i , \nAltura: %f"%(nombre,edad,altura))
    
else:
    print("Error, Argumentos invalidos")
    print("Ejemplo: entrada_datos_script 'Texto' 5")