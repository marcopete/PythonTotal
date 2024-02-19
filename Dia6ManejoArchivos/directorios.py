import os


ruta = os.getcwd()
print(ruta)

ruta = os.chdir('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos')
archivo = open('texto.txt')
print(archivo.read())

# crear carpeta
# ruta = os.makedirs('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/another')

# archivo = open('texto.txt')
# print(archivo.read())

ruta = '/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/Prueba.txt'

elemento = os.path.basename(ruta)
print(elemento)

ruta = '/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/Prueba.txt'

elemento = os.path.dirname(ruta)
print(elemento)

ruta = '/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/Prueba.txt'

elemento = os.path.split(ruta)
print(elemento)

# eliminar carpeta
# os.rmdir('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/another')

otro_archivo = open('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/texto.txt')
print(otro_archivo.read())