import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif resultado_moneda == "Cruz":
        print("La lista fue salvada")
        return lista_numeros

# Crear una lista llamada lista_numeros (puedes agregar tus valores aquí)
lista_numeros = [1, 2, 3, 4, 5]

# Lanzar la moneda
resultado_moneda = lanzar_moneda()

# Probar suerte con el resultado de la moneda y la lista
nueva_lista = probar_suerte(resultado_moneda, lista_numeros)

print("Resultado de la moneda:", resultado_moneda)
print("Lista resultante:", nueva_lista)
