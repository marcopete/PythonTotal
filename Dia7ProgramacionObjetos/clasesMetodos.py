class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"Volo {metros} metros de distancia")

piolin = Pajaro('amarillo', 'canario')

piolin.piar()
piolin.volar(26)

class Mago:
    def __init__(self):
        pass
    
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
        
merlin = Mago()

merlin.lanzar_hechizo()

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

# Crear una instancia de la clase Alarma
mi_alarma = Alarma()

# Llamar al método postergar con una cantidad de minutos específica
mi_alarma.postergar(10)