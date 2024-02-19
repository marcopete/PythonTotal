from datetime import datetime

mi_hora = datetime.time(17,35)
print(mi_hora)
print(mi_hora.min)

mi_dia = datetime.date(2025, 10, 17)

print(mi_dia)
print(mi_dia.year)
print(mi_dia.ctime())
print(mi_dia.today())

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)