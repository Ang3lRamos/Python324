#crear una funcion que genere una contraseña aleatoria

import random

def contraAle():
    mayus = ["A","B","C","D","E","F","G","H","I","J"]
    min = ["a","b","c","d","e","f","g","h","i"]
    simb = ["!","·","#","%"]
    num = ["1","2","3","4","5","6","7","8","9"]

    carac = mayus + num + simb + min

    contra = []

    for i in range(10):
        formContra = random.choice(carac)
        contra.append(formContra)

    contra = "".join(contra)
    print(f"Su contraseña aleatoria es {contra}")

if __name__ == "__main__":
    contraAle()