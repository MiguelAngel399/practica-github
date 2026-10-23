#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales 
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El primer número ({num1}) es mayor que el segundo ({num2}).")
elif num1 < num2:
    print(f"El primer número ({num1}) es menor que el segundo ({num2}).")
else:
    print(f"Los dos números ({num1} y {num2}) son iguales.")