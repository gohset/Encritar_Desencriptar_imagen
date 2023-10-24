#!/usr/bin/python
#-*- coding: latin-1 -*-

import os
import pathlib
from time import sleep
import time

os.system("cls")
print("###########################################################")
print("######### ENCRIPTACION Y DESENCRIPTACION DE IMAGEN ########")
print("###########################################################")



################################################################
################################################################

#directorio_prueba = "C:/Users/admin/PycharmProjects/prueba1/Documentos/apps-html5.pdf"
directorio_actual = os.getcwd()
directorio_raiz =  os.path.join(os.getcwd(), "/")
##################################################################

opcion = 0
lista = ()
total = {}
cont = {}
j = {}
ingresar_clave = 0

def info():
    time.sleep(5)
    # os.system("cls")
    print("[!] Esta aplicacion realiza la ENCRIPTACION Y DESENCRIPTACION ->")
    time.sleep(2)
    # os.system("cls")
    print("[!] esto quiere decir que cuando se ejecute por SEGUNDA vez...->")
    time.sleep(2)
    # os.system("cls")
    print("[!] significara que realizara el DESENCRIPTADO. Por lo talnto...")
    time.sleep(2)
    # os.system("cls")
    print("[*] La DESENCRIPTACION solo se realiza una sola vez [*]")
    time.sleep(2)
    # os.system("cls")
    print("[?] Si se equivoca al ingresar la clave de cifrado, el archivo...")
    time.sleep(2)
    # os.system("cls")
    print("[?] quedara INSERVIBLE")
    print("  20s -> Cargando...")
    time.sleep(25)
    #os.system("cls")
    # Solo permite 2 digitos...
    clave = 77

def logica_directorio_actual():
    ingresar_clave = int(input("[*] Ingrese la clave de encriptacion solo 2 digitos: "))
    directorio_actual = os.getcwd()
    #print(directorio_actual)
    for ruta, carpetas, archivos in os.walk(directorio_actual):
        # clave2 = ingresar_clave
        lista = archivos
        for j in lista:
            if ".jpg" in j:
                # print(os.path.join(ruta, j))
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".png" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".jpeg" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".gif" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".ico" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            else:
                pass

    print("[*] Encriptacion y Desencriptacion completa...")
    time.sleep(2)
    quit()

def logica_directorio_raiz():
    ingresar_clave = int(input("[*] Ingrese la clave de encriptacion solo 2 digitos: "))
    for ruta, carpetas, archivos in os.walk(directorio_raiz):
        # clave2 = ingresar_clave
        lista = archivos
        for j in lista:
            if ".jpg" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".png" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".jpeg" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".gif" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            elif ".ico" in j:
                total = os.path.join(ruta, j)
                encrp_decrip_img2()
            else:
                pass

    print("[*] Encriptacion y Desencriptacion completa...")
    time.sleep(2)
    quit()

def encrp_decrip_img():

    try:

        ruta = input("[*] Ingrese la ruta de la Imagen: ")
        clave = int(input("[*] Ingrese la clave de encriptacion solo 2 digitos: "))

        abrir = open(ruta, "rb")

        imagen = abrir.read()
        abrir.close()

        imagen = bytearray(imagen)

        for index, values in enumerate(imagen):
            imagen[index] = values ^ clave

        abrir = open(ruta, "wb")

        abrir.write(imagen)
        abrir.close()

        print("[*] Encriptacion y Desencriptacion completa...")
        time.sleep(2)
        quit()
    except Exception:
        print("Error:", Exception.__name__)

def encrp_decrip_img2():
    try:

        # La letra < j > representa la coleccion de todas las imajenes en el [for de la condicion]
        ruta2 = total
        clave = ingresar_clave
        abrir = open(ruta2, "rb")

        imagen = abrir.read()
        abrir.close()

        imagen = bytearray(imagen)

        for index, values in enumerate(imagen):
            imagen[index] = values ^ clave

        abrir = open(ruta2, "wb")

        abrir.write(imagen)
        abrir.close()

        #print("[*] Encriptacion y Desencriptacion completa...")
        #quit()
    except Exception:
        print("Error:", Exception.__name__)

def encrp_decrip_img3():

    try:

        ruta = j
        clave = int(input("Ingrese la clave de encriptacion: "))

        abrir = open(ruta, "rb")

        imagen = abrir.read()
        abrir.close()

        imagen = bytearray(imagen)

        for index, values in enumerate(imagen):
            imagen[index] = values ^ clave

        abrir = open(ruta, "wb")

        abrir.write(imagen)
        abrir.close()

        print("[*] Encriptacion y Desencriptacion completa...")
    except Exception:
        print("Error:", Exception.__name__)


print("[1] Encriptar y Desencriptar [una] sola imagen... ")
print("[2] Encriptar y Desencriptar imagen [Directorio actual]")
print("[3] Encriptar y Desencriptar [todas] las Imagenes del equipo... ")
opcion = int(input("[*] Ingresa la opcion: "))
os.system("cls")

# Encripta una sola imagen de su eleccion...
if opcion == 1:
    info()
    encrp_decrip_img()

# Encripta tosas las imagenes del directorio actual...

if opcion == 2:
    info()
    logica_directorio_actual()

# Encripta tosas las imagenes desde el directorio raiz...
if opcion == 3:
    print("[!] Ten cuidado con lo que quieres realizar...")
    print("[!] Por tu seguridad esta opcion no esta avilitada...")
    # time.sleep(4)
    #     print("[1] Si")
    #     print("[2] No")
    #     op2 = input("[?] Deseas continuar...?: ")
    #     if op2 == 1:
    #         logica_directorio_raiz()
    #     if op2 == 2:
    #         time.sleep(2)
    #         print("Saliendo...")
    #         quit()



input("\nPrecione una tecla para continuar...")
