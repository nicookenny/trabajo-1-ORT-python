ventas = float(input("Ingresa el importe monetario de ventas realizadas por el empleado: "))
SUELDO_FIJO = 44000

comision = 0.16 * ventas
sueldoFinal = SUELDO_FIJO + comision

print(f"El salario percibido por el empleado es: {sueldoFinal}")