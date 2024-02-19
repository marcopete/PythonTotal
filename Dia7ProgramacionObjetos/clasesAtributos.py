class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # def __init__(self, mi_parametro):
    #     self.atributo = mi_parametro    


mi_pajaro = Pajaro('negro', 'Tucan')

# print(mi_pajaro.atributo)
# print(mi_pajaro.color)

print(f"Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)


class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

# Crear una instancia de Casa llamada casa_blanca
casa_blanca = Casa(color="blanco", cantidad_pisos=4)

# Acceder a los atributos de la instancia
print(f"Color de casa_blanca: {casa_blanca.color}")
print(f"Cantidad de pisos de casa_blanca: {casa_blanca.cantidad_pisos}")

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color    
        
cubo_rojo = Cubo(color="rojo")
print(f"Cubo de color: {cubo_rojo.color}")

class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico    
        self.edad = edad
        
harry_potter  = Personaje(especie="Humano", magico=True, edad=17)
print(f"El personaje Harry Potter es {harry_potter.especie}, del tipo {harry_potter.magico} y de {harry_potter.edad} años")