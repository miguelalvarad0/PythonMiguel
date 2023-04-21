#Importar librerias de operaciones matematicos y sorteo aleatorio 
from random import randint
import math

#Inicializar lista de numeros aleatorios, y lista de cubos de los numeros aleatorios 
listaNumeros = []
listaCubos = []

#el ciclo se correra una cantidad de veces aleatoria (entre 1 y 10 veces),
# y por cada loop se agregara un numero aleatorio (entre 1 y 99)a la lista
#y a su vez se calculara el cubo de ese numero aleatorio para agregarlo entonces a la segunda lista de cubos 
for i in range(1,randint(1,10)+1,1):
    num = randint(1,99)
    num2 = int(math.pow(num,3))
    listaNumeros.append(num)
    listaCubos.append(num2)

#Imprimir ambas listas en pantalla (lista numeros aleatorios y lista de cubos de numeros aleatorios)
print("Lista de números aleatorios del 1 al 99:")    
print(listaNumeros)
print("Lista de numeros al cubo:")
print(listaCubos)

