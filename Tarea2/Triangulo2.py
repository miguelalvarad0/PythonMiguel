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
            #y=1
            #for x in range(1, int(z+1)):
                #y = y*x 
            #print("El factorial de " + str(z) + " corresponde a " + str(y) + "\nFin del Programa\n")
    except ValueError:
        print("No es un numero valido")
        print("Fin del Programa\n")

num = input("Ingrese un numero entero positivo:")
triangulo(num)

