#defino la funcion donde se valida que ambas cadenas de caracteres ingresados contegan la misma cantidad caracteres
#y de ser asi, se procede a imprimir en pantalla de manera intercalada/combinada, los caracteres de las cadenas ingresadas por el usuario
#se utiliza el largo de la cadena de caracteres como numero de veces que se corre el loop en la funcion 
def combinar_palabras(string11, string22):

    if len(string11) != len(string22):
        print("Inserción inválida: \nLas palabras ingresadas no contienen la misma cantidad de letras\n")
    else:
        print("Combinación de Palabras:")

        for i in range(0,len(string1),1):
            print(string11[i],end="")
            print(string22[i],end="")
        print("\n")

#se define la funcion en la cual se verifica que los caracteres de las palabras no sean numeros sino letras
#la funcion retorna un '1' o un '0' si la verificacione o no exitosa 
def validar_palabra(palabra,largo):

    contador_strings = 0
    for i in range(0,largo,1):
        try:
            entero = int(palabra[i])
        
        except ValueError:
            contador_strings = contador_strings + 1 

    if contador_strings == largo:
        return 0
    else:
        return 1


#se piden al usuario las palabras a ser combninadas, se almacena el largo de estas en variables y se usan como parametro de entradas para llamar la funcion validar_palabra
string1 = input("Inserte una palabra:")
string2 = input("Inserte otra palabra con la misma cantidad de letras: ")
largo_palabra1 = len(string1)
largo_palabra2 = len(string2)
validar_palabra(string1,largo_palabra1)
validar_palabra(string2,largo_palabra2)

#si ambas palabras contienen unicamente letras, se llama la funcio combinar_palabras; caso contrario se finaliza el programa
if ((validar_palabra(string1,largo_palabra1) == 0) and (validar_palabra(string2,largo_palabra2) == 0)):
    combinar_palabras(string1,string2)
    print("FIN DEL PROGRAMA\n")    
else:
    print("Palabra invalida : No se permiten números \n\nFIN DEL PROGRAMA")
    print("\n")  

