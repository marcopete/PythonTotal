from collections import Counter, defaultdict, namedtuple, deque

numeros = [6,4,8,3,5,9,0,1,4,2,7,8,9,5,1,0,6,2,9,4,1,8,9]
print('*****')
# cantidad de veces que el numero esta en lista
print(Counter(numeros))
print('*****')
frase = 'al pan vino'
# cantidad de veces que la letra esta en lista
print(Counter('misssissisissisisisisispi'))
print('*****')
# cantidad de veces que la letra esta en lista
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3])
print(serie.most_common())
print()

##########################################################################
mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
print(mi_dic['dos'])

mi_dic = defaultdict(lambda:'nada')
# Esto dira "nada"
print(mi_dic['jfkhgdfkjhgkdjfhg'])
# Esto dira el valor jfkhgdfkjhgkdjfhg y "nada"
print(mi_dic)

############################
mi_tupla = (500,18,65)
print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.altura)
print(ariel[2])
print(ariel[0])
####################################
ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(ciudades)
print(lista_ciudades)

ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(ciudades)
listaCasteadaCiudades = list(lista_ciudades)
print(listaCasteadaCiudades)

# insertar por la derecha
lista_ciudades.append("Bogota")
dequeCasteadoDerecha = list(lista_ciudades)
print(dequeCasteadoDerecha)
 
# insertar por la izquierda
lista_ciudades.appendleft("Tokyo")
dequeCasteadoIzquierda = list(lista_ciudades)
print(dequeCasteadoIzquierda)