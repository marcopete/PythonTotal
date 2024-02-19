import os
import shutil
# print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

# carpeta = Path('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos/texto.txt')

print(os.listdir())

shutil.move('curso.txt', "/home/mpuga/python")