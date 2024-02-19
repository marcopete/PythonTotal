import bs4
import requests
 
#url sin numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'
 
#lista de titulos con 4 - 5 estrellas
titles_5_stars = []
titles_4_stars = []
titles_3_stars = []
titles_2_stars = []
titles_1_stars = []
 
#iterar paginas 
for i in range(1,51):
    #crear sopa por pagina
    url_page = url_base.format(i)
    result =  requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    
    #seleccion datos de libro
    books = soup.select('.product_pod')
    for book in books:
        #validar estrellas 
        if len(book.select('.star-rating.Five')) != 0: 
            title = book.select('a')[1]['title']
            titles_5_stars.append(title)         
        elif len(book.select('.star-rating.Four')) != 0:
            title = book.select('a')[1]['title']
            titles_4_stars.append(title)
        elif len(book.select('.star-rating.Three')) != 0:
            title = book.select('a')[1]['title']
            titles_3_stars.append(title)
        elif len(book.select('.star-rating.Two')) != 0:
            title = book.select('a')[1]['title']
            titles_2_stars.append(title)
        elif len(book.select('.star-rating.One')) != 0:
            title = book.select('a')[1]['title']
            titles_1_stars.append(title)
            
            
count_5 = 0
for t in titles_5_stars:
    count_5 += 1
    print(f'⭐  ⭐  ⭐  ⭐  ⭐ {count_5}.- {t}')
    
count_4 = 0        
for t in titles_4_stars:
    count_4 += 1
    print(f'⭐  ⭐  ⭐  ⭐  ⚫ {count_4}.- {t}')
 
count_3 = 0
for t in titles_3_stars:
    count_3 += 1
    print(f'⭐  ⭐  ⭐  ⚫  ⚫ {count_3}.- {t}')
 
count_2 = 0     
for t in titles_2_stars:
    count_2 += 1
    print(f'⭐  ⭐  ⚫  ⚫  ⚫ {count_2}.- {t}')
 
count_1 = 0
for t in titles_1_stars:
    count_1 += 1 
    print(f'⭐  ⚫  ⚫  ⚫  ⚫ {count_1}.- {t}')