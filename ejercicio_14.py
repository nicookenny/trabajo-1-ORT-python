altura = float(input("Ingresa tu altura"))
edad = float(input("Ingresa tu edad"))

EDAD_MINIMA = 7
ALTURA_MINIMA = 1.50


# Infierno
if(edad >= EDAD_MINIMA and altura <= ALTURA_MINIMA):
    print("Adelante, puede pasar a Infierno")
else:
    print("En Infierno no pasas... Vas a tener que volver en un tiempo, bro")

EDAD_MINIMA = 6

# Miedo a las alturas
if(edad > EDAD_MINIMA or altura > ALTURA_MINIMA):
    print("Adelante, puede pasar a Miedo a las alturas")
else:
    print("En Miedo a las alturas no pasas... Vas a tener que volver en un tiempo, bro")