FIN = "*"


name = input("Ingresa el nombre de la persona: ")
age = int(input("Ingresa la edad de la persona: "))

younger = ""
youngerAge = 120

while (name != FIN):
    if (age < youngerAge):
        youngerAge = age
        younger = name

    name = input("Ingresa el nombre de la persona: ")
    age = int(input("Ingresa la edad de la persona: "))


print(younger)
