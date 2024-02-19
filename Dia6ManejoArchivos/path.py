from pathlib import Path

carpeta = Path('/home/mpuga/python/PythonProjects/PythonTotal/Dia6ManejoArchivos/archivosAlternativos')
archivo = carpeta / 'texto.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())


base = Path.home()
guia = Path("Barcelona", "Sagrada Familia.txt")
guia2 = Path(base,"Europa", "España", Path("Barcelona", "Sagrada Familia.txt"))
guia3 = guia2.with_name("La_Pedrera.txt")
print(base)
print(guia)
print(guia2)
print(guia3)
print(guia2.parent)
print(guia2.parent.parent)

guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espana = guia.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espana)


##################### 
guia = Path("Curso Python","Día 6","practicas_path.py")
ruta = guia.relative_to(Path())
print(ruta)

################
ruta = Path (Path.home(),"Curso Python","Día 6","practicas_path.py")
print(ruta)