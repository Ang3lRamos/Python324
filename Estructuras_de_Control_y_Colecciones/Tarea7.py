#Devolver la estación del año.
numero = int(input("Digite un numero: "))

if numero == 1:
    estacion = 'Verano'
elif numero == 2:
    estacion = 'Otoño'
elif numero == 3:
    estacion = 'Invierno'
elif numero == 4:
    estacion = 'Primavera'
else:
    estacion = 'ERROR'

print(estacion)