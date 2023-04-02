horasTrabajadas = int(input("Ingresa el número de horas trabajadas diariamente (en un día hábil): "))
precioHora = int(input("Ingresa el valor monetario por hora de trabajo: "))

horasSabado = horasTrabajadas / 2
horasHabiles = horasTrabajadas * 5

horasSemanales = horasSabado + horasHabiles

salario = precioHora * horasSemanales

print(f"El empleado gana semanalmente ${salario}")