import random
separador = "\n"*15
finDeJuego = False
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
            print("|", "?", end=" ")
        if i[-2] == 1:
            if i[-1] > 0 and i[-1] < 9:
                print("|", i[-1], end=" ")
            if i[-1] == 0:
                print("|", " ", end=" ")
            if i[-1] == -1:
                print("|", chr(164), end=" ")
        if i[-2] == -1:
            print("|", chr(182), end=" ")
    print("|")
    print(" "*7, "-"*((anchura*4)+1), sep="")
def ponerBombas():    
    posiblesBombas=list(len(coordenadas))    
    posiblesBombas.pop(pedirCoordenadaNumero)    
    coodrdenadas[random.sample(posiblesBombas,(3))][-1] #devuelve random de la lista     
##iniciar
##tablero base: 18x14 - 40bombas
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
ponerBombas()    
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
        if coordenadas[pedirCoordenadaNumero][-2] == -1:
            coordenadas[pedirCoordenadaNumero][-2] = 0
        else:
            coordenadas[pedirCoordenadaNumero][-2] = 1
            
            
print ()

