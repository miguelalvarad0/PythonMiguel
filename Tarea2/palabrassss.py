string1 = input("Inserte la primera palabra:")
string2 = input("Inserte otra palabra con las misma cantidad de letras: ")


if len(string1) != len(string2):
    print("Inserción inválida: \nLas palabras ingresadas no contienen la misma cantidad de letras")
else:
    print("Combinación de Palabras:")

    for i in range(0,len(string1),1):
        print(string1[i],end="")
        print(string2[i],end="")

print("\n")        


# falta restringir el ingreso de numeros...