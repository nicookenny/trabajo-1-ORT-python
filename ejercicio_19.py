num = int(input("Ingresa un número"))

esDeUnSoloDigito = num <= 9
esImpar = num % 2 != 0

estaEnAmbosGrupos = esDeUnSoloDigito and esImpar
noEstaEnNingunGrupo = not esDeUnSoloDigito and not esImpar

print(f"El número ingresado es: {num}")

if(esDeUnSoloDigito):
    print("El número es de un solo digito")
else:
    print("El número no es de un solo digito")

if(esImpar):
    print("El número es impar")
else:
    print("El número no es impar")

if(estaEnAmbosGrupos):
    print("El número está en ambos grupos")
else:
    print("El número no está en ambos grupos")

    
if(noEstaEnNingunGrupo):
    print("El número no está en ningun grupo")
else:
    print("El número está en algún grupo")