def contar_cursos(sample_dictionary):
    largo = len(sample_dictionary["class"]["student"]["marks"])
    return largo 

def calcular_promedio(sample_dictionary,cantidad_cursos):
    suma_notas = 0
    g = list(sample_dictionary["class"]["student"]["marks"].values())

    for i in range(0,cantidad_cursos,1):
        suma_notas = suma_notas + g[i]
    promedio = suma_notas / cantidad_cursos
    return promedio

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

miDict = {
    "nombre": "nombre",
    "nota": "promedio"
}

a = contar_cursos(sampleDict)
b = calcular_promedio(sampleDict,a)
miDict["nombre"] = sampleDict["class"]["student"]["name"]
miDict["nota"] = b

print("Nombre:",miDict["nombre"],", Promedio: ",end="")
print(b)
print("\n")


