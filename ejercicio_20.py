num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

operacion = input("Ingresa la operación (+  -  /  *): ")

SUMA = "+"
RESTA = "-"
MULTIPLIACION = "*"
DIVISION = "/"

if(operacion == SUMA):
    print(f"El resultado de la suma es: {num1 + num2}")
elif (operacion == RESTA):
    print(f"El resultado de la resta es: {num1 - num2}")
elif (operacion == MULTIPLIACION):
    print(f"El resultado de la multiplicación es: {num1 * num2}")
elif (operacion == DIVISION):
    if(num2 == 0 ):
        print("No se puede dividir por CERO")
    else:
        print(f"El resultado de la división es: {num1 / num2}")
else:
    print("La división ingresada es inválida")

    