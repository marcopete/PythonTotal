# inicio = time.time()
# [código]
# final = time.time()
# duracion = final - inicio

# duracion = timeit.timeit(declaracion, setup, number = numero)

import time

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
prueba_for(150)
final = time.time()
tiempo = final - inicio
print(f"El for se demoro {tiempo}")

inicio = time.time()
prueba_while(150)
final = time.time()
tiempo = final - inicio
print(f"El while se demoro {tiempo}")