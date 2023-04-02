

num = int(input("Ingresa un número (si deseas terminar, ingresa un 0): "))

max = float("-inf")
min = float("inf")

print(min, max)
while (num != 0):
    if (max < num):
        max = num

    if (min > num):
        min = num

    num = int(input("Ingresa otro número: "))


print(f"El máximo número ingresado fue {max} y el mínimo {min}")
