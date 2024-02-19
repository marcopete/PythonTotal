import re

texto = 'Si necesitas ayuda, llama al (658)-598-9977 las 24 horas al servivio de ayuda onlone'
palabra = 'ayuda' in texto
# true
print(palabra)

patron  = 'nada'
busqueda = re.search(patron, texto)
# none (no hay objeto)
print(busqueda)

patron  = 'ayuda'
busqueda = re.search(patron, texto)
# encontro, desde el 13 al 18
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

busqueda = re.findall(patron, texto)
print(busqueda)

for hallazgo in re.finditer(patron, texto):
    print(f"el for pillo {hallazgo.span()}")

texto = "llama al 123-456-9977 ya mismo"
# estos 2 patron hacen lo mismo
patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)
print(resultado.group(1))
print(resultado.group(2))
print(resultado.group(3))

# clave = input("Clave: ")
clave = 'etyuiop5'
patron = r'\D{1}\w{7}' 
chequear = re.search(patron, clave)
# elemplo de chequear valido para una letra obligatoria seguido de 7 caracteres: etyuiop5
print(chequear)

texto = "No atendemos los lunes en la tarde"
# lunes o martes
buscar = re.search(r'lunes|martes', texto)
print(buscar)

texto = "No atendemos los jueves en la tarde"
buscar = re.search(r'lunes|martes', texto)
print(buscar)

buscar = re.search(r'.demos', texto)
print(buscar)

buscar = re.search(r'....demos....', texto)
print(buscar)

buscar = re.search(r'....demos....', texto)
print(buscar)

buscar = re.search(r'^\D', texto)
print(buscar)

buscar = re.search(r'\D$', texto)
print(buscar)

buscar = re.findall(r'[^\s]', texto)
print(buscar)

buscar = re.findall(r'[^\s]+', texto)
print(buscar)

buscar = re.findall(r'[^\s]+', texto)
print(''.join(buscar))

def verificar_email(email):
    # Verifica la presencia de "@" y ".com" o ".com.br"
    if "@" in email and (email.endswith(".com") or email.endswith(".com.br")):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

# direccion_email = input("Ingrese la dirección de email: ")
direccion_email = 'yo@yo.com'        
verificar_email(direccion_email)

def verificar_saludo(frase):
    # Verifica si la frase inicia con "Hola"
    if frase.startswith("Hola"):
        print("Ok")
    else:
        print("No has saludado")

# Ejemplo de uso:
# saludo_usuario = input("Ingresa tu saludo: ")
saludo_usuario = "Hola"
verificar_saludo(saludo_usuario)

def verificar_cp(codigo_postal):
    # Verifica si el código postal sigue el patrón XX1234
    if len(codigo_postal) == 6 and codigo_postal[:2].isalpha() and codigo_postal[2:].isdigit():
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

# Ejemplo de uso:
codigo_ingresado = input("Ingrese el código postal: ")
verificar_cp(codigo_ingresado)
