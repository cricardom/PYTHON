import random


def la_computadora_adivina_el_numero(x):

    print("BIENVENID@ AL JUEGO!!!")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo...")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "C":
        # Genear prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # tambien prodria ser el limite superior

            # Obtener respuesta del usuario
            respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()

            if repuesta == "a":
                limite_superior = prediccion - 1
            elif respuesta == "b":
                limite_inferior = prediccion + 1

    print(f"CORRECTO!!!! la computadora Adivino {prediccion}")

la_computadora_adivina_el_numero(10)