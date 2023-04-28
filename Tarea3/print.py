#imprimir en pantalla
def imprimir_menu(): #Imprime menu de opciones en pantalla.
    print("            CALCULADORA")
    print("Digite 1 para Sumar n cantidad de numeros")
    print("Digite 2 para Restar 2 numeros")
    print("Digite 3 para Multiplicar n cantidad de numeros")
    print("Digite 4 para Dividir 2 numeros")
    print("Digite 5 para calcular el Factorial de un numero")
    print("Digite 6 para calcular la potencia de un numero")
    print("Digite 7 para salir del programa\n")

#la funcion recibe una lista cuyo 4to elemento hace referencia al tipo de operacion,y dependendiedo de su valor imprime distinto 
def imprimir_operacion(nuevo_calculo):
    if (nuevo_calculo[3]=="Resta"):
        print(nuevo_calculo[0],"-",nuevo_calculo[1]," = ",nuevo_calculo[2])
    elif (nuevo_calculo[3]=="Factorial"):
        print(nuevo_calculo[0],"!"," = ",nuevo_calculo[2])
    elif (nuevo_calculo[3]=="Potencia"):
        print(nuevo_calculo[0],"^",nuevo_calculo[1]," = ", nuevo_calculo[2])
    else:
        print(nuevo_calculo[0],"/",nuevo_calculo[1]," = ",nuevo_calculo[2])

#imprime en pantalla el caclulo y resultado de una suma
def imprimir_suma(nuevo_calculo,resultado):
    for i in nuevo_calculo:
        print("+", end="")
        print(str(i), end="")
    print(" =",str(resultado)) 

#imprime en pantalla el calculo y resultado de una multiplicación.
def imprimir_mult(nuevo_calculo,resultado):
    for i in nuevo_calculo:
        print("x", end="")
        print(str(i), end="")
    print(" =",str(resultado)) 
