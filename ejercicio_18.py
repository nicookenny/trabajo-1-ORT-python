num1 = int(input("Ingresa un número"))
num2 = int(input("Ingresa otro número"))

if(num1 > num2):
    es_divisible = num1 % num2 == 0

    if(es_divisible):
        print("El primer numero es divisible por el segundo")
    
else:

    es_divisible = num2 % num1 == 0

    if(es_divisible):
        print("El segundo numero es divisible por el primero")

