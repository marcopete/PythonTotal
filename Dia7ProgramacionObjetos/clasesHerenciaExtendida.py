class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal ha emitido un sonido")        

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        # self.edad = edad
        # self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

print (Pajaro.__bases__)
print (Animal.__subclasses__())

piolin = Pajaro(3, 'amarillo', 60)
mi_animal = Animal(5, 'negro')

piolin.nacer()
piolin.hablar()
piolin.volar(100)
mi_animal.hablar()

class Padre:
    def hablar(self):
        print("Papa dijo hola")

class Madre:
    def nocheDeChicas(self):
        print("Hoy es noche de chicas!!!")

    def reir(self):
        print("jajajaja")

    def hablar(self):
        print("Mama dijo hola")        

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
print(Nieto.__mro__)

mi_nieto.nocheDeChicas()
mi_nieto.hablar()
