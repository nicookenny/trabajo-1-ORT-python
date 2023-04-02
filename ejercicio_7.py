ancho = float(input("Ingresa el ancho del predio: "))
largo = float(input("Ingresa el largo del predio: "))

precioM2 = float(input("Ingresa el precio por m2 del terreno: "))

VUELTAS_ALAMBRE = 3

area = ancho * largo
perimetro = ancho * 2 + largo * 2

precioTerreno = area * precioM2
metrosAlambre = perimetro * VUELTAS_ALAMBRE

print(f"El precio del terreno es {precioTerreno}")
print(f"Necesitas {metrosAlambre} para bordear el terreno con alambre")