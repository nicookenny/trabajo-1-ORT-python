socio1 = input("Ingresa el nombre del primer socio ")
capitalSocio1 = float(input("Ingresa el capital aportado por el primer socio "))

socio2 = input("Ingresa el nombre del segundo socio ")
capitalSocio2 = float(input("Ingresa el capital aportado por el segundo socio "))

socio3 = input("Ingresa el nombre del tercer socio ")
capitalSocio3 = float(input("Ingresa el capital aportado por el tercer socio "))


capitalTotal = capitalSocio1 + capitalSocio2 + capitalSocio3

porcentajeSocio1 = capitalSocio1 * 100 / capitalTotal
porcentajeSocio2 = capitalSocio2 * 100 / capitalTotal
porcentajeSocio3 = capitalSocio3 * 100 / capitalTotal

print(f"El capital aportado por el primer socio, {socio1}, es {capitalSocio1} ({porcentajeSocio1}%)")
print(f"El capital aportado por el segundo socio, {socio2}, es {capitalSocio2} ({porcentajeSocio2}%)")
print(f"El capital aportado por el tercer socio, {socio3}, es {capitalSocio3} ({porcentajeSocio3}%)")