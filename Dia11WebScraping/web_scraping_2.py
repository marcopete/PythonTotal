import bs4
import requests
 
resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')
 
# print(type(resultado))
# print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# print(sopa)
# print(sopa.select('title'))
# print(sopa.select('p'))
# print(len(sopa.select('p')))
# print(sopa.select('h1'))
# print(sopa.select('title')[0])
# print(sopa.select('title')[0].getText())

# parrafo_especial = sopa.select('p')
# print(parrafo_especial)

# parrafo_especial = sopa.select('p')[3]
# print(parrafo_especial)

# parrafo_especial = sopa.select('p')[3].getText()
# columna_lateral = sopa.select('.PopularPosts')
# print(columna_lateral)

# columna_lateral = sopa.select('.content')
# print(columna_lateral)

# columna_lateral = sopa.select('.PopularPosts')
# print(columna_lateral)

# columna_lateral = sopa.select('.PopularPosts h3')[0]
# print(columna_lateral)

columna_lateral = sopa.select('.PopularPosts h3')

for p in columna_lateral:
    print(p.getText())