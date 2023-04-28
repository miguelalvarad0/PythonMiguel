#Librerias con funciones de importacion de fecha y hora, y de pausado en la ejecucion del programa.
from datetime import datetime
import time

#borra todo el contenido presente en el archivo 'Datalog.txt'
def limpiar_datalog():
    file = open("Datalog.txt", "w")
    file.write("")
    file.close()

#la funcion recibe una operacion y la almacena en el archivo de texto.
def guardar_operacion(nuevo_calculo):
    input("Presione Enter para guardar y volver al Menu Principal...")#espera la tecla enter para continuar
    print("La operación esta siendo exportada al datalog....... 20%")#notificacion de progreso en almacenamiento de datos.
    time.sleep(1)#detiene la ejecucion del codigo por un segundo
    file = open("Datalog.txt","a") #abre el archivo de texto y agrega contenido al final de este (en una nueva linea)
    file.write("--------------------\n") #escribe contenido en el archivo de texto
    now = datetime.now() #guarda la fecha y hora exacta en una variable 
    string_aux= "Date: " + str(now.day) +"/"+str(now.month)+"/"+ str(now.year)+ "  Time: "+str(now.hour)+":"+ str(now.minute)+"\n"
    file.write(string_aux) #escribe fecha y hora en el archivo de texto con un formato adecuado.

    #segun el tipo de operacion se corren distintas intrucciones para escribir los calculos y resultados en el archivo de text.
    #el tipo de operacion viene indicado en el 4to elemento de la lista 'nuevo_calculo'
    if (nuevo_calculo[3]=="Resta"):
        file.write(str(nuevo_calculo[0]))
        file.write(str("-"))
        file.write(str(nuevo_calculo[1]))
        file.write(str("="))
        file.write(str(nuevo_calculo[2]))
    elif (nuevo_calculo[3]=="Factorial"):
        file.write(str(nuevo_calculo[0]))
        file.write("! = ")
        file.write(str(nuevo_calculo[2]))
    elif (nuevo_calculo[3]=="Potencia"):
        file.write(str(nuevo_calculo[0]))
        file.write("^")
        file.write(str(nuevo_calculo[1]))
        file.write("=")
        file.write(str(nuevo_calculo[2]))
    else:
        operacion=nuevo_calculo[0],"/",nuevo_calculo[1]," = ",nuevo_calculo[2]
        file.write(str(nuevo_calculo[0]))
        file.write("/")
        file.write(str(nuevo_calculo[1]))
        file.write("=")
        file.write(str(nuevo_calculo[2]))

    #escribir en el archivo de respaldo: los operadores que componen la operacion y el resultado de la misma.
    print("La operación esta siendo exportada al datalog....... 74%")#notificacion de progreso en copia de datos al archivo.
    time.sleep(2)#detiene la ejecucion del programa por 2 segundos para ganar atencion en el ultimo comentario impreso.
    file.write("\nOperación: ")
    file.write(str(nuevo_calculo[3]))
    file.write("  Resultado: ")
    file.write(str(nuevo_calculo[2]))
    print("La operación esta siendo exportada al datalog....... 80%")
    time.sleep(1)
    if nuevo_calculo[3]=="Factorial":    
        texto = "  Operadores: " + str(nuevo_calculo[0])
    else:
        texto = "  Operadores: " + str(nuevo_calculo[0]) + ", " + str(nuevo_calculo[1])
    file.write(texto)
    file.write("\n")
    file.close()
    print("La operación ha sido EXPORTADA EXITOSAMENTE!........ 100%\n")

#escribir el calculo de la operacion en un archivo de respaldo, asi como sus operadores y resultado.Tambien escribe hora exacta.
def guardar_suma(nuevo_calculo,resultado):
    input("Presion Enter para guardar y continuar...")
    file = open("Datalog.txt","a")
    file.write("--------------------\n")
    now = datetime.now()
    string_aux= "Date: " + str(now.day) +"/"+str(now.month)+"/"+ str(now.year)+ "  Time: "+str(now.hour)+":"+ str(now.minute)+"\n"
    file.write(string_aux)
    for i in nuevo_calculo:      
        file.write("+")
        file.write(str(i))
    file.write(" =")
    file.write(str(resultado))
    file.write("\nOperación: Suma  ")
    file.write("Resultado: ")
    file.write(str(resultado))
    print("La operación esta siendo exportada al datalog....... 74%")
    time.sleep(2)
    file.write("  Operadores: ")
    for i in nuevo_calculo:
        file.write(str(i))
        file.write(", ")
    file.write("\n")
    file.close()
    print("La operación ha sido EXPORTADA EXITOSAMENTE!........ 100%\n")
    
#escribir el calculo de la operacion en un archivo de respaldo, asi como sus operadores y resultado.Tambien escribe hora exacta.
def guardar_mult(nuevo_calculo, resultado):
    input("Presione Enter para guardar y volver al Menu Principal...")
    print("La operación esta siendo exportada al datalog....... 20%")
    time.sleep(1)
    file = open("Datalog.txt","a")
    file.write("--------------------\n")
    now = datetime.now()
    string_aux= "Date: " + str(now.day) +"/"+str(now.month)+"/"+ str(now.year)+ "  Time: "+str(now.hour)+":"+ str(now.minute)+"\n"
    file.write(string_aux)
    for i in nuevo_calculo:      
        file.write("*")
        file.write(str(i))
    file.write(" =")
    file.write(str(resultado))
    file.write("\nOperación: Multiplicacion  ")
    print("La operación esta siendo exportada al datalog....... 74%")
    time.sleep(1)
    file.write("Resultado: ")
    file.write(str(resultado))
    print("La operación esta siendo exportada al datalog....... 80%")
    time.sleep(2)
    file.write("  Operadores: ")
    for i in nuevo_calculo:
        file.write(str(i))
        file.write(", ")
    file.write("\n")
    file.close()
    print("La operación ha sido EXPORTADA EXITOSAMENTE!........ 100%\n")

