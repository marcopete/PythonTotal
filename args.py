def suma(*args):
    ## Metodo 1
    # total = 0

    # for arg in args:
    #     total += arg

    # return total

    ## Metodo 2
    return sum(args)

print(suma(5,6,10,100,346))

def suma_cuadrados(*args):
    return sum(x**2 for x in args)

# Ejemplo de uso
resultado = suma_cuadrados(1, 2, 3)
print(resultado)

def suma_absolutos(*args):
    return sum(abs(x) for x in args)

# Ejemplo de uso
resultado = suma_absolutos(-1, 2, -3, 4)
print(resultado)

def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

# Ejemplo de uso
resultado = numeros_persona("Juan", 1, 2, 3)
print(resultado)