#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo 
import math

a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

discriminante = b**2 - 4*a*c

if discriminante < 0:
    print("La ecuación no tiene soluciones reales.")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")