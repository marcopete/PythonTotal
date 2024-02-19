def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3

    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        # Calcular el número intermedio
        numeros = [num1, num2, num3]
        # numeros.remove(max(numeros))
        # numeros.remove(min(numeros))
        numeros.sort()
        # return numeros[0]
        return numeros[1]

# Ejemplos de uso
resultado_1 = devolver_distintos(5, 6, 7)
resultado_2 = devolver_distintos(2, 3, 6)
resultado_3 = devolver_distintos(4, 5, 6)

print(resultado_1)  # Devuelve el número intermedio (6)
print(resultado_2)  # Devuelve el número menor (2)
print(resultado_3)  # Devuelve el número mayor (6)
####################################################################
def letras_unicas_ordenadas(palabra):
    letras_unicas = sorted(set(palabra))
    return letras_unicas

# Ejemplo de uso
resultado = letras_unicas_ordenadas("entretenido")
print(resultado)

##################################
def verificar_doble_cero(*args):
    for contador in range(len(args) - 1):
        if args[contador] == 0 and args[contador + 1] == 0:
            return True
    return False

# Ejemplos de uso
resultado_1 = verificar_doble_cero(5, 6, 1, 0, 0, 9, 3, 5)
resultado_2 = verificar_doble_cero(6, 0, 5, 1, 0, 3, 0, 1)
resultado_3 = verificar_doble_cero(0, 6, 0, 5, 1, 0, 3, 0, 1, 0)

print(resultado_1)  # Devuelve True
print(resultado_2)  # Devuelve False
print(resultado_3)  # Devuelve False

####################################
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(n):
    primos = [num for num in range(2, n + 1) if es_primo(num)]
    for primo in primos:
        print(primo, end=' ')
    print()  # Imprime una línea en blanco para separar la lista de primos
    return len(primos)

# Ejemplo de uso
numero_dado = 20
cantidad_primos = contar_primos(numero_dado)
print(f"Encontré {cantidad_primos} números primos en el rango de 0 a {numero_dado}.")

