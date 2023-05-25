import random
import os
import time
from datetime import datetime


class Carta():

    def __init__(self,numero,palo):
        self.numero = numero
        self.palo = palo 

class Deck():

    def __init__(self,lista):
        
        self.lista_cartas = lista
#agregar J Q K A
        valor = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palo = ['\u2764', '\u2666', '\u2660', '\u2618']

        for val in valor:
            for pal in palo:
                self.lista_cartas.append(Carta(val,pal))

    def barajar(self):
        lista_cartas = random.shuffle(self.lista_cartas)    

    def repartir_carta(self,mano):
        carta = self.lista_cartas[0]
        self.lista_cartas.pop(0)
        mano.mano.append(carta)

class Mano():

    def __init__(self,dealer_tag,lista,usuario):
        self.dealer = dealer_tag
        self.mano = lista
        self.valor = 0
        self.modo  = 'standby'
        self.usuario = usuario 

    def sumar_cartas(self,puntuacion):
        if self.mano[-1].numero.isdigit() == True:
            puntuacion = puntuacion + int(self.mano[-1].numero)
        else:
            if self.mano[-1].numero == 'J' or self.mano[-1].numero == 'Q' or self.mano[-1].numero == 'K':
                puntuacion = puntuacion + 10
            else: 
                puntuacion = puntuacion + 11
                if puntuacion > 21:
                    puntuacion = puntuacion - 10     
        return(puntuacion)
    
    def retornar_valor(self):
        return(self.valor)
  
    
def imprimir_mano(player,puntuacion):
    if player.dealer == 0:
        largo = len(player.mano)
        print("La mano del dealer es:")
        print('X   X')
        for i in range(1,largo):
            print(player.mano[i].numero," ",player.mano[i].palo)
        print(f"Suma: ?\n")
       
    else:
        print(f"La mano de {player.usuario} es:")
        for i in player.mano:
            print(i.numero," ",i.palo)   
        print(f"Suma : {puntuacion}\n")
      
def contar_sietes(mano):
    contador = 0
    lista = []
    for i in mano.mano:
        lista.append(i.numero)
    #por cada letra contenida en el set, se hace un conteo de repeticiones en la palabra y se almacena el resultado en diccionario
    for i in lista:
        if i == '7':
            contador = contador + 1
    return(contador)

def imprimir_menu(): #Imprime menu de opciones en pantalla.
    print("\n             BLACK JACK")
    print("Digite 1 para seleccionar usuario y comenzar a jugar")
    print("Digite 2 para ver las Estadísticas")
    print("Digite 3 para salir \n")

def print_users():
    numerador = 0
    f = open('usuarios.txt', 'r')
    userlist = []
    for line in f:
        userlist.append(line.rstrip('\n'))
    f.close()
    for i in userlist:
        numerador = numerador + 1
        print(f'{numerador}. {i}')
    

def get_users():
    numerador = 0
    f = open('usuarios.txt', 'r')
    userlist = []
    for line in f:
        userlist.append(line.rstrip('\n'))
    f.close()
    for i in userlist:
        numerador = numerador + 1
        print(f'{numerador}. {i} {get_scores(i)}')


def get_scores(usuario):
    score = 0
    f = open(f'{usuario}.txt', 'r')
    for line in f:
        if line.rstrip('\n') == 'GANE':
            score = score + 1
    f.close()
    return score 


def main(): 
    imprimir_menu()
    select = int(input(" "))
    if select == 1:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        print("\nUSUARIOS")

        file9 = open('usuarios.txt','a')
        file9.close()
        print_users()
        usuario = input ('Escriba el usuario a utilizar, si no existe se creara uno nuevo:')
        os.system('clear')

        repetido = False
        resultado = 'por jugarse'
        select = 0
        plantarse = 0 
        finalizar = False
        puntuacion_dealer = 0
        puntuacion_jugador = 0
        lista = []
        lista2 = []
        lista3 = []
        deck = Deck(lista)
        deck.barajar()
        jugador = Mano(1,lista2,usuario)
        dealer = Mano(0,lista3,'Dealer')
        deck.repartir_carta(jugador)
        auxi = jugador.sumar_cartas(puntuacion_jugador)
        puntuacion_jugador = auxi
        deck.repartir_carta(jugador)
        auxi = jugador.sumar_cartas(puntuacion_jugador)
        puntuacion_jugador = auxi
        deck.repartir_carta(dealer)
        aux = dealer.sumar_cartas(puntuacion_dealer)
        puntuacion_dealer = aux
        deck.repartir_carta(dealer)
        aux1 = dealer.sumar_cartas(puntuacion_dealer)
        puntuacion_dealer = aux1
        imprimir_mano(jugador,puntuacion_jugador)
        imprimir_mano(dealer,puntuacion_dealer)

        while (jugador.modo != 'N' or dealer.modo != 'N'):


            if finalizar==False and jugador.modo!='N' and puntuacion_jugador<22 and input("Desea pedir carta? (Digite S o N)") == 'S':
                deck.repartir_carta(jugador)
                auxi = jugador.sumar_cartas(puntuacion_jugador)
                puntuacion_jugador = auxi
                if puntuacion_jugador>21:
                    jugador.modo = 'N'
                    dealer.modo = 'N'
            else:  
                jugador.modo = 'N'



            if puntuacion_dealer<17:
                deck.repartir_carta(dealer)
                aux = dealer.sumar_cartas(puntuacion_dealer)
                puntuacion_dealer = aux
                input('\nPRESIONE ENTER para ver la movida del dealer...')
                os.system('clear')
                print("\nEl dealer decide tomar carta")
                print('Cargando...')
                time.sleep(4)
            else:
                dealer.modo = 'N'
                if plantarse == 0:
                    input('\nPRESIONE ENTER para ver la movida del dealer...')
                    os.system('clear')
                    print("\nEl dealer decide no tomar carta y plantarse")
                    print('Cargando...')
                    plantarse = 1
                    time.sleep(4)
                else:
                    input('\n PRESIONE ENTER para ver la movida del dealer...')
                    os.system('clear')
                    print("\nDealer plantado, no puede tomar carta")
                    print('Cargando...')
                    time.sleep(4)

            






            if contar_sietes(dealer)==3 or contar_sietes(jugador)==3:
                dealer.modo = 'N'
                jugador.modo = 'N'

            os.system('clear')
            imprimir_mano(jugador,puntuacion_jugador)
            imprimir_mano(dealer,puntuacion_dealer)

        print('------------------------------------')
        print (f"\n\nRESULTADO DE LA PARTIDA:","\n",f"Dealer : {puntuacion_dealer}","\n",f"{jugador.usuario}: {puntuacion_jugador}")

        if contar_sietes(dealer)==3:
            resultado = 'PERDIDA'
            print('El dealer GANA con triple 7')
        elif contar_sietes(jugador)==3:
            resultado = 'GANE'
            print(f'{jugador.usuario} gana con triple siete')
        else:
            if puntuacion_jugador<22 and puntuacion_dealer>21:
                resultado = 'GANE'
                print(f'El ganador es {jugador.usuario}')
            elif puntuacion_jugador>21 and puntuacion_dealer<22:
                resultado = 'PERDIDA'
                print('El ganador es el Dealer')
            elif puntuacion_jugador<22 and puntuacion_dealer<22:
                if puntuacion_jugador>puntuacion_dealer:
                    resultado = 'GANE'
                    print(f'El ganador es {jugador.usuario}')
                elif puntuacion_jugador==puntuacion_dealer:
                    resultado = 'EMPATE'
                    print('Es un empate')
                else:
                    resultado = 'PERDIDA'
                    print('El ganador es el dealer')
            elif (puntuacion_dealer>21 and puntuacion_jugador>21) or (puntuacion_dealer==puntuacion_jugador):
                resultado = 'EMPATE'
                print('Empate')
        file5 = open ('usuarios.txt','a')
        file5.close()
        file = open('usuarios.txt','r')
        for line in file:
            z = line.strip('\n')
            if z.lower() == jugador.usuario.lower():
                repetido = True
        if repetido == False:
            file.close()
            file3 = open('usuarios.txt','a')
            file3.write(f'{jugador.usuario}\n')
            file3.close()
        
        file2 = open(f'{jugador.usuario}.txt','a')
        file2.write(f'{resultado}\n')
        file2.close()

        input('presione enter para continuar...')
        #time.sleep() #detiene la ejecucion del codigo por unos instantes 
        os.system('clear')
        main()
    elif select == 2:
        os.system('clear')
        print('ESTADISTICAS\n')
        get_users()
        input('\nPresione ENTER para volver al Menu Principal')
        os.system('clear')
        main()
    else:
        os.system('clear')
        return""   #fin del programa


main()
