from datetime import datetime, date

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
#cambio a mes de noviemnbre en duro
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

nacimiento = date(1973, 9, 11)
defuncion = date(1990, 3, 11)

vida = defuncion - nacimiento

print(vida)
print(vida.days)

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme - despierta
print(f"Estuvo despierto {vigilia.seconds} segundos")

hoy = datetime.today().date()

# Acceder a la fecha actual almacenada en la variable hoy
print("Fecha actual:", hoy)

# Obtener la hora actual
hora_actual = datetime.now().time()

# Extraer los minutos de la hora actual
minutos = hora_actual.minute

# Imprimir los minutos
print("Minutos actuales:", minutos)