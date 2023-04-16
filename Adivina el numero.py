import random


def adivina_el_numero(x):

    print("Bienvnid@ al juego")

    print("Adivine el numero generado por la computadora")

    numero_aleatorio = random.randint(1, x)

    prediccion = 0 

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina el numero entre 1 y {x}:  "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy grande.")

    print(f"Felicitaciones! Adivino el numero {numero_aleatorio} correctamente")


adivina_el_numero(1000)