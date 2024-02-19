import zipfile
import shutil

'''
# crea archivo comprimido con 2 archivos dentro
# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# mi_zip.write(('mi_texto_A.txt'))
# mi_zip.write(('mi_texto_B.txt'))

# mi_zip.close()

# descomprime el archivo
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

zip_abierto.extractall()
'''

# usa shutil para comprimir y descomprimir todo lo que hay en carpeta_origen
carpeta_origen = '/home/mpuga/python/PythonProjects/PythonTotal/Dia9CollectionsMath'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('ProyectoDia9.zip')
