#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

nota = float(input("Introduce tu nota: "))

if nota < 0 or nota > 10:
    print("Nota no válida. Por favor, introduce un número entre 0 y 10.")
elif nota >= 8.5:
    print("Tu nota es excelente.")
elif nota >= 6.5:
    print("Tu nota es notable.")
elif nota >= 5:
    print("Tu nota es satisfactoria.")
else:
    print("Tu nota es insuficiente.")