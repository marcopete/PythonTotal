num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

suma = num1 + num2
print(f"La suma de {num1} y {num2} es {suma}")
 
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")