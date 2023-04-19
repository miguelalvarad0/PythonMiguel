from random import randint
import math


listaNumeros = []
listaCubos = []

for i in range(1,randint(1,10)+1,1):
    num = randint(1,99)
    num2 = int(math.pow(num,3))
    listaNumeros.append(num)
    listaCubos.append(num2)

print("Lista de número aleatorios:")    
print(listaNumeros)
print("Lista de numeros al cubo:")
print(listaCubos)

