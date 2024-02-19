from pathlib import Path, PurePath, PureWindowsPath

carpeta = Path('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/texto.txt')
# archivo = carpeta / 'texto.txt'
print(carpeta.read_text())
# nombre archivo
print(carpeta.name)
# sufijo
print(carpeta.suffix)
# sin terminacion
print(carpeta.stem)
# ve si archivo existe
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("El archivo existe, la raja")
# ruta windows    
rutaWindows = PurePath(carpeta)
print(rutaWindows)

rutaWindows = PureWindowsPath(carpeta)
print(rutaWindows)

# mi_archivo = open(archivo)
# print(mi_archivo.read())