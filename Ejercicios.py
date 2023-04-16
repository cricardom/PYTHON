import math
#Crear un programa modular que cacule el area de u trangulo valores de entrada por teclado
def calcularArea(a,b):
    area = (a  * b) / 2
    return area

print("Ingresar Altura")
a = float (input())
print("Ingresar Base")
b = float (input())

print("El area es: " + str(calcularArea(a, b)))


#Area de un circulo
def calcularAreaCirculo(r):
    area = math.pi * math.pow(r,2)
    return area

print("Ingresar radio")
r = float (input())

print("El Area Del Circulo es: " + str(calcularAreaCirculo(r)))


