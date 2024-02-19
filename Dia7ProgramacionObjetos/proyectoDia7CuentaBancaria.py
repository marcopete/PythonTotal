import os
# from pathlib import Path, PurePath, PureWindowsPath
from os import system

class Persona:
    def __init__(self, nombre, apellido, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut

class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, numeroCuenta, balance = 0):
        super().__init__(nombre, apellido, rut)
        self.numeroCuenta = numeroCuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numeroCuenta}: ${self.balance}"
    
    def depositar(self, monto_deposito):
        balance_actual = self.balance
        self.balance += monto_deposito
        print(f"El balance de ${balance_actual} con el nuevo deposito de ${monto_deposito} el nuevo balance es de {self.balance}")


    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            balance_actual = self.balance
            self.balance -= monto_retiro
            print(f"El balance de ${balance_actual} con el nuevo retiro de ${monto_retiro} el nuevo balance es de {self.balance}")
        else:
            print("No seas barza estas sacando mas de lo que tienes")

def crear_cliente():
    nombre_cliente = input("Ingresa nombre: ")            
    apellido_cliente = input("Ingresa apellido: ")
    rut_cliente = input("Ingresa rut: ")            
    numero_cuenta = input("Ingresa numero de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, rut_cliente, numero_cuenta)            
    return cliente
        

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)

    eleccion_menu = 'x'

    while  eleccion_menu != 'S':
        print("Elige una opcion:")
        print('''
        [I] - Imprimir cliente
        [D] - Depositar
        [R] - Retirar
        [S] - Salir''')
        eleccion_menu = input()

        if eleccion_menu == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif eleccion_menu == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Chao gracias")
    

inicio()