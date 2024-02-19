nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42] 
ciudades = ['Lima', 'Madrid', 'México']

zipeada = list(zip(nombres,edades,ciudades))
print(zipeada)

for nombre, edad, ciudad in zipeada:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

    espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portug = ['um', 'dois', 'três', 'quatro', 'cinco']
english = ['one', 'two', 'three', 'four', 'five']
numeros = list(zip(espaniol, portug, english))
for espaniol, portug, english in numeros:
    print(f"{espaniol} {portug} {english}")