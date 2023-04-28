#importa libreria con funciones matematicas para hacer uso del math.pow 
import math

#recibe una lista de numeros y calcula el resultado de la suma.
def calcular_suma(nuevo_calculo):    
    resultado = 0 
    for i in nuevo_calculo:
        resultado = resultado + int(i)
    return resultado 

#recibe una lista de numeros y retorna el resultado de su multiplicacion, utiliza un ciclo para recorrer la lista.
def calcular_mult(nuevo_calculo):
    resultado = 1
    for i in nuevo_calculo:
        resultado = resultado*int(i)
    return resultado

#caclula una potencia dados dos numeros como entrada de la funcion utilizando math.pow de la libreria math
def calcular_potencia():
    lista = []
    print("\nElevar a la potencia")
    num1 = int(input("Numero Base: "))
    num2 = int(input("Numero Exponente: "))
    resultado = math.pow(num1,num2)
    lista.append(num1)#agrega operadores a la lista
    lista.append(num2)
    lista.append(resultado)#agrega resultado a la lista
    lista.append("Potencia")#agrega tipo de operacion a la lista
    return lista

#recibe dos numeros y los devuelve empaquetados en una lista junto con el resultado de su resta.
def restar_numeros():
    lista = []
    print("\nRESTA")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    resultado = num1 - num2
    lista.append(num1)
    lista.append(num2)
    lista.append(resultado)
    lista.append("Resta")
    return lista

#recibe dos numeros y los devuelve empaquetados en una lista junto con el resultado de su division.
def dividir_numeros():
    lista = []
    print("\nDIVISION")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    resultado = num1 / num2
    lista.append(num1)
    lista.append(num2)
    lista.append(resultado)
    lista.append("Division")
    return lista


#se calcula el factorial de un numero recibido y se devuelve una lista con el operador y el resultado de la operacion.
def calcular_factorial(x):
# se intenta convertir el\los caracteres de entrada a tipo entero y se valida que sea menor a 0,
    lista = []
    try:  #se trata de convertir el parametro/variable de entrada a un entero para comprobar que sea un numero
        z = int(x)
        
        if z<0: #no se aceptan numeros negativos, si se detecta uno se imprime un mensaje con advertencia.
            print("No es un número válido")
            print("Fin del Programa\n")
        else:
            y=1
            for x in range(1, int(z+1)):  #se utiliza un ciclo con una variable acumulativa para el calculo de la operacion
                y = y*x 
            
            lista.append(z)
            lista.append(z)
            lista.append(str(y))
            lista.append("Factorial") #se guardan en una lista el operador, el resultado, y el tipo de operacion.
            return lista 
    except ValueError: #si la variable no se puede convertir a entero entonces se advierte que no es valida
        print("No es un numero valido")
        print("Fin del Programa factorial\n")
