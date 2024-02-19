# def chequear_3_cifras(lista):

#     lista_3_cifras = []
    
#     for n in lista:
#         if n in range(100,1001):
#             lista_3_cifras.append(n)
#         else:
#             pass

#     return lista_3_cifras

# # suma = 586 + 402

# resultado = chequear_3_cifras([55,99,6000,11,158,8745,12,654])
# print(resultado)

def chequear_3_cifras(lista):
    numeros_3_cifras = []
    otros_numeros = []

    for n in lista:
        if 100 <= n <= 999:
            numeros_3_cifras.append(n)
        else:
            otros_numeros.append(n)

    resultado = "Los números de 3 cifras en la lista son: " + ', '.join(map(str, numeros_3_cifras))
    otros = "Los números que no son de 3 cifras son: " + ', '.join(map(str, otros_numeros))

    return resultado, otros

lista = [55, 99, 6000, 11, 158, 8745, 12, 654]
resultado, otros = chequear_3_cifras(lista)
print(resultado)
print(otros)
