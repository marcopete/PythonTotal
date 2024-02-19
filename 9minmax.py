menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor)
print(mayor)

lista = [58,96,72,64,35]
print(min(lista))

print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

nombres = ['juan','pablo','alicia','carlos']
print(min(nombres))

nombre = 'maRco'
# Min y max en strings comienzan su busqueda por 
# mayusculas y luego por minusculas, en el caso de maRco, min sera R y no m, para eso se usa .lower
print(min(nombre))
print(min(nombre.lower()))

dic = {'C1':45,'C2':11}
print(min(dic))
print(max(dic))
print(min(dic.values()))
print(max(dic.values()))