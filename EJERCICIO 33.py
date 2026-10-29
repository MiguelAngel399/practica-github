#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
frase = "No hay mal que dure cien años"
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
contador = 0   
vocales_a = 0
vocales_e = 0
vocales_i = 0
vocales_o = 0
vocales_u = 0
for letra in frase:
    if letra in vocales:
        contador += 1
        if letra == 'a' or letra == 'A':
            vocales_a += 1
        elif letra == 'e' or letra == 'E':
            vocales_e += 1
        elif letra == 'i' or letra == 'I':
            vocales_i += 1
        elif letra == 'o' or letra == 'O':
            vocales_o += 1
        elif letra == 'u' or letra == 'U':
            vocales_u += 1

print(f"El número de vocales en la frase es: {contador}. El numero de a es: {vocales_a}, el numero de e es: {vocales_e}, el numero de i es: {vocales_i}, el numero de o es: {vocales_o}, el numero de u es: {vocales_u}.")
