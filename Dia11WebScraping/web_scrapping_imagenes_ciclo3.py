from bs4 import BeautifulSoup
import requests
import re
 
url= "https://www.escueladirecta.com/courses"
result=requests.get(url)
soup = BeautifulSoup(result.text,'html.parser')
 
image=soup.select('.course-box-image')
title=soup.select('.course-listing-title')
 
def clean_title(n_title):
    c_title =re.sub(r'[^a-zA-Z0-9-ÑñÁáÉéÍíÓóÚú]',' ',n_title)
    return c_title
 
 
def download_images(image,title):
    for i, image in enumerate(image):
        n_title = clean_title(title[i]['title'])
        image_url=image['src']
        try:
            response=requests.get(image_url)
            response.raise_for_status()
 
            with open(f'{i+1}'+'_'+n_title+'.jpg','wb') as file:
                file.write(response.content)
            print(f'Imagen {i+1, n_title} descargada correctamente')
        except requests.exceptions.RequestException as e:
            print(f'Error al descargar imagen {i}: {str(e)}')
 
download_images(image, title) 