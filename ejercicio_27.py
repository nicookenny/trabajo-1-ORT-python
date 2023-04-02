

counter = 0
accumulator = 0

for i in range(5):
    edad = int(input("Ingresa una edad"))
    accumulator += edad

    if (edad > 18 and edad % 2 != 0):
        counter += 1

print(f"El promedio de las edades es: {accumulator / 5}")
print(f"Se ingresaron {counter} edad/es impares mayores a 18")
