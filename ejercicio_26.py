num = int(input("Ingresa un número: "))

counter = 0
value = 1
while (counter < num):

    if (value % 3 == 0 and value % 5 != 0):
        print(value)
        counter += 1

    value += 1
