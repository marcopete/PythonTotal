from pathlib import Path

carpeta = Path('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/texto.txt')
# archivo = carpeta / 'texto.txt'
print(carpeta.read_text())
# mi_archivo = open(archivo)
# print(mi_archivo.read())