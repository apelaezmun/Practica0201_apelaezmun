#Escribir un programa que pregunte al usuario por el número de horas
#trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que
#le corresponde.
Horas = int(input('Horas trabajadas:'))
print(Horas)
CosteHora = int(input('¿Cuanto cuesta la hora trabajada?'))
print(CosteHora)
paga = (CosteHora * Horas)
print(paga)