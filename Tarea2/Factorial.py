#Definir la funcion que recibe caracteres, determina si es un numero natural, y devuelve el resultado del calculo factorial



def calcular_factorial(x):
# se intenta convertir el\los caracteres de entrada a tipo entero y se valida que sea menor a 0,
# en caso de que no se cumpla entonces no se calcula el factorial y se devuelve un msj al usuario indicando que 
# el valor insertado no es valido.
# en caso de que se validen los caracteres como un entero se calcula el factorial mediante un ciclo for
#la cantidad de loops del ciclo for esta definido por el largo del caracter ingresado por el usuario

    try:
        z = int(x)
        
        if z<0:
            print("No es un número válido")
            print("Fin del Programa\n")
        else:
            y=1
            for x in range(1, int(z+1)):
                y = y*x 
            print("El factorial de " + str(z) + " corresponde a " + str(y) + "\nFin del Programa\n")
    except ValueError:
        print("No es un numero valido")
        print("Fin del Programa\n")


#Imprimir Titulo del programa, solicitar un numero al usuario, e invocar la funcion factorial
print("\nCalculadora de Factorial\n")
num = input("Ingrese un numero natural:")
calcular_factorial(num)
         
         