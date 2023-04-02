inscriptos = int(input("Ingrese la cantidad de inscriptos a la conferencia: "))
asientosDisponibles = int(input("Ingrese la cantidad de asientos disponibles para la conferencia: "))

if(inscriptos <= asientosDisponibles):
    print("Perfecto, todos tienen un asiento :)")
    if(inscriptos < asientosDisponibles):
        print(f"Quedan {asientosDisponibles - inscriptos} asientos libres")
else:
    asientosFaltantes = inscriptos - asientosDisponibles
    print(f"No todos tienen asiento, {asientosFaltantes} personas deberán permanecer paradas")