def eliminar_elemento(elemento,lista):
    #se mantiene una copia de la lista original (sin eliminar elementos)
    lista2 = lista.copy()  

    #se compara el elemento por eliminar con todos los elementos de la lista original..si coincide,se elimina de la lista final
    for i in lista2:
        if i==elemento or str(i)==elemento or i==str(elemento) or str(i)==str(elemento): 
            lista.remove(i)

    print("\n","Input:","\n",lista2,f" => {elemento}","\n","Resultado:","\n",lista,"\n") 


def calcular_distribucion_caracteres(estring):
    largo = len(estring)
    numeros = 0
    letras = 0
    especiales = 0

    #se determina si cada caracter corresponde a un digito(numero), a un 'alphabetic'(letras) o a ninguna de ellas (caracter especial). Se utiliza un contador separado para cada uno de ellos.
    for i in range (0,largo):
        boool = estring[i].isdigit()
        bool3 = estring[i].isalpha()
        if boool == True:
            numeros += 1
        if bool3 == True:
            letras += 1
        if boool == False and bool3 == False:
            especiales += 1

    print("\n", "Input: ","\n",estring,"\n\n", "Resultado: ","\n",f"Numeros = {numeros}","\n", f"Letras = {letras}","\n", f"Caracteres Especiales = {especiales}","\n")
    

def omitir_comas(cadena):

    #lista es la lista final que va contener los numeros separados por las comas 
    lista = []

    #listita va acumulando los digitos de numeros de 2 o más digitos, antes de agregarlos a 'lista'
    listita = []

    #comparadora es simplemente una lista vacia..que usaré para comparar con otras listas y saber si tambien están vacías
    comparadora = []

    largo = len(cadena) 


    for i in range(0,largo):

        #este if me indica si estoy en el ultimo elemento de la lista 
        if i == largo-1:
            #este if me indica si el caracter siguiente es un numero o una coma 
            if cadena[i].isdigit()==True:
                #este if me indica si el elemento anterior corresponde a un numero o una coma
                if listita == comparadora:
                        lista.append(cadena[i])
                else:
                    sstring = ""
                    listita.append(cadena[i])  
                    #este 'for' convierte los digitos acumulados en listita en un solo numero de varios digitos                 
                    for x in listita:
                        sstring += x
                    lista.append(sstring)  
                    listita = []
        else:
            if cadena[i].isdigit()==True:
                if cadena[i+1].isdigit()==False:
                    if listita == comparadora:
                        lista.append(cadena[i])
                    else:
                        sstring = ""
                        listita.append(cadena[i])                    
                        for x in listita:
                            sstring += x
                        lista.append(sstring)
                        listita = []
                else:
                    listita.append(cadena[i])
    
    tupla = tuple(lista)
    print("\n","Input:","\n",cadena,"\n","Resultado:","\n","Lista:",lista,"\n","Tupla:",tupla,"\n")
    

def contar_letras(palabra):
    
    Dict = {}   
    lista_letras = []
    
    #crear una lista con las letras contenidas en la palabra...mas facil trabajarlo en lista para recorrerlo y para convertirla en set
    for i in palabra:
        lista_letras.append(i)
    
    #eliminar letras repetidas de la lista
    set1 = set(lista_letras)

    #por cada letra contenida en el set, se hace un conteo de repeticiones en la palabra y se almacena el resultado en diccionario
    for i in set1:
        contador = 0
        for z in lista_letras:
            if z==i:
                contador+=1
        Dict[i] = contador
        
    
    print("\n","Input:","\n",palabra,"\n\n","Resultado:","\n",Dict,"\n")


#------------------------------------
#PROBLEMA 1

#Test case 1:
#g = "Empanadáñ"
#calcular_distribucion_caracteres(g)

#Test case 2:
#g = "hoy es 15!"
#calcular_distribucion_caracteres(g)

#Test case 3:
#g = "P@#yn26at^&i5ve"
#calcular_distribucion_caracteres(g)

#Test case 4:
#g = "1990"
#calcular_distribucion_caracteres(g)

#Test case 5:
#g = "+_="
#calcular_distribucion_caracteres(g)

#-----------------------------------
#PROBLEMA 2

#Test case 1:
#palabra = 'perro'
#contar_letras(palabra) 

#Test case 2:
#palabra = 'PeRro'
#contar_letras(palabra)

#Test case 3:
#palabra = '555221'
#contar_letras(palabra)

#Test case 4:
#palabra = 'papaya'
#contar_letras(palabra)

#------------------------------------
#PROBLEMA 3

#Test case 1:
#lista = ["c",'7',7,"b"]
#elemento = '7'
#eliminar_elemento(elemento,lista)

#Test case 2:
#lista = ["c",'5',5,"b",6]
#elemento = 5
#eliminar_elemento(elemento,lista)

#Test case 3:
#lista = ["fresa","sandía","papaya","papaya"]
#elemento = 'papaya'
#eliminar_elemento(elemento,lista)

#Test case 4:
#lista = ["hola","HOLA"]
#elemento = "hola"
#eliminar_elemento(elemento,lista)

#-------------------------------------
#PROBLEMA 4

#Test case 1:
#cadena = '1,2,3,4,5,6'
#omitir_comas(cadena)

#Test case 2:
#cadena = ',6,7,8'
#omitir_comas(cadena)

#Test case 3:
#cadena = '9,10,11,123,5,5,'
#omitir_comas(cadena)

#Test case 4:
#cadena = '100,2,,,34567,,4,557'
#omitir_comas(cadena)


