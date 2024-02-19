import unittest
import clase114_cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    # fa funcion debe iniciar con test_ para realizar la prueba, en este caso test_mayusculas
    def test_mayusculas(self):
        palabra = 'sldkfjlsdkfhjlksdhfkwjehrkwjherrwekjhekwjhrwejkh'
        resultado = clase114_cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'Sldkfjlsdkfhjlksdhfkwjehrkwjherrwekjhekwjhrwejkh')

if __name__ == '__main__':
    unittest.main()

# var = input("kjsfhdgfkjhsdfkjhsdfkjhdfkjhsdkfjh")

