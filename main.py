import os
import msvcrt
from ListaLigada import ListaLigada
from ListaDos import ListaLigadaDoble
from ListaTres import ListaCircular


def limpiar():
    os.system('cls')

def menuPrincipal():
    print("     BIENVENIDO\n"
          "¿QUÉ DESEA REALIZAR?")
    opcion = 0
    while True:
        print("""
        1) Lista ligada simples
        2) Lista ligada dobles
        3) Lista ligada circulares
        4) Salir""")
        opcion = int(input("¿Que opción eliges?: "))
        limpiar()
        if opcion == 1:
            menuLigada()
        elif opcion == 2:
            menuDobles()
        elif opcion == 3:
            menuCircular()
        elif opcion == 4:
            limpiar()
            print("¡Vuelve pronto!")
            break
        else:
            limpiar()
            print("Intenta con otra opción: ")

def menuLigada():
    lista = ListaLigada()
    print('"LISTA LIGADA SIMPLE"')
    opcion = 0
    while True:
        print("""
        1) Lista de acceso
        2) Buscar en la lista
        3) Insertar en la lista
        4) Eliminar algún valor de la lista
        5) Regresar al menú principal""")
        opcion = int(input("Introduce una opción: "))
        limpiar()
        if opcion == 1:
            lista.acceso()
        elif opcion == 2:
            valor = int(input("Introduzca el valor a buscar en la lista: "))
            nodo = lista.busqueda(valor)
            print(nodo)
        elif opcion == 3:
            valor = int(input("Introduce un valor para insertar: "))
            lista.insercion(valor)
            print(f"El valor {valor} se ha insertado en la lista.")
        elif opcion == 4:
            valor = int(input("Introduce el valor que deseas eliminar: "))
            lista.eliminar(valor)
            print(f"El valor {valor} se ha eliminado de la lista.")
        elif opcion == 5:
            limpiar()
            menuPrincipal()
        else:
            print("Intenta escogiendo otra opción")


def menuDobles():
    lista = ListaLigadaDoble()
    print('"LISTA LIGADA DOBLE"')
    opcion = 0
    while True:
        print("""
            1) Lista de acceso
            2) Buscar en la lista
            3) Insertar al principio
            4) Insertar al final
            5) Eliminar
            6) Invertir
            7) Regresar al menú principal""")
        opcion = int(input("Introduce una opción: "))
        limpiar()
        if opcion == 1:
            lista.acceso()
        elif opcion == 2:
            valor = int(input("Introduzca el valor a buscar en la lista: "))
            nodo = lista.buscar(valor)
            if nodo is not None:
                print(nodo)
            else:
                print("Intente con otro numero")
        elif opcion == 3:
            valor = int(input("Introduzca el valor del nuevo nodo al inicio: "))
            lista.primeraInsercion(valor)
            print(f"El valor {valor} se ha insertado al principio de la lista.")
        elif opcion == 4:
            valor = int(input("Introduzca el valor del nuevo nodo al final: "))
            lista.ultimaInsercion(valor)
            print(f"El valor {valor} se ha insertado al final de la lista.")
        elif opcion == 5:
            valor = int(input("Introduzca el valor del nodo a eliminar: "))
            lista.eliminar(valor)
            print(f"El valor {valor} se ha eliminado de la lista.")
        elif opcion == 6:
            lista.invertir()
            lista.acceso()
            print("Se han invertido :0 ")
        elif opcion == 7:
            limpiar()
            menuPrincipal()
        else:
            print("Intenta escogiendo otra opción")

def menuCircular():
    lista = ListaCircular()
    print('"LISTA CIRCULAR"')
    opcion = 0
    while True:
        print("""
        1) Lista de acceso
        2) Buscar en la lista
        3) Insertar en la lista
        4) Eliminar algún valor de la lista
        5) Regresar al menú principal""")
        opcion = int(input("Introduce una opción: "))
        limpiar()
        if opcion == 1:
            lista.acceso()
        elif opcion == 2:
            valor = int(input("Introduzca el valor a buscar en la lista: "))
            nodo = lista.buscar(valor)
            if nodo is not None:
                print(nodo)
            else:
                print("Intente con otro numero")
        elif opcion == 3:
            valor = int(input("Introduce un valor para insertar: "))
            lista.insercion(valor)
            print(f"El valor {valor} se ha insertado en la lista.")
        elif opcion == 4:
            valor = int(input("Introduce el valor que deseas eliminar: "))
            lista.eliminar(valor)
            print(f"El valor {valor} se ha eliminado de la lista.")
        elif opcion == 5:
            limpiar()
            menuPrincipal()
        else:
            print("Intenta escogiendo otra opcion")


menuPrincipal()
limpiar()
msvcrt.getch()
