#Importar libreria "universales" para limpiar pantalla de terminal o pausar la ejecucion del codigo por instantes.
import os
import time

#Importar mi funcion para reproduccion de los resultados en audio.
from audio import reproducir_audio 

#Importar mis funciones para imprimir en pantalla 
from print import imprimir_menu
from print import imprimir_operacion
from print import imprimir_suma
from print import imprimir_mult

#Importar las funciones de mi libreria "data_manage". data_manage contiene funciones para manejo de archivo de texto
from data_manage import limpiar_datalog  
from data_manage import guardar_operacion
from data_manage import guardar_suma
from data_manage import guardar_mult

#Importar funciones de mi libreria calculos para realizar las distintas operaciones matematicas requeridas
from calculos import calcular_suma
from calculos import calcular_mult
from calculos import calcular_potencia
from calculos import restar_numeros
from calculos import dividir_numeros
from calculos import calcular_factorial

#Solicita datos al usuario hasta que éste decida detenerse, los almacena en una lista y la retorna.
def solicitar_numeros():
    lista = []
    bool = True
    while bool :
        num = input("Ingrese un nuevo Numero o el caracter '=' para finalizar la operacion:")
        if num=="=":
            bool=False               
            return lista
        else:
            lista.append(num)

#Codigo Main:Muestra opciones en pantalla y ejecuta un conjunto de funciones según la operacion seleccionada por el usuario.
def main_calculadora(): 
    imprimir_menu()
    select = int(input(" "))
    if select == 1:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        print("\nSUMA")
        numeros = solicitar_numeros() #pide datos de entrada al usuario
        resultado_operacion = calcular_suma(numeros) #calcula el resultado de la operacion matematica
        reproducir_audio(resultado_operacion) #reproduce en audio el resultado del calculo 
        imprimir_suma(numeros,resultado_operacion) #imprime la operacion y resultado en pantalla
        guardar_suma(numeros,resultado_operacion) #hace un backup de la solucion de la operacion en un archivo de respaldo
        time.sleep(2.5) #detiene la ejecucion del codigo por unos instantes 
        os.system('clear')
        main_calculadora()
    elif select == 2:
        os.system('clear')
        numeros = restar_numeros()
        reproducir_audio(numeros[2])
        imprimir_operacion(numeros)
        guardar_operacion(numeros)
        time.sleep(2.5)
        os.system('clear')
        main_calculadora()
    elif select == 3:
        os.system('clear')
        print("\nMULTIPLICACION")
        numeros = solicitar_numeros()
        resultado_operacion = calcular_mult(numeros)
        reproducir_audio(resultado_operacion)
        imprimir_mult(numeros,resultado_operacion)
        guardar_mult(numeros,resultado_operacion)
        time.sleep(2.5)
        os.system('clear')
        main_calculadora()    
    elif select == 4:
        os.system('clear')
        calculo = dividir_numeros()
        reproducir_audio(calculo[2])
        imprimir_operacion(calculo)
        guardar_operacion(calculo)
        time.sleep(2.5)
        os.system('clear')
        main_calculadora()
    elif select == 5:
        os.system('clear')
        print("\nCalculadora de Factorial\n")
        num = input("Ingrese un numero natural:")
        calculo = calcular_factorial(num)
        reproducir_audio(calculo[2])
        imprimir_operacion(calculo)
        guardar_operacion(calculo)
        time.sleep(2.5)
        os.system('clear')
        main_calculadora()
    elif select == 6:
        os.system('clear')
        calculo = calcular_potencia()
        reproducir_audio(calculo[2])
        imprimir_operacion(calculo)
        guardar_operacion(calculo)
        time.sleep(2.5)
        os.system('clear')
        main_calculadora()
    else:
        return""   #fin del programa

#Limpia el archivo de respaldo y ejecuta la funcion principal / Muestra opciones en pantalla y espera seleccion del usuario.
limpiar_datalog()
main_calculadora()
