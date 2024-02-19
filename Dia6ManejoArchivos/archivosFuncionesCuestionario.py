def abrir_leer(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return f"El archivo {nombre_archivo} no se encontró."
    except Exception as e:
        return f"Error al abrir el archivo {nombre_archivo}: {str(e)}"

# Ejemplo de uso
nombre_archivo_ejemplo = "practicas_path.py"
contenido_archivo = abrir_leer(nombre_archivo_ejemplo)

# Imprime el contenido del archivo
print(f"Contenido del archivo {nombre_archivo_ejemplo}:\n{contenido_archivo}")

def sobrescribir(archivo):
    ruta = open(archivo,"w")
    ruta.write("contenido eliminado")
    ruta.close()
 
    ruta = open(archivo, "r")
    return ruta.read()

def registro_error(archivo):
    nuevo_registro = open(archivo, 'a')
    nuevo_registro.write('se ha registrado un error de ejecución')
    nuevo_registro.close()
 
    nuevo_registro = open(archivo, 'r')
    print(nuevo_registro)