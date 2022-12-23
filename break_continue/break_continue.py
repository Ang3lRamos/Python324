c = 0

# while c < 10:
#     c += 1
#     print(c)
#     if c == 4:
#         print(c)
#         print("Se rompio el bucle")
#         break
# else:
#     print("Fin del while")


# while c < 10:
#     c += 1
#     print(c)
#     if c == 4:
#         print("Entro en el if")
#         continue #Todo lo que este luego de continue no se va a ejecutar
#     print("COntinue")
# else:
#     print("Fin del while")

dias = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
 
for dia in dias:
    if dia == "Lunes":
        continue
    elif dia == 'Viernes':
        break
    print(dia)