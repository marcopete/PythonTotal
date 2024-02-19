import os
import shutil
import send2trash
# print(os.getcwd())

# archivo = open('curso.txt', 'w')
# archivo.write('texto de prueba')
# archivo.close()

# # carpeta = Path('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/texto.txt')

# print(os.listdir())

# shutil.move('curso.txt', "/home/mpuga/python")

print(os.walk('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/'))

ruta = '/home/mpuga/python/PythonProjects/PythonTotal/Dia9CollectionsMath/'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta {ruta}')
    print(f'Las subcarpets son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print(f'\n')

