# Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas no distinguir entre mayúsculas y minúsculas
import string

palabra_elegida = input("introduce la palabra que deseas buscar: ")
oracion = "A quién madruga Dios ayuda."

print("Frase:", oracion)
if palabra_elegida.lower() in oracion.lower():
    print(f"La palabra '{palabra_elegida}' se encuentra en la frase en la posición {oracion.lower().index(palabra_elegida.lower())}.")
else:
    print(f"La palabra '{palabra_elegida}' no se encuentra en la frase.")