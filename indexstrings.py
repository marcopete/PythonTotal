mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
print(resultado)

resultado = mi_texto.index("prueba")
resultadoinverso = mi_texto.rindex("a")
print(resultado)
print(resultadoinverso)

texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[2:21:2]
print(fragmento)
fragmento = texto[::-1] #entrega la cadena al reves
print(fragmento)