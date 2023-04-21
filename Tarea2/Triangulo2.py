#Se define la funcion en la cual se verifica que el caracter/caracteres ingresado$ correspondaN a un numero entero mayor a cero 
# en caso valido, se utiliza un ciclo de impresion de digitos en columnas, dentro de un ciclo de impresion en filas  
def triangulo(x):
    try:
        z = int(x)
        
        if z<1:
            print("No es un número válido")
            print("Fin del Programa\n")
        else:
            print("\nTRIANGULO\n")
            for i in range(1,z+1,1):
                print("")
                for y in range(1,i+1,1):
                    print(y,end=" ")
    
            print("\n")
            
    except ValueError:
        print("No es un numero valido")
        print("Fin del Programa\n")

#Se pide un numero al usuario, se almacena en la variable 'num' y se utiliza como parametro de entrada para llamar a funcion 'triangulo'
num = input("Ingrese un numero entero positivo:")
triangulo(num)

