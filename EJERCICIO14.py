#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal. import math
import math

diametro = float(input("Introduce el diámetro del círculo: "))
radio = diametro / 2
area = round(math.pi * (radio ** 2), 1)
perimetro = round(2 * math.pi * radio, 1)

print("El área del círculo es:", area )
print("El perímetro del círculo es:", perimetro)
