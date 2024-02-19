mi_archivo = open('Prueba.txt', encoding='cp1252', errors='surrogateescape')
# print(mi_archivo.read())

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.lower())

una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo3 = open('Prueba.txt', encoding='cp1252', errors='surrogateescape')
for l in mi_archivo3:
    print("Aqui dice: " + l)

mi_archivo2 = open('Prueba.txt', encoding='cp1252', errors='surrogateescape')
todas = mi_archivo2.readlines()
print(todas)

# with open('Prueba.txt', 'rb') as mi_archivo:
#     contenido_binario = mi_archivo.read()
#     try:
#         contenido_texto = contenido_binario.decode('utf-8')
#         print(contenido_texto)
#     except UnicodeDecodeError:
#         print("No se pudo decodificar el archivo con UTF-8. Puedes intentar con otra codificación o tratar los datos como bytes directamente.")
