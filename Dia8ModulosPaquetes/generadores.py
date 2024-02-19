def mi_funcion():
    print("mi_funcion")
    return 4

def mi_generador():
    for x in range(1, 5):
        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def mi_generador2():
    x = 1
    yield x
    x+=1
    yield x
    x+=1
    yield x

g2 = mi_generador2()

print(next(g2))
print(next(g2))
print(next(g2))

def mi_generador3():
    x = 0
    yield x
    while True:
        x += 1
        yield x
 
generador = mi_generador3()
 
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

# multiplos de 7
def mi_generador():
    num = 7
    while True:
        yield num
        num +=7
 
generador = mi_generador()

#######################################
def fun_generador2():
    vidas = 4
 
    while True:
 
        if vidas > 2:
            vidas -= 1
            yield f"Te quedan {vidas} vidas"
        elif vidas > 1:
            vidas -= 1
            yield f"Te queda {vidas} vida"
        else:
            yield f"Game Over"
 
 
perder_vida = fun_generador2()
# print(next(perder_vida))
# print(next(perder_vida))
# print(next(perder_vida))
# print(next(perder_vida))