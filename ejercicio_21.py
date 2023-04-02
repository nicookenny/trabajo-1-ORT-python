dia = int(input("Ingresa un número del 1 al 7 => refriendo al día de la semana: "))

DOMINGO = "DOMINGO"
LUNES = "LUNES"
MARTES = "MARTES"
MIERCOLES = "MIERCOLES"
JUEVES = "JUEVES"
VIERNES = "VIERNES"
SABADO = "SABADO"

if(dia < 1 or dia > 7):
    print("El día ingresado está fuera de rango, debe ser del 1 al 7")
else:

    if (dia == 1):
        print(DOMINGO)

    if (dia == 2):
        print(LUNES)

    if (dia == 3):
        print(MARTES)

    if (dia == 4):
        print(MIERCOLES)

    if (dia == 5):
        print(JUEVES)

    if (dia == 6):
        print(VIERNES)

    if (dia == 7):
        print(SABADO)
    