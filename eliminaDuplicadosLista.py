def reducir_lista(lista):
    # Eliminar duplicados manteniendo el orden original
    lista_sin_duplicados = list(dict.fromkeys(lista))
    
    if lista_sin_duplicados:
        # Encontrar el valor más alto
        max_valor = max(lista_sin_duplicados)
        
        # Eliminar el valor más alto
        lista_sin_duplicados.remove(max_valor)
    
    return lista_sin_duplicados

def promedio(lista):
    if lista:
        # Calcular el promedio de la lista
        suma = sum(lista)
        promedio = suma / len(lista)
        return promedio
    else:
        return None

# Ejemplo de una lista llamada lista_numeros
lista_numeros = [1, 2, 15, 7, 2]

# Reducir la lista eliminando duplicados y el valor más alto
lista_reducida = reducir_lista(lista_numeros)

# Calcular el promedio de la lista reducida
resultado_promedio = promedio(lista_reducida)

print("Lista reducida:", lista_reducida)
print("Promedio de la lista reducida:", resultado_promedio)
