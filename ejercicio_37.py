salarioCobrado = 0
mes = 1

salario = float(input(f"Ingresa el salario cobrado del mes {mes}: "))

while (salario > 0 and mes <= 12):
    salarioCobrado += salario
    mes += 1
    salario = float(input(f"Ingresa el salario cobrado del mes {mes}: "))

print(f"El salario cobrado hasta el momento es {salarioCobrado}")
