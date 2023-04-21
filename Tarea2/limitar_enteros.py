#limitar enteros

#tomando en cuenta que pueden ingresar combinacion de letras y numero y queremos limitar eso entonces...
#sabiendo el largo del string o entero ingresado, podremos mediante un ciclo hacer una evaluacion de cada uno
#de los caracteres usando indexacion y tratando de convertirlo a entero con try and except y si se puede convertir
#sabremos de esa manera que no querremos la cadena string ingresada

string = input("Ingrese una palabra: ")
largo_palabra = len(string)
contador_strings = 0

for i in range(0,largo_palabra,1):
    try:
        entero = int(string[i])
        print("Caso Try: El caracter analizado de La palabra no es valida ya que se puede convertir en un entero BAD")
        
    except ValueError:
        print("Caso except: el caracter es un string GOOD")
        contador_strings = contador_strings + 1 

if contador_strings == largo_palabra:
    print("EJCUTAR PROGRAMA PALABRAS")

else:
    print("NO EJECUTAR PROGRAMA")

