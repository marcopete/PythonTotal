from pathlib import Path

carpeta = Path('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos')
archivo = carpeta / 'texto.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())