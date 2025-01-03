precios_cafe =[('Capuchino',2.5),('Expreso',1.2),('Moka',1.9)]

def precio_mayor(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''
 
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)
 
cafe_mas_caro, precio_mas_alto = precio_mayor(precios_cafe)
print(f'El cafe mas caro es {cafe_mas_caro} valiendo {precio_mas_alto}')