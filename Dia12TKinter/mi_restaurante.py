from tkinter import *

# Operador -> almacenala cant. de nº que se presionan, construyendo un string
operador = ''
 
# fc que se llama c/vez que se oprime un botón
def click_boton(numero):
    global operador
    operador = operador + numero
    # Para eliminar lo que había antes. Sino, ej. apretar el 1 2 3 rdo: 1 12 123
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)
 
# fc borrar cuando de oprime B
def borrar():
    global operador
    operador = ''  # resetear operador para que no vuelva aparecer lo que había luego de apretar B
    visor_calculadora.delete(0, END)
 
def obtener_resultado():
    global operador
    resultado = str(eval(operador))  # fc evaluar que devuelve integer, luego lo casteamos a string. La fc realiza la op.
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


# iniciar tkinter

aplicacion = Tk()

#tamaño ventana y ubicacion superior izquierdo (0+0)
aplicacion.geometry('1300x850+0+0')  #1020x630+0+0'

# evitar maixmizar ejes x y
aplicacion.resizable(0,0)

# titulo
aplicacion.title ("Mi sistema de facturacion!!!!")

# color de fondo
# aplicacion.config(bg='burlywood')
aplicacion.config(bg='DeepSkyBlue')

##################################Parte 2

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#ETIQUETA TITULO
# etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacionb', fg='azure4', font=('Dosis', 58), bg = 'burlywood', width=27)
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacionb', fg='azure4', font=('Dosis', 58), bg = 'burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#PANEL_COSTOS
# panel_costos =  Frame(aplicacion, bd=1, relief=FLAT)
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='DodgerBlue', padx=30)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

#panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

#panel CALCULADORA
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

#lista de productos
lista_comidas = ['pollo','cordero','salmon','machas','pizza','superpiiza', 'kebab', 'cazuela']
lista_bebidas = ['agua','coca','fanta','cunsman','blu leibol','orange leibol', 'jugo', 'champaña']
lista_postres = ['suspiro','helado','torta','pastel','cujen','cafelado', 'flan', 'mousse']

# lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
# lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza', 'cerveza2']
# lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

#generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:

    #crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable =variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for bebida in lista_bebidas:

    #crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable =variables_comida[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')    
    cuadros_comida[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1  

variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for postre in lista_postres:

    #crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable =variables_comida[contador])
    postre.grid(row=contador, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')    
    cuadros_comida[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

#################################
# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()
 
# Etiquetas de Costo y Campos de Entrada
etiqueta_costo_comida = Label(panel_costos, text='Costo Comida', font=('Dosis', 12, 'bold'), bg='DodgerBlue', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
 
texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=25)
 
etiqueta_costo_bebida = Label(panel_costos, text='Costo Bebida', font=('Dosis', 12, 'bold'), bg='DodgerBlue', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
 
texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=25)
 
etiqueta_costo_postres = Label(panel_costos, text='Costo Postres', font=('Dosis', 12, 'bold'), bg='DodgerBlue',              fg='white')
etiqueta_costo_postres.grid(row=2, column=0)
 
texto_costo_postres = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=25)
 
etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'), bg='DodgerBlue', fg='white')
etiqueta_subtotal.grid(row=0, column=2)
 
texto_subtotal = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=25)
 
etiqueta_impuestos = Label(panel_costos, text='Impuestos', font=('Dosis', 12, 'bold'), bg='DodgerBlue', fg='white')
etiqueta_impuestos.grid(row=1, column=2)
 
texto_impuestos = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=25)
 
etiqueta_total = Label(panel_costos, text='Total', font=('Dosis', 12, 'bold'), bg='DodgerBlue', fg='white')
etiqueta_total.grid(row=2, column=2)
 
texto_total = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3, padx=25) 

#############################################################################################
# Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis', 14, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    boton.grid(row=0, column=columnas)
    columnas += 1
 
# Area de recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), bd=1,  width=42, height=10)
texto_recibo.grid(row=0, column=0)
 
# Calculadora
visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), width=32, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)
 
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'C', '0', '/']
 
# Vamos a guardar estos botones cuando se crean dentro de unas vars p/asignarlas a la fc click boton
botones_guardados = []
 
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,  text=boton.title(),  font=('Dosis', 16, 'bold'),  fg= 'white', bg='azure4', bd=1, width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)
 
    if columna == 3:
        fila += 1
 
    columna += 1
 
    if columna == 4:
        columna = 0
 
# Asignar a c/boton de esa lista una llamada a la fc click. Command -> llamado a un comando y lambda para incorporar el argumento que va a necesitar la fc
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

# evitar que la pantalla se cierre
aplicacion.mainloop()