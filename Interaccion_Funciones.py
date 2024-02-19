from random import shuffle

palitos = ['-','--','---','----']

def mezclar (lista):    
    shuffle (lista)    
    return (lista)

def probar_suerte ():
  intento= " "
  x = 0
  while intento not in ["1","2","3","4"]:
    intento = input("Elige un número del 1 al 4: ")
    # x += 1
    # if x == 3:
    #   print("¡Ya no puedes seguir jugando!")
    #   break
  return int(intento)

def chequear_intento(lista,intento):
   if lista[intento -1] == '-':
      print('A lavar los platos!!!')
   else:
      print('La hiciste, no lavas los platos')

   print(f"Te ha tocado {lista[intento-1]}")

palitos_mazclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mazclados,seleccion)

