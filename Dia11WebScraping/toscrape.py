##########explorar diferentes paginas de sitio web
import bs4
import requests

urlBase = 'https://books.toscrape.com/catalogue/page-{}.html'

# for n in range(1,11):
#     print(urlBase.format(n))
##########################################################################################################
resultado =  requests.get(urlBase.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# print(sopa.select('.product_pod'))
libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)
# A Light in the Attic