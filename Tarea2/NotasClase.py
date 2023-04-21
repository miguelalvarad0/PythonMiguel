#definicion de funcion que cuenta la cantidad de materias que cursa el estudiante y retorna dicho valor.
#recibe una colección tipo diccionario como input
def contar_cursos(sample_dictionary):
    largo = len(sample_dictionary["class"]["student"]["marks"])
    return largo 

#defincion de funcion que toma la nota de todos las materias cursadas por el estudiante y calcula el promedio de ellas 
# la colecciond de valores(en este caso calificaciones) del diccionario se convierten en lista para poder ser accesados mediente un indice
def calcular_promedio(sample_dictionary,cantidad_cursos):
    suma_notas = 0
    g = list(sample_dictionary["class"]["student"]["marks"].values())

    for i in range(0,cantidad_cursos,1):
        suma_notas = suma_notas + g[i]
    promedio = suma_notas / cantidad_cursos
    return promedio


#Creacion del diccionario, el valor de los keys "name" y "marks" pueden sin alterados sin afectar la funcionalidad del programa,
#ademas se pueden agregar nuevos marks (en este caso materias/cursos)
sampleDict = {
       "class": {
           "student": {
               "name": "Mike",
               "marks": {
                   "physics": 70,
                   "history": 80,
                    "math": 90
                       }
} }
}

#Creacion del diccionario que utilizaremos como herramienta de manejo de datos para el programa 
miDict = {
    "nombre": "nombre",
    "nota": "promedio"
}

#Ejecutar la funcion contar_cursos utilizando el diccionario 'sampleDict' como parametro y asignar el valor retornado a una variable 'a' 
#Ejecutar la funcion calcular_promedio con el diccionario 'sampleDict' como parametro de entrada, y asignar el output de la funcion a una variable 'b' 
#Copiar el valor del key name, del sampleDict al diccionario miDict del cual tomare dicho dato para imprimirlo.
#Asignar una valor de nota (promedio obtenido) al key 'nota' en miDict.
a = contar_cursos(sampleDict)
b = calcular_promedio(sampleDict,a)
miDict["nombre"] = sampleDict["class"]["student"]["name"]
miDict["nota"] = b

#Imprimir en pantalla el nombre del estudiante y su calificación promedio de materias cursadas.
print("Nombre:",miDict["nombre"],", Promedio: ",end="")
print(b)
print("\n")


