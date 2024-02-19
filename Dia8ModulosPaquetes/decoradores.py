def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())        

mi_funcion = mayuscula

mi_funcion("jhgjhgfruytrfhyjgfhjgfhjgfhjgfjhgf")

def una_funcion(funcion):
    return funcion

una_funcion(mayuscula("wedwqexfqexfqexfqewdxqfwxe"))

def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == "min":
        return minuscula
    
operacion = cambiar_letras('may')
operacion2 = cambiar_letras('min')

operacion('okjnmonjouoionono')
operacion2('ESTE TEXTO ESTABA EN MAYUSCULAS, AHORA LO VES MINUSCULO POR LA FUNCION')
###########################################################################################
def decorar_saludo(funcion):

    def otra_funion(palabra):
        print('holaq')
        funcion(palabra)
        print('aDIOS')
    return otra_funion

def mayusculas2(texto):
    print(texto.upper())


def minusculas2(texto):
    print(texto.lower())

minusculas2('HJKGJKHSGFHJGFJHGFRJHGERFHJ')       
mayusculas2('hsdjfghjsdfgjhsdgfdjhsgfjhsdgfjhsdgfhjsdgjhsgd')

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada(' = mayuscula')

