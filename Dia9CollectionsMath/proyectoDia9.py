import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = '/home/mpuga/python/PythonProjects/PythonTotal/Dia9CollectionsMath/Mi_Gran_Directorio'

mi_patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()
nros_encontrados = []

archivos_encontrados = []

def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), mi_patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encotrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear_listas()
mostrar_todo()


# from os import walk
# import os.path
# import re
# from datetime import datetime
# from time import time
# from math import ceil
 
# formato = '%d-%m-%y'
# fecha = datetime.today()
# fecha = fecha.strftime(formato)
 
# contador = 0
 
# ruta = "/home/mpuga/python/PythonProjects/PythonTotal/Dia9CollectionsMath/Mi_Gran_Directorio"
# patron = 'N'+r'\D{3}'+'-'+r'\d{5}'
# linea = '-'*32
# linita = '-'*13
# print(linea)
# print(f'Fecha de Búsqueda: {fecha}\n')
# print("Archivo \t\tN° de Serie")
# print('-'*13+'   '+'-'*11)
# inicio = time()
# for carpeta,subcarpetas,archivos in walk(ruta):
#     for ar in archivos:
#         archivo = open(os.path.join(carpeta,ar))
#         texto = archivo.read()
#         buscar = re.search(patron, texto)
#         if buscar:
#             print(f'{ar}\t{buscar.group()}')
#             contador +=1
# final = time()
# duracion = final - inicio
 
 
# print(f'\nNúmeros encontrados: {contador}')
# print(f'Tiempo de búsqueda: {ceil(duracion)}')
# print(linea)