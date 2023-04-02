
SUMA = "+"
RESTA = "-"
DIVISION = "/"
MULTIPLICACION = "*"
FIN = "F"


choice = input("Ingresa una opción: (+ | - | / | * | F): ")

if (choice != FIN):

    while (choice != FIN):

        if (choice != SUMA and choice != RESTA and choice != DIVISION and choice != MULTIPLICACION and choice != FIN):
            print("Por favor, ingresa una opción válida")
        else:

            num1 = int(input("Ingresa un número: "))
            num2 = int(input("Ingresa otro número: "))

            if (choice == SUMA):
                print(f"La suma entre {num1} + {num2} es {num1 + num2}")

            if (choice == RESTA):
                print(f"La resta entre {num1} - {num2} es {num1 - num2}")

            if (choice == MULTIPLICACION):
                print(
                    f"La multiplicación entre {num1} * {num2} es {num1 * num2}")

            if (choice == DIVISION):
                if (num2 == 0):
                    print(
                        "Debes ingresar un número válido; no se puede dividir por cero")
                else:
                    print(
                        f"La división entre {num1} / {num2} es {num1 / num2}")

        choice = input("Ingresa una opción: (+ | - | / | * | F): ")
