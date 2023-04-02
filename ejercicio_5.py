num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

print(f"num1 = {num1}; num2 = {num2}")
aux = num1
num1 = num2
num2 = aux
print(f"num1 = {num1}; num2 = {num2}")
