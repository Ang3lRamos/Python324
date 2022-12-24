#El concepto de cola dice que el primer elemento en entrar es el primero en salir
#y el ultimo elemento en entrar va al final
#Para simular esto importaremos una libreria y un metodo proveniente de esta

from collections import deque

cola = deque([17,1.76,"Angel","Ingeniero"])

cola.append("5to semestre")

print(cola)

cola.popleft()

print(cola)

#y asi se simula una cola primero en entrar primero en salir, ultimo en entrar va al final


