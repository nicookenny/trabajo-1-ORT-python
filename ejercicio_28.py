
cant = int(input("Ingrese la cantidad de números que desea ingresar: "))

max = float("-inf")
min = float("inf")
position = 0

for i in range(cant):
    num = int(input("Ingresa un número: "))
    if (max < num):
        max = num
        print(i)
        position = i+1

print(f"El mayor numero fue: {max} y apareción en la posición {position}")
