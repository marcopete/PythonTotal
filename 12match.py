serie = 'N-02'
match serie:
    case 'N-01':
        print('samsung')
    case 'N-02':
        print('nokia')
    case 'N-03':
        print('motorola')
    case _:
        print('El producto no existe') 

cliente = {'nombre': 'Federico',
           'edad': 45,
           'ocupacion': 'instructor'}
 
pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'Keanu Reeves',
                              'director': 'Lana y Lilly Wachowski'}}
 
elementos = [cliente, pelicula, 'libro']
 
for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                              'director': director}}:
            print("Es una película")
            print(titulo, protagonista, director)
        case _:
            print('No sé qué es esto')        