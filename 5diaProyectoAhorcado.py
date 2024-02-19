import random

def choose_word():
    # Lista de palabras para elegir al azar
    palabras = ["python", "programacion", "ahorcado", "juego", "divertido", "tiburon"]
    return random.choice(palabras)

def display_word(word, guessed_letters):
    # Mostrar la palabra oculta con guiones bajos para las letras no adivinadas
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display

def get_user_guess():
    # Obtener una letra válida del usuario
    guess = input("Ingresa una letra: ").lower()
    while not guess.isalpha() or len(guess) != 1:
        print("Ingresa una letra válida.")
        guess = input("Ingresa una letra: ").lower()
    return guess

def play_hangman():
    # Configuración inicial
    palabra_secreta = choose_word()
    vidas = 6
    letras_adivinadas = []

    print("¡Bienvenido al Juego del Ahorcado!")
    print(display_word(palabra_secreta, letras_adivinadas))

    while vidas > 0:
        letra_usuario = get_user_guess()

        if letra_usuario in letras_adivinadas:
            print("Ya has adivinado esa letra. Inténtalo de nuevo.")
            continue

        letras_adivinadas.append(letra_usuario)

        if letra_usuario in palabra_secreta:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            vidas -= 1
            print(f"Incorrecto. Pierdes una vida. Te quedan {vidas} vidas")
            

        palabra_actual = display_word(palabra_secreta, letras_adivinadas)
        print(palabra_actual)

        if "-" not in palabra_actual:
            print("¡Felicidades! Has adivinado la palabra.")
            break

    if vidas == 0:
        print(f"Perdiste. La palabra era: {palabra_secreta}")

# Llamamos a la función principal para iniciar el juego
play_hangman()
