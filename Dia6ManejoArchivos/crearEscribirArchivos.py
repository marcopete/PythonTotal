archivo = open('Prueba1.txt','w')
# 'w' hace que el archivo se sobreescriba si existe
archivo.write('Esta es la nueva linea\n')
archivo.write('Segunda linea\n')
archivo.write('''Tercera linea
sobre muchas
lineas''')
# write sobreescribe el archivo
archivo.close()

archivo = open('Prueba2.txt','w')
archivo.writelines(['hola','mundo','esta','es','una','lista'])
archivo.close()

archivo = open('Prueba3.txt','w')
lista = ['hola','mundo','esta','es','una','lista']

for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

archivo = open('Prueba1.txt','a')
archivo.write('welcome')
archivo.close()

# Abrir el archivo en modo escritura para cambiar su contenido
# with open("mi_archivo.txt", "w") as archivo:
#     archivo.write("Nuevo texto")

# # Volver a abrir el archivo en modo lectura para imprimir su contenido
# with open("mi_archivo.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)


# Abrir el archivo en modo escritura para añadir una línea al final
# with open("mi_archivo.txt", "a") as archivo:
#     archivo.write("Nuevo inicio de sesión")

# # Volver a abrir el archivo en modo lectura para imprimir su contenido
# with open("mi_archivo.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)



# Lista de valores
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# # Convertir la lista en una cadena con tabuladores
# linea_a_escribir = "\t".join(registro_ultima_sesion)

# # Abrir el archivo en modo escritura para escribir la línea
# with open("registro.txt", "a") as archivo:
#     archivo.write(linea_a_escribir + "\n")

# # Volver a abrir el archivo en modo lectura para imprimir su contenido
# with open("registro.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)
