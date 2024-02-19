class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beeeee")

vaca = Vaca('Lola')
oveja = Oveja('Dolly')

animales = [vaca, oveja]

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca)
animal_habla(oveja)
#############################################################
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

nuevo = [palabra,lista,tupla]
 
for n in nuevo:
    print(len(n))
############################################
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Construir un iterable (lista) con los personajes en el orden deseado
personajes = [arquero, mago, samurai]

# Utilizar un iterador para realizar un ataque conjugado
for personaje in personajes:
    personaje.atacar()            
###########################################
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")
        
def personaje_defender(personaje):
    personaje.defender()

# Crear instancias de las clases
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Llamar a la función personaje_defender() con diferentes personajes
personaje_defender(mago)     # Salida: Escudo mágico
personaje_defender(arquero)  # Salida: Esconderse
personaje_defender(samurai)  # Salida: Bloqueo

from abc import ABC, abstractmethod
 
# Definición de la clase abstracta
class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
 
    @abstractmethod
    def perimetro(self):
        pass
 
# Clases derivadas
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
 
    def area(self):
        return self.lado ** 2
 
    def perimetro(self):
        return 4 * self.lado
 
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
 
    def area(self):
        return 3.1416 * self.radio ** 2
 
    def perimetro(self):
        return 2 * 3.1416 * self.radio
 
# Intentar instanciar la clase abstracta generará un error
# figura = FiguraGeometrica()
 
# Instanciar las clases derivadas
cuadrado = Cuadrado(5)
circulo = Circulo(3)
 
# Utilizar los métodos implementados en las clases derivadas
print("Área del cuadrado:", cuadrado.area())
print("Perímetro del cuadrado:", cuadrado.perimetro())
 
print("Área del círculo:", circulo.area())
print("Perímetro del círculo:", circulo.perimetro())