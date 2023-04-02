num1 = int(input("Ingresa el primer numero "))
num2 = int(input("Ingresa el segundo numero "))
num3 = int(input("Ingresa el tercer numero "))

if(num1 > num2 and num1 > num3):
    print(f"El número 1 ({num1}) es el mayor número")
elif (num2 > num1 and num2 > num3):
    print(f"El número 2 ({num2}) es el mayor número")
else:
    print(f"El número 3 ({num3}) es el mayor número")
