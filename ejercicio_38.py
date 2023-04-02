USUARIO = "admin"
PASSWORD = "123456"

accesoConcedido = False

intentos = 1


while (intentos <= 3 and accesoConcedido == False):
    user = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa su contraseña: ")

    if (user == USUARIO and password == PASSWORD):
        print("Acceso concedido")
        accesoConcedido = True
    else:

        if (intentos + 1 == 4):
            print("Se ha bloqueado la cuenta")
        else:
            print(f"ERROR: Te quedan {3 - intentos} intentos")

        intentos += 1
