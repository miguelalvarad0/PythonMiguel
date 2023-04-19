
sampleDict = {
       "class": {
           "student": {
               "name": "Mike",
               "marks": {
                   "physics": 70,
                   "history": 80,
                    "math": 90, }
} }
}

physics = sampleDict["class"]["student"]["marks"]["physics"] 
history = sampleDict["class"]["student"]["marks"]["history"]
math = sampleDict["class"]["student"]["marks"]["math"]

nombre = sampleDict["class"]["student"]["name"]

promedio = (physics+history+math)/3

miDict = {
    "nombre": nombre,
    "nota": promedio
}

print("Nombre:",miDict["nombre"],", Promedio: ",miDict["nota"])

