def multiplicar(numero1,numero2):
    total = numero1*numero2
    # print(total)
    return total

# resultado = multiplicar(8,10)
# print(resultado)

def potencia(base, exponente):
    resultado = base ** exponente
    return resultado

def usd_a_clp(monto_usd):
    tasa_de_cambio = 907.55
    monto_eur = monto_usd * tasa_de_cambio
    return monto_eur

# Ahora, creemos una variable llamada 'dolares' con un monto en dólares y usemos la función 'usd_a_eur' para convertirlo a euros.
dolares = 50000  # Puedes cambiar este valor a la cantidad que desees convertir
clp = usd_a_clp(dolares)

print(f"{dolares} dolar(es) equivalen a {clp} CLP")