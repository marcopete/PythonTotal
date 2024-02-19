monedas  = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas -1
else:
    print("N me qieda plata")    

resp = 's'

while resp == 's':
    resp = input("sigues? s/n")
else:
    print("ok")    

nombre = input("Tu nombre?")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)    