
print("pasaje y tarjeta")

distancia = int(input("ingrese la distancia en (km): "))
categoria = int(input("ingrese la categoria que corresponde (1 al 5): "))

descuento_pasaje = 0

if distancia >= 400:
    if categoria == 1 or categoria == 2:
        descuento_pasaje = 20
    elif categoria == 3 or categoria == 4:
        descuento_pasaje = 14
elif distancia <= 200:
    if categoria == 1 or categoria == 2:
        descuento_pasaje = 12
    elif categoria == 3 or categoria == 4:
        descuento_pasaje = 8


descuento_tarjeta = 0

if categoria == 1 or categoria == 2 or categoria == 3:
    descuento_tarjeta = 10
elif distancia >= 300:
    descuento_tarjeta = 15

valor_pasaje = 95000 * (100 - descuento_pasaje) // 100
valor_tarjeta = 5000 * (100 - descuento_tarjeta) // 100

print(f"el valor del pasaje es de: ", valor_pasaje)
print(f"el valor de la tarjeta es de: ", valor_tarjeta)



