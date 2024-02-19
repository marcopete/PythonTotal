class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"Volo {metros} metros de distancia")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"El pajaro se ha pintado de color {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad_huevos):
        print(f"Puso {cantidad_huevos} huevos")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

piolin = Pajaro('amarillo', 'canario')
pajaro_loco = Pajaro('rojo', 'carpintero')
Pajaro.poner_huevos(4)
Pajaro.mirar()
print(f"El pajaro loco es un {pajaro_loco.especie} de color {pajaro_loco.color}")


class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

# Llamar al método estático respirar sin crear una instancia de Mascota
Mascota.respirar()

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print("¡Flecha lanzada! Flechas restantes:", self.cantidad_flechas)
        else:
            print("¡No quedan flechas!")

# Crear una instancia de la clase Personaje con 5 flechas iniciales
arquero = Personaje(cantidad_flechas=5)

# Llamar al método lanzar_flecha para reducir la cantidad de flechas
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
