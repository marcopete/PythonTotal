import random

def juego_adivinanza():
    # Pedir el nombre del usuario
    nombre = input("Hola, ¿cuál es tu nombre? ")
    print(f"Bueno, {nombre}, he pensado en un número entre 1 y 100.")
    print("Tienes solo ocho intentos para adivinar cuál es.")

    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    intentos = 0
    while intentos < 8:
        intento = input("Introduce un número: ")
        
        # Verificar si la entrada es un número
        if not intento.isdigit():
            print("Debes ingresar un número válido.")
            continue
        
        intento = int(intento)

        # Verificar si el número está dentro del rango
        if intento < 1 or intento > 100:
            print("Has elegido un número que no está permitido. Debe estar entre 1 y 100.")
        else:
            intentos += 1

            # Comprobar si el número es igual al número secreto
            if intento == numero_secreto:
                print(f"¡Felicidades, {nombre}! Has adivinado el número secreto ({numero_secreto}) en {intentos} intentos.")
                break
            elif intento < numero_secreto:
                print("Tu respuesta es incorrecta. Has elegido un número menor al número secreto.")
            else:
                print("Tu respuesta es incorrecta. Has elegido un número mayor al número secreto.")

    if intentos == 8:
        print(f"Lo siento, {nombre}. Has agotado tus 8 intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    juego_adivinanza()
