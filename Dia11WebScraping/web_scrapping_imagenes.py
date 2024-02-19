import bs4
import requests
import lxml
 
resultado = requests.get("https://www.escueladirecta.com/courses/")
 
 
sopa = bs4.BeautifulSoup(resultado.text, "lxml")
 
# imagenes = sopa.select("img")
imagenes = sopa.select(".course-box-image")[0]
imagenes = sopa.select(".course-box-image")[0]['src']
 
for img in imagenes:
    print(img)

print(imagenes)

imagen_curso_1 = requests.get(imagenes)
# print(imagen_curso_1)
# print(imagen_curso_1.content)

f = open('mi_imagen.png', 'wb')
f.write(imagen_curso_1.content)
f.close()