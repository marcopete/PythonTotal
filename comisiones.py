pctcomision = 0.13 # 13%
nombre = input("Dime tu nombre: ")
ventas = input("Cuanto vendiste: ")
comision = round(pctcomision * float(ventas),2)
# print('Ok ' + nombre + ' este mes ganaste ' + str(comision))
print(f"Ok {nombre} este mes gamaste {str(comision)}")