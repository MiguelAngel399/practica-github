#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales. 
import math
radio = float(input("Introduce el valor del radio del cilindro: "))
altura = float(input("Introduce el valor de la altura del cilindro: "))

area = round(2 * math.pi * radio * altura + 2 * math.pi * (radio ** 2), 2)
volumen = round(math.pi * (radio ** 2) * altura, 2)

print("El área del cilindro es:", area)
print("El volumen del cilindro es:", volumen)