lista = ['a','b','c','d']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print("Letra: " + letra)
    print(f"Letra {numero_letra}: {letra}")

lista = ['mon','elo','chi','yo'] 

for nombre in lista:
    if nombre.startswith('e'):
        print(nombre)
    else:
        print(f"Los nombres sin e {nombre}")        

numeros = [1,2,3,4,5]
mivalor = 0

for numero in numeros:
    mivalor = mivalor + numero
    print(mivalor)
print(mivalor)    

palabra = 'python'

for letra in palabra:
    print(letra)

for letra in [[1,2],[3,4],[5,6]]:
    print(letra) 

for a,b in [[1,2],[3,4],[5,6]]:
    print("a:")
    print(a)
    print("b:")        
    print(b)        

dic = {'clave1':'a','clave2':'b','clave3':'c'}    

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)    

for a,b in dic.items():
    print(a,b)    