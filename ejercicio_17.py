edad = int(input("Ingresa tu edad: "))
genero = input("Ingresa tu género: ").upper()[0]

JUBILACION_M = 65
JUBILACION_F = 60

if (genero != "M" and genero != "F"):
    print("Debes ingresar un género válido")
else:
    if (edad > 120 or edad < 1):
        print("Debes ingresar una edad válida")
    else:
        if (genero == "M"):
            if (edad >= JUBILACION_M):
                print("Te podes jubilar, Edgardo")
            else:
                print("Edgardo, segui laburando")
        else:
            if (edad >= JUBILACION_F):
                print("Te podes jubilar, Juana")
            else:
                print("Juana, segui laburando")
