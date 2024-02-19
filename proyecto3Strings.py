texto = input("Ingresa un texto a eleccion de cualueri tamaño: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower()) 
letras.append(input("Ingresa la segunda letra: ").lower()) 
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("Cantidad de leteras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Encontramos la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Encontramos la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Encontramos la letra {letras[2]} repetida {cantidad_letras3} veces")

print("\n")
print("Cantidad de alabras")
palabras = texto.split() # palabras es de tipo lista
print(f"Hemos encontrado {len(palabras)} palabras en tu tecto")

print("\n")
print("Letras de inicio y fin")
letra_inivio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inivio}' y la letra final es '{letra_final}'")

print("\n")
print("Texto invertifo")
palabras.reverse()
textoInvertido = ' '.join(palabras)
print(f"Si ordenamos el texto al reves se ve: {textoInvertido}")

print("\n")
print("Buscando la palabra python")
buscarPython = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'python' {dic[buscarPython]} se encuentra en el texto")