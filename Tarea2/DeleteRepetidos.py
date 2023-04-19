from random import randint
import math

# evaluar quitar esta deifinicion de variable
listaNumeros = []


for i in range(1,16,1):
    num = randint(1,3)
    listaNumeros.append(num)

set1 = set(listaNumeros)


print("Lista aleatoria con números del 1 al 3:")    
print(listaNumeros)
print("Nueva lista SIN REPETIDOS:")
print(set1)
