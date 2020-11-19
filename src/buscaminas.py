import random
separador = "\n"*15
##definiremos las funciones arriba
def pedirCoordenada():
    coordenadaX= int(input("Escribe una cordenada X: "))
    coordenadaY= int(input("Escribe una cordenada Y: "))
    ##Se le pide al jugador que elija coordenada
    coordenadaXY = coordenadas[(coordenadaY-1)+((coordenadaX-1)*altura)]
    return coordenadaXY
    ##se localiza la coordenada
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
    ## el contenido puede ser 0(vacio), 1, 2, 3, 4, 5, 6, 7, 8, -1(bomba) o -2(bandera)
