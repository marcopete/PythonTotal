class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

print (Pajaro.__bases__)
print (Animal.__subclasses__())

piolin = Pajaro(2, 'amarillo')

piolin.nacer()
print(piolin.color)

class Persona:

    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre 

class Alumno(Persona):
    pass

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas, raza):
        # Llamamos al constructor de la clase base Mascota
        super().__init__(edad, nombre, cantidad_patas)
        # Atributo específico de la clase Perro
        self.raza = raza

# Crear una instancia de la clase Perro
mi_perro = Perro(edad=3, nombre="Max", cantidad_patas=4, raza="Labrador")

# Acceder a los atributos de la clase base Mascota
print(f"Nombre: {mi_perro.nombre}")
print(f"Edad: {mi_perro.edad}")
print(f"Cantidad de patas: {mi_perro.cantidad_patas}")

# Atributo específico de la clase Perro
print(f"Raza: {mi_perro.raza}")
