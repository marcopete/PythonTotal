# = ==
mi_variable = 'Hola Mundo'
mi_bool = 10 == 25 # False
mi_bool_menor = 10 < 25 # True
mi_variable_string = 'blanco'=='Blanco'.lower()
print(mi_bool)
print(mi_variable_string)
print(mi_bool_menor)

mi_bool = 4 < 5 < 6
print(mi_bool) # TRUE
mi_bool = (4 < 5) and (5 == 2+3)
print(mi_bool) # TRUE
mi_bool = (10 == 1) or (5 == 2+3)
print(mi_bool) # TRUE

texto = "Esta frase es breve"
mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool) # TRUE

mi_bool = 'a' == 'a'
mi_bool = not ('a' != 'a')
print(mi_bool) # not ('a' != 'a') true