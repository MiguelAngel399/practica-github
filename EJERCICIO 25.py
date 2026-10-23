# Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos. 
nota = float(input("Introduce tu nota: "))
if nota < 0 or nota > 10:
    print("Nota no válida. Por favor, introduce un número entre 0 y 10.")
else:
    if nota >= 8.5:
        print("Tu nota es excelente.")
    elif nota >= 6.5 and nota < 8.5:
        print("Tu nota es notable.")
    elif nota >= 5 and nota < 6.5:
        print("Tu nota es satisfactoria.")
    else:
        print("Tu nota es insuficiente.")