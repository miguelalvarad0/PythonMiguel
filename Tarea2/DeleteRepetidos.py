# Importar librerias a utilizar : operaciones matematicas y de sorteo aleatorio
from random import randint
import math

# Inicializar la lista que se llenara aleatoriamente 
listaNumeros = []

#Llenar la lista con 15 numeros aleatorios del 1 al 3
for i in range(1,16,1):
    num = randint(1,3)
    listaNumeros.append(num)

# Crear un set a partir de la lista de 15 numeros, de manera que se eliminaran todos los numeros repetidos en la lista
set1 = set(listaNumeros)

#Imprimir lista y set en pantalla 
print("Lista aleatoria con números del 1 al 3:")    
print(listaNumeros)
print("Nueva lista SIN REPETIDOS:")
print(set1)

