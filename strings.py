texto = 'Este es el texto!!'
texto2 = 'Este; es; el; texto!!'
resultado = texto.upper()
resultado = texto[2].upper()
resultado = texto.lower()
resultado = texto.split()  # retorna ['Este', 'es', 'el', 'texto!!']
resultado = texto2.split(";")
resultado = texto.find('s') #1
resultado = texto.replace('x','todos') #retorna Este es el tetodosto!!

print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

n1 = 'Mark'
n2 = 'o'
print(n1 + n2)
print(n1 * 10)

poema = """mIL PEQUEÑOS PECES BLANCOS
COMO SI HIRVIERA
EL COLOR DEL AGUA"""
print(poema)
print("AGUA" in poema)
print("SOL" not in poema)
print(len(e))

mi_lista = ['a','b','c']
mi_lista_2 = ['d','e','f']
mi_lista_3 = mi_lista+mi_lista_2
resultado = len(mi_lista)
# resultado = mi_lista[0:2] # listas no incluyen el 2, toma 0 y 1
print(resultado)
print(mi_lista_3)
# otra_lista = ['hola',55,6.1]
# mi_lista_3[0] = 'alfa'
# mi_lista_3.append('g')
eliminado = mi_lista_3.pop(0)
print(mi_lista_3)
print(eliminado)

mi_lista = ['x','f','y','o','m','a']
mi_lista.sort()
mi_lista.reverse()
print(mi_lista)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c1']+dic['c2'])
print(dic['c2'][1].upper())

dic = {'c1':'a','c2':'b'}
print(dic)
dic['c3'] = 'c'
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

mi_tuple = (1,2,3,4,(10,20))
print(mi_tuple)
print(mi_tuple[0])
print(mi_tuple[-2])
print(mi_tuple[4][0])

t = (1,2,3)
x,y,z = t
print(x,y,z)

t = (1,2,3,1)
print(len(t))
print(t.count(1)) #1 ESTA 2 VECES
print(t.index(2))

mi_set = set([1,2,3,4,5,(1,2,3)]) #los set no repitem, si tiene repetidos los saca. set([1,2,3,4,5,1,1,1])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

print(mi_set)
print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = {6,7,8}
s4 = s1.union(s2.union(s3))
print(s4)
s1.add(15)
print(s1)
# s1.remove(15) #si valor 15 no existe arroja error, con discard no pasa esto
s1.discard(15)
print(s1)
sorteo = s1.pop()
s1.clear()
print(s1)

bool1 = True
bool2 = False
numero = 5 == 2+3
print(numero)
lista = [1,2,3,4]
control = 5 in lista
print(control)
