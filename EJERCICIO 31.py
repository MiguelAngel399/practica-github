#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice. 

palabra_elegida = input("introduce la palabra que deseas buscar: ")
frase = "A quién madruga Dios ayuda."

print("Frase:", frase)
if palabra_elegida in frase:
    print(f"La palabra '{palabra_elegida}' se encuentra en la frase en la posición {frase.index(palabra_elegida)}.")
else:
    print(f"La palabra '{palabra_elegida}' no se encuentra en la frase.")