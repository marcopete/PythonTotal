lista = ['a','b','c','d','e','f']
indice = 0
for item in enumerate(lista):
    print(item)

for indice,item in enumerate(range(50,60)):
    print(indice,item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1][1])