#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice. 
frase = "A quién madruga Dios ayuda."
palabras = ["quién", "Dios", "ayuda", "madruga", ]
print("Frase:", frase)
for palabra in palabras:
    if palabra in frase:
        print(f"La palabra '{palabra}' se encuentra en la frase en la posición {frase.index(palabra)}.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en la frase.")