from random import randint

inferior = int(input("Ingrese límite inferior: "))
superior = int(input("Ingrese límite superior: "))

if inferior >= superior:
    print("El límite inferior debe ser menor que el superior.")
else:
    numero = randint(inferior, superior)
    ajustado = (numero // 3) * 3
    if ajustado < inferior:
        ajustado = inferior

    intento1 = int(input("Intente adivinar: "))
    if intento1 == ajustado:
        print("Felicitaciones, adivinó en el primer intento.")
    else:
        if ajustado > intento1:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        intento2 = int(input("Intente de nuevo: "))
        if intento2 == ajustado:
            print("Felicitaciones, adivinó en su segundo intento.")
        else:
            if ajustado > intento2:
                print("El número es mayor.")
            else:
                print("El número es menor.")

            print("Te daré una pista:")
            distancia_intento1 = abs(ajustado - intento1)
            distancia_intento2 = abs(ajustado - intento2)
            if dist1 < dist2:
                print("El número que buscas está más cerca de", intento1, "que de", intento2)
            elif dist2 < dist1:
                print("El número que buscas está más cerca de", intento2, "que de", intento1)
            else:
                print("Ambos intentos están igual de cerca.")

            intento3 = int(input("Intente la última vez: "))
            if intento3 == ajustado:
                print("Felicitaciones, pudiste adivinar.")
            else:
                print("Perdiste.")
                print("El número era:", ajustado)
