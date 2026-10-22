'''Juego sencillo'''
import random

numero_programa= random.randint(1,5)
numero_persona=int(input("Introduce tu valor pensado del 1 al 5: "))

if numero_persona > 1 and numero_persona < 5:
    if numero_persona==numero_programa:
            print("Has acertado, muy bien!!")
    
    else:
            print("No es correcto, prueba suerte otra vez")
else:
    print("Cambia el valor introducido")

    #Otra manera de hacerlo:
    '''Juego sencillo'''
import random

numero_programa= random.randint(1,5)
numero_persona=int(input("Introduce tu valor pensado del 1 al 5: "))

if numero_persona in [1,2,3,4,5] :
    if int(numero_persona)==numero_programa:
            print("Has acertado, muy bien!!")
    
    else:
            print("No es correcto, prueba suerte otra vez")
else:
    print("Cambia el valor introducido")