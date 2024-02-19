import requests
import bs4
 
resultado = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
imagenes = sopa.select('.course-box-image')
 
def descargar_imagenes(imagenes):
    for i, imagen in enumerate(imagenes):
        imagen_url = imagen['src']
        try:
            respuesta = requests.get(imagen_url)
            respuesta.raise_for_status()  # Verificar si hay errores en la respuesta HTTP
            with open(f'{i+1}_mi_imagen.jpg', 'wb') as archivo:
                archivo.write(respuesta.content)
            print(f'Imagen {i+1} descargada correctamente.')
        except requests.exceptions.RequestException as e:
            print(f'Error al descargar imagen {i}: {str(e)}')
 
descargar_imagenes(imagenes)