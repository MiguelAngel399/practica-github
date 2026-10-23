#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
while True:
    num1 = float(input("Introduce el primer número (entre 0 y 10): "))
    if 0 <= num1 <= 10:
        break
    print("Número no válido. Por favor, introduce un número entre 0 y 10.")

while True:
    num2 = float(input("Introduce el segundo número (entre 0 y 10): "))
    if 0 <= num2 <= 10:
        break
    print("Número no válido. Por favor, introduce un número entre 0 y 10.")

if num1 > num2:
    print(f"El primer número ({num1}) es mayor que el segundo ({num2}).")
elif num1 < num2:
    print(f"El primer número ({num1}) es menor que el segundo ({num2}).")
else:
    print(f"Los dos números ({num1} y {num2}) son iguales.")