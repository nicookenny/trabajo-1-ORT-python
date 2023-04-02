def obtenerPuntaje(distancia):
    if (distancia == 0):
        return 500

    if (distancia <= 10):
        return 250

    if (distancia > 10 or distancia < 50):
        return 100

    return 0


jugadores = int(input("Ingrese la cantidad de jugadores: "))
TIROS = 3


if (jugadores < 2):
    print("Deben ser al menos dos jugadores")
else:
    nombreGanador = ""
    puntajeGanador = 0

    tirosCentro = 0

    for i in range(jugadores):
        nombreJugador = input("Ingrese su nombre: ")
        puntajeTotal = 0

        for j in range(TIROS):
            distancia = int(
                input("Ingrese la distancia al centro de su primer tiro: "))

            if (distancia == 0):
                tirosCentro += 1

            puntos = obtenerPuntaje(distancia)

            puntajeTotal += puntos

        if (puntajeTotal > puntajeGanador):
            nombreGanador = nombreJugador
            puntajeGanador = puntajeTotal

    print(
        f"El ganador es: {nombreGanador} con un puntaje de {puntajeGanador}. En total, hubieron {tirosCentro} tiros al centro.")
