def hola(x):
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

print("\nCalculadora de Factorial\n")
num = input("Ingrese un numero natural:")
hola(num)
