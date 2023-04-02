

altura = float(
    input("Ingresa la edad del basquetbolista: (al terminar, ingresa 0): ")
)

accumulator = 0
count = 0

while (altura != 0):
    accumulator += altura
    count += 1
    altura = float(
        input("Ingresa la edad del basquetbolista: (al terminar, ingresa 0): ")
    )

print(
    f"La altura promedio de los {count} basquetbolistas es {accumulator / count}")
