

promedio = 21
num = int(input("Ingresa un número: "))

acc = 0
count = 0

while (promedio > 20):
    count += 1
    acc += num

    promedio = acc / count

    if (promedio > 20):
        num = int(input("Ingresa un número: "))


print(f"El promedio es {promedio}")
print(f"Se ingresaron {count} números")
