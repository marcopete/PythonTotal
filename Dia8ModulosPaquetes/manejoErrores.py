def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1+n2)
    print("suma realizada")

# suma()

try:
    # Prueba
    suma()
except TypeError:
    # A ejecutar si hay error
    print("Estas intentando concatendar tipos disotntos")
except ValueError:
    # A ejecutar si hay error
    print("Ingresa un numoer")
else:
    # A ejecutar si no hay error
    print("Perfect")
finally:
    # A ejecutar
    print("Ha saido todo")

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame in numero: "))    
        except:
            print("Eso no es un numero")
        else:
            print(f"Ingresaste el numer {numero}")
            break

print("Numero pedido terminado")

pedir_numero()