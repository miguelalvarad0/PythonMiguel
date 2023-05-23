import random

class Carta():

    def __init__(self,numero,palo):
        self.numero = numero
        self.palo = palo 

class Deck():

    def __init__(self,lista):
        
        self.lista_cartas = lista
#agregar J Q K A
        valor = ['2','3','4','5','6','7','8','9','10','10','10','10','11']
        palo = ['b','c','d','e']

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

    def __init__(self,dealer_tag,lista):
        self.dealer = dealer_tag
        self.mano = lista
        self.valor = 0
        self.modo  = 'standby'

    def sumar_cartas(self,puntuacion):
        
        puntuacion = puntuacion + int(self.mano[-1].numero)
            
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
        print(f"Suma: {puntuacion}")
    else:
        print("La mano del Jugador1 es:")
        for i in player.mano:
            print(i.numero," ",i.palo)   
        print(f"Suma : {puntuacion}")

finalizar = False
puntuacion_dealer = 0
puntuacion_jugador = 0
lista = []
lista2 = []
lista3 = []
deck = Deck(lista)
deck.barajar()
jugador = Mano(1,lista2)
dealer = Mano(0,lista3)
deck.repartir_carta(jugador)
puntuacion_jugador = jugador.sumar_cartas(puntuacion_jugador)
deck.repartir_carta(jugador)
puntuacion_jugador = jugador.sumar_cartas(puntuacion_jugador)
deck.repartir_carta(dealer)
puntuacion_dealer = dealer.sumar_cartas(puntuacion_dealer)
deck.repartir_carta(dealer)
puntuacion_dealer = dealer.sumar_cartas(puntuacion_dealer)
imprimir_mano(jugador,puntuacion_jugador)
imprimir_mano(dealer,puntuacion_dealer)
while (jugador.modo != 'N' or dealer.modo != 'N'):
    if puntuacion_dealer<18:
        deck.repartir_carta(dealer)
        puntuacion_dealer = dealer.sumar_cartas(puntuacion_dealer)
        print("El dealer decide tomar carta")
        if puntuacion_dealer>21:
            dealer.modo = 'N'
            jugador.modo = 'N'
            finalizar = True
    else:
        dealer.modo = 'N'
        print("El dealer decide no tomar carta")
    if finalizar==False and jugador.modo!='N' and puntuacion_jugador<22 and input("Desea pedir carta? (Digite S o N)") == 'S':
        deck.repartir_carta(jugador)
        puntuacion_jugador = jugador.sumar_cartas(puntuacion_jugador)
        if puntuacion_jugador>21:
            jugador.modo = 'N'
            dealer.modo = 'N'
    else: 
        jugador.modo = 'N'
    imprimir_mano(jugador,puntuacion_jugador)
    imprimir_mano(dealer,puntuacion_dealer)

print (f"Resultdo de la Partida:","\n",f"Dealer : {puntuacion_dealer}","\n",f"Jugador1: {puntuacion_jugador}")
if puntuacion_jugador<22 and puntuacion_dealer>21:
    print('El ganador es el Jugador 1')
elif puntuacion_jugador>21 and puntuacion_dealer<22:
    print('El ganador es el Dealer')
elif puntuacion_jugador<22 and puntuacion_dealer<22:
    if puntuacion_jugador>puntuacion_dealer:
      print('El ganador es el Jugador 1')
    elif puntuacion_jugador==puntuacion_dealer:
        print('Es un empate')
    else:
      print('El ganador es el dealer')
elif (puntuacion_dealer>21 and puntuacion_jugador>21) or (puntuacion_dealer==puntuacion_jugador):
    print('Empate')
    
