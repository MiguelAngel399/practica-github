#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine. 

numero_menores = int(input("Introduce el número de menores: "))
numero_adultos = int(input("Introduce el número de adultos: "))

total_menores = numero_menores * 12 * 0.5
total_adultos = numero_adultos * 12 * 0.9
total_pagar = total_menores + total_adultos

print("Total a pagar por menores:", total_menores, "euros")
print("Total a pagar por adultos:", total_adultos, "euros")
print("El total a pagar es:", total_pagar, "euros")
