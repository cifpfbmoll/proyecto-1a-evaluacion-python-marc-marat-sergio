import random
import sys
separador = "\n"*15
finDeJuego = False
bombas = []

##definiremos las funciones arriba
def pedirCoordenada():
    coordenadaX= (input("Escribe una cordenada X: "))
    if coordenadaX == "bandera" or coordenadaX == "b": ##por si quiere poner bandera
        coordenadaX= (input("Escribe una cordenada X para la bandera: "))
        coordenadaY= (input("Escribe una cordenada Y para la bandera: "))
        coordenadaXY = [True, int((int(coordenadaX)-1)+((int(coordenadaY)-1)*anchura))]
        return coordenadaXY
    else:
        coordenadaY= (input("Escribe una cordenada Y: "))
        ##Se le pide al jugador que elija coordenada
        coordenadaXY = [False, int((int(coordenadaX)-1)+((int(coordenadaY)-1)*anchura))]
        return coordenadaXY
def actualizarTablero(): ## de esto me encargo yo (mucha mierda - poco jugo)
    print(separador)
    print(" "*9, sep="", end="")
    for j in range(anchura):
        print((j+1), sep="", end="   ")
    print("\n")
    print(" "*7, "-"*((anchura*4)+1), sep="")
    print("1", " "*5, end="")
    for i in coordenadas:
        if (coordenadas.index(i)) != 0:
            if (coordenadas.index(i))%anchura == 0:
                print("|")
                print(" "*7, "|", "-"*((anchura*4)-1), "|", sep="")
                print((int(coordenadas.index(i)/anchura)+1), " "*(6 - (len(str(int(coordenadas.index(i)/anchura)+1)))), end="")
        if i[-2] == 0:
            print("\033[1;37;40m|", "\033[0;32;40m?", end="\033[1;37;40m ")
        if i[-2] == 1:
            if i[-1] > 0 and i[-1] < 9:
                print("\033[1;37;40m|", "\033[0;34;40m ", i[-1], end="\033[1;37;40m ", sep="")
            if i[-1] == 0:
                print("|", " ", end=" ")
            if i[-1] == -1:
                print("\033[1;37;40m|", "\033[0;31;40m ", chr(164), end="\033[1;37;40m ", sep="")
        if i[-2] == -1:
            print("\033[1;37;40m|", "\033[0;31;40m ", chr(182), end="\033[1;37;40m ", sep="")
    print("|")
    print(" "*7, "-"*((anchura*4)+1), sep="")
##iniciar
##tablero base: 18x14 - 40bombas
def ponerBombas():
    posiblesBombas=list(range(len(coordenadas)))
    posiblesBombas.pop(pedirCoordenadaNumero)
    posiblesBombas = random.sample(posiblesBombas,(int((anchura*altura)//6.3)))
    for k in posiblesBombas:
        coordenadas[k][-1] = -1
anchura = int(input("Anchura del tablero: ")) ##selecciona anchura tablero (x)
altura = int(input("Altura del tablero: ")) ##seleccionar altura tablero (y)
coordenadas=[] ##se declara la lista vacia para meter las coordenadas
for x in range(anchura): ##se crean las coordenadas
  for y in range(altura):
    coordenadas.append([x + 1, y + 1, 0, 0])
    ## estructura de las listas anidadas:
    ##(coordenadaX, coordenadaY, descubierto?, contenido)
    ## descubierto? puede tomar los valores 0 (no descubierto), 1(descubierto) y -1(con bandera)
    ## el contenido puede ser 0(vacio), 1, 2, 3, 4, 5, 6, 7, 8 o -1(bomba)
casillasAbiertas = 0
while finDeJuego == False:
    actualizarTablero()
    coordenadaActual = pedirCoordenada()
    pedirCoordenadaNumero = coordenadaActual[1]
    pedirCoordenadaBandera = coordenadaActual[0]
    if pedirCoordenadaBandera == True:
        if coordenadas[pedirCoordenadaNumero][-2] == -1:
            coordenadas[pedirCoordenadaNumero][-2] = 0
        elif coordenadas[pedirCoordenadaNumero][-2] == 0:
            coordenadas[pedirCoordenadaNumero][-2] = -1
    if pedirCoordenadaBandera == False:
        coordenadas[pedirCoordenadaNumero][-2] = 1
        if casillasAbiertas == 0:
            ponerBombas()
        casillasAbiertas =+ 1
        if coordenadas[pedirCoordenadaNumero][-1] == -1:
            actualizarTablero()
            print("\nHAS PERDIDO!")
            finDeJuego=True