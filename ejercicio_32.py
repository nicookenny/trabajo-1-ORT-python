

nota = int(input("Ingresa una nota: "))

while ((nota < 2 or nota > 10) or nota == 3):
    nota = int(input("Ingresa una nota válida (2, 4 - 10): "))


print(nota)
