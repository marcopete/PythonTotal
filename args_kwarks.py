def prueba(num1, num2, *args, **kwargs):

    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")

    total = 0
    # print(type(kwargs))
    for clave,valor in kwargs.items():
        print(f"{clave} es igual a {valor}")

args = [15,50,100,200,330,405]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(125,285,*args,**kwargs)

# prueba(15,50,100,200,330,405,x='uno',y='dos',z='tres')    

def cantidad_atributos(**kwargs):
    cantidad = len(kwargs)
    return cantidad

# Ejemplo de uso
resultado = cantidad_atributos(a=1, b=2, c=3)
print(resultado)

def lista_atributos(**kwargs):
    return list(kwargs.values())

# Ejemplo de uso
resultado = lista_atributos(a=1, b=2, c=3)
print(resultado)


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Ejemplo de uso
describir_persona("María", color_ojos="azules", color_pelo="rubio")

##################
def describir_persona(nombre,**describir_persona):

    print(f"Características de {nombre}:")

    for valor1, valor2 in describir_persona.items():

        print(f"{valor1}: {valor2}")