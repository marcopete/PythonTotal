import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        mensaje = "Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        mensaje = "Tienes buenas chances"
    else:
        mensaje = "Parece una jugada ganadora"

    resultado = f"La suma de tus dados es {suma_dados}. Dado 1: {dado1}, Dado 2: {dado2}. {mensaje}"
    return resultado

# Lanzar los dados y obtener los resultados
resultado_dado1, resultado_dado2 = lanzar_dados()

# Evaluar la jugada y obtener el mensaje
mensaje = evaluar_jugada(resultado_dado1, resultado_dado2)

# Imprimir el mensaje
print(mensaje)
