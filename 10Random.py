from random import *

aleatorio = randint(1,100)
print(aleatorio)

aleatorio = round(uniform(1,56),2)
print(aleatorio)

aleatorio = random()
# Un numero entre 0 y 1 (fraccion de un entero)
print(aleatorio)

colores = ['azul','rojo','verde','celeste']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)