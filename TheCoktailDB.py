import requests
import sqlite3
import APISERVICE
import APICLASS

def buscar(apiclas):
    n = input("Nombre de la Bebida: ")
    buscar = apiclas.buscarNombre(n)
    print("Bebidas encontradas: ")
    print(buscar)
    be = int(input("Elige una Bebida por su numero: "))
    mostrr = apiclas.getBebida(be, n)
    print(mostrr)
    return mostrr

def guardar(apiclas2, bebida):
    print(apiclas2.guardarBebida(bebida))

def mostrar(apiclas2):
    pass

def main():
    apiclas = APICLASS.buscarNombre()
    apiclas2 = APICLASS.guardarBebida()
    print("Bienvenido al Sabor, Elige una opcion: ")
    opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida "+"\n"+"2 -> Mostrar Bebidas Guardadas "+"\n"+"3 -> Salir "))
    cont = 0
    while cont == 0:
        if opcion == 1:
            bde = buscar(apiclas)
            print("Guardar Bebida ?")
            gb = int(input("0 -> Si "+"\n"+"1 -> No "))
            if gb == 0:
                guardar(apiclas2, bde)
                #print("Bebida guardada con exito !!!")# guardar la bebida esta en duda si se queda
                opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida " + "\n" + "2 -> Mostrar Bebidas Guardadas " + "\n" + "3 -> Salir "))
            elif gb == 1:
                opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida " + "\n" + "2 -> Mostrar Bebidas Guardadas " + "\n" + "3 -> Salir "))
            else:
                print("Introdusca una opcion valida")
                gb = int(input("0 -> Si " + "\n" + "1 -> No"))
        elif opcion == 2:
            print("Aqui tu lista de Favoritos :D !!!")

            opcion = int(input("MENU" + "\n" + "1 -> Buscar Bebida " + "\n" + "2 -> Mostrar Bebidas Guardadas " + "\n" + "3 -> Salir "))
        elif opcion == 3:

           exit()
        else:
            print("Introdusca una opcion valida")
            opcion = int(input("MENU"+"\n"+"1 -> Buscar Bebida " + "\n" + "2 -> Mostrar Bebidas Guardadas "+"\n"+"3 -> Salir "))

if __name__ == '__main__':
    main();