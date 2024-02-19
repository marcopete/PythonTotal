import os
from pathlib import Path, PurePath, PureWindowsPath
from os import system
# import shutil

# def welcome():
#     print("¡Bienvenido al gestor de recetas!")
#     print("Ruta del directorio de recetas:", os.path.abspath("Recetas"))
#     print("Número total de recetas:", count_recipes())

# def count_recipes():
#     total_recipes = 0
#     for category in os.listdir("Recetas"):
#         category_path = os.path.join("Recetas", category)
#         if os.path.isdir(category_path):
#             total_recipes += len(os.listdir(category_path))
#     return total_recipes

# def show_recipe(category, recipe_name):
#     file_path = os.path.join("Recetas", category, recipe_name)
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print("\nContenido de la receta '{}':\n".format(recipe_name))
#         print(content)

# def create_recipe(category, recipe_name, recipe_content):
#     file_path = os.path.join("Recetas", category, recipe_name)
#     with open(file_path, 'w') as file:
#         file.write(recipe_content)
#         print("\nReceta '{}' creada con éxito.".format(recipe_name))

# def create_category(category_name):
#     category_path = os.path.join("Recetas", category_name)
#     os.makedirs(category_path)
#     print("\nCategoría '{}' creada con éxito.".format(category_name))

# def delete_recipe(category, recipe_name):
#     file_path = os.path.join("Recetas", category, recipe_name)
#     os.remove(file_path)
#     print("\nReceta '{}' eliminada con éxito.".format(recipe_name))

# def delete_category(category_name):
#     category_path = os.path.join("Recetas", category_name)
#     shutil.rmtree(category_path)
#     print("\nCategoría '{}' eliminada con éxito.".format(category_name))

# def main():
#     while True:
#         os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla

#         welcome()

#         print("\nOpciones:")
#         print("1. Leer una receta")
#         print("2. Crear una nueva receta")
#         print("3. Crear una nueva categoría")
#         print("4. Eliminar una receta")
#         print("5. Eliminar una categoría")
#         print("6. Salir")

#         choice = input("\nSeleccione una opción (1-6): ")

#         if choice == '1':
#             category = input("Ingrese la categoría de la receta: ")
#             recipe_name = input("Ingrese el nombre de la receta: ")
#             show_recipe(category, recipe_name)

#         elif choice == '2':
#             category = input("Ingrese la categoría de la nueva receta: ")
#             recipe_name = input("Ingrese el nombre de la nueva receta: ")
#             recipe_content = input("Ingrese el contenido de la nueva receta: ")
#             create_recipe(category, recipe_name, recipe_content)

#         elif choice == '3':
#             category_name = input("Ingrese el nombre de la nueva categoría: ")
#             create_category(category_name)

#         elif choice == '4':
#             category = input("Ingrese la categoría de la receta a eliminar: ")
#             recipe_name = input("Ingrese el nombre de la receta a eliminar: ")
#             delete_recipe(category, recipe_name)

#         elif choice == '5':
#             category_name = input("Ingrese el nombre de la categoría a eliminar: ")
#             delete_category(category_name)

#         elif choice == '6':
#             print("¡Hasta luego!")
#             break

#         input("\nPresione Enter para volver al menú principal.")

# if __name__ == "__main__":
#     main()

#############################################################

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

def inicio():
    system('clear')
    print('*' * 50)
    print('*' * 5 +"Bienvenido al recetario magistral"+ '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas estan en {mi_ruta}")
    print(f"Las recetas son {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'

    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range (1,7):
        print("Elige una opcion:")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir''')
        eleccion_menu = input()

    return eleccion_menu

def mostrar_categorias(ruta):
    print("Categrorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")

    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador +=1

    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")

    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta)) 

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe el contenido de tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input() + '.txt'
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta} fue eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} fue eliminada")

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V y Enter para volver al menu:")        


# Menu inicial
finalizar_programa = False

while not finalizar_programa:
    menu = int(inicio())

    if int(menu) == 1:
        #Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        #elegir recetas
        if len(mis_recetas) < 1:
            print("No hay recetas en esa categoria")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            #leer receta
            leer_receta(mi_receta)
        #volver inicio
        volver_inicio()
    elif menu == 2:
        #Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #crear receta nueva
        crear_receta(mi_categoria)
        #volver inicio
    elif menu == 3:
        #crear categorias
        crear_categoria(mi_ruta)
        #volver inicio
        volver_inicio()
    elif menu == 4:
        #Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esa categoria")
        else:        
        #elegir recetas
            mi_receta = elegir_recetas(mis_recetas)
            #eliminar receta
            eliminar_receta(mi_receta)
        #volver inicio
        volver_inicio()
    elif menu == 5:
        #Mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        #elegir categoria
        mi_categoria = elegir_categoria(mis_categorias)
        #eliminar categori
        eliminar_categoria(mi_categoria)
        #volver inicio
        volver_inicio()    
    elif menu ==6:
        finalizar_programa = True
        #Finalizar programa        