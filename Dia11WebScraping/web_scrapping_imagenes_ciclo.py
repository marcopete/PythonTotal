
import bs4
import requests
from datetime import datetime
 
resultado = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')
list_imgs = sopa.select('.course-box-image')
 
for img in list_imgs:
    now = datetime.now()
    name = 'img_' + str(now).replace(":","").replace(".","") + '.jpg'
    binary_img = requests.get(img['src'])
    binary_content = binary_img.content
 
    img_file = open(name, 'wb')
    img_file.write(binary_content)
    img_file.close()