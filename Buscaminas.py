import random
separador = "\n"*15 #15 saltos de linea para mejorar la meta-interfaz
finDeJuego = False #Esta variable se encarga de parar el bucle del programa principal
INDICEDEBOMBAS = 6.3 #Tablero original = 18x14 - 40bombas 18*14/40=6.3
coordenadas=[] #Se declara la lista vacia para meter las coordenadas


def pedirCoordenada(): #Pide al jugador las coordenadas XY que quieres descubrir
    coordenadaX = (input("Escribe una cordenada X: "))  #Si quiere poner una bandera
    if coordenadaX == "bandera" or coordenadaX == "b": #coordenadaX tiene que ser = "b"
        coordenadaX = (input("Escribe una cordenada X para la bandera: ")) 
        coordenadaY = (input("Escribe una cordenada Y para la bandera: "))  #Este if sirve para ver que 
        if comprovarCoordenadas(int(coordenadaX),int(coordenadaY)) == True: #las coordenadas sean correctas
            coordenadaXY = [True, int((int(coordenadaX)-1)+((int(coordenadaY)-1)*anchura))]
            return coordenadaXY #Esta variable contiene un booleano para la bandera
        else:                   #y un entero para el numero de la casilla
            while comprovarCoordenadas(int(coordenadaX),int(coordenadaY)) != True:
                print("Valores introducidos incorrectos")
                coordenadaXY = [False, int((int(coordenadaX)-1)+((int(coordenadaY)-1)*anchura))]
                coordenadaXY = pedirCoordenada()
                return coordenadaXY#Si las coordenadas no son correctas se vuelve a llamar al procedimiento
    else:
        coordenadaY = (input("Escribe una cordenada Y: ")) #Lo mismo de arriba pero sin bandera
        if comprovarCoordenadas(int(coordenadaX),int(coordenadaY)) == True:
            coordenadaXY = [False, int((int(coordenadaX)-1)+((int(coordenadaY)-1)*anchura))]
            return coordenadaXY
        else:
            while comprovarCoordenadas(int(coordenadaX),int(coordenadaY)) != True:
                print("Valores introducidos incorrectos")
                coordenadaXY = [False, int((int(coordenadaX)-1)+((int(coordenadaY)-1)*anchura))]
                coordenadaXY = pedirCoordenada()
                return coordenadaXY

            
def comprovarCoordenadas(x,y): #la funcion recibe coordenadaX y coordenadaY desde pedirCoordenadas()
    if x > 0 and x <= anchura and y > 0 and y <= altura: 
        return True #si las coordenadas estan dentro del tablero la funion = True
    else:
        return False
            
            
def actualizarTablero(): #Muchos prints para hacer una meta-interfaz mas entretenida
    print(separador)
    print(" "*9, sep="", end="")
    for j in range(anchura): #aqui se escriben las coordenadas horizontales
        if j < 9:
            print((j+1), sep="", end="   ")
        elif j < 99:
            print((j+1), sep="", end="  ")
        elif j < 999:
            print((j+1), sep="", end=" ")
    print("\n")
    print(" "*7, "-"*((anchura*4)+1), sep="")
    print("1", " "*5, end="")
    for i in coordenadas:
        if (coordenadas.index(i)) != 0:
            if (coordenadas.index(i))%anchura == 0: #aqui las verticales
                print("|")
                print(" "*7, "|", "-"*((anchura*4)-1), "|", sep="")
                print((int(coordenadas.index(i)/anchura)+1), " "*(6 - (len(str(int(coordenadas.index(i)/anchura)+1)))), end="")
        if i[-2] == 0:
            print("\033[1;37;40m|", "\033[0;32;40m?", end="\033[1;37;40m ") 
        if i[-2] == 1: #estos codigos son para los colores
            if i[-1] > 0 and i[-1] < 9: #si la coordenada contiene un numero
                print("\033[1;37;40m|", "\033[0;34;40m ", i[-1], end="\033[1;37;40m ", sep="")
            if i[-1] == 0: #si la coordenada contiene un vacio
                print("|", " ", end=" ")
            if i[-1] == -1: #si la coordenada contiene una bomba
                print("\033[1;37;40m|", "\033[0;31;40m ", chr(164), end="\033[1;37;40m ", sep="")
        if i[-2] == -1: #si la coordenda tiene una bandera --- los chr(x) son los simbolos utilizados para las bombas y banderas
            print("\033[1;37;40m|", "\033[0;31;40m ", chr(182), end="\033[1;37;40m ", sep="")
    print("|")
    print(" "*7, "-"*((anchura*4)+1), sep="")


def ponerBombas(): #este procedimiento se encarga de repartir las bombas y establecer los numeros
    posiblesBombas=list(range(len(coordenadas))) #se establecen todas las casillas como posibles bombas
    posiblesBombas.pop(pedirCoordenadaNumero) #deja de ser posible que haya una bomba en la primera casilla elegida
    posiblesBombas = random.sample(posiblesBombas,(int((anchura*altura)//INDICEDEBOMBAS))) #se ponen aleatoriamente las bombas en posibles bombas
    for k in posiblesBombas:
        coordenadas[k][-1] = -1 #se introduce la bomba en la lista principal
        if k >= anchura: #se establecen los numeros al rededor de cada bombas
            if coordenadas[k-anchura][-1] != -1:
                coordenadas[k-anchura][-1] = coordenadas[k-anchura][-1] + 1
                if (k % anchura) != 0:
                    if coordenadas[k-anchura-1][-1] != -1:
                        coordenadas[k-anchura-1][-1] = coordenadas[k-anchura-1][-1] + 1
                if ((k+1) % anchura) != 0:
                    if coordenadas[k-anchura+1][-1] != -1:
                        coordenadas[k-anchura+1][-1] = coordenadas[k-anchura+1][-1] + 1
        if k < anchura*(altura-1):
            if coordenadas[k+anchura][-1] != -1:
                coordenadas[k+anchura][-1] = coordenadas[k+anchura][-1] + 1
            if (k % anchura) != 0:
                if coordenadas[k+anchura-1][-1] != -1:
                    coordenadas[k+anchura-1][-1] = coordenadas[k+anchura-1][-1] + 1
            if ((k+1) % anchura) != 0:
                if coordenadas[k+anchura+1][-1] != -1:
                    coordenadas[k+anchura+1][-1] = coordenadas[k+anchura+1][-1] + 1
        if (k % anchura) != 0:
            if coordenadas[k-1][-1] != -1:
                coordenadas[k-1][-1] = coordenadas[k-1][-1] + 1
        if ((k+1) % anchura) != 0:
            if coordenadas[k+1][-1] != -1:
                coordenadas[k+1][-1] = coordenadas[k+1][-1] + 1
                
                
def descubrirVacios(vacio): #se descubren todas las casillas contiguas
    if vacio >= anchura:
        if coordenadas[vacio-anchura][-2] == 0:
            coordenadas[vacio-anchura][-2] = 1
            if coordenadas[vacio-anchura][-1] == 0:
                descubrirVacios(vacio-anchura) #si la casilla contigua es un vacio, 
        if (vacio % anchura) != 0:             #la funcion se vuelve a llamar
            if coordenadas[vacio-anchura-1][-2] == 0:
                coordenadas[vacio-anchura-1][-2] = 1
                if coordenadas[vacio-anchura-1][-1] == 0:
                    descubrirVacios(vacio-anchura-1)
        if ((vacio+1) % anchura) != 0:
            if coordenadas[vacio-anchura+1][-2] == 0:
                coordenadas[vacio-anchura+1][-2] = 1
                if coordenadas[vacio-anchura+1][-1] == 0:
                    descubrirVacios(vacio-anchura+1)
    if vacio < anchura*(altura-1):
        if coordenadas[vacio+anchura][-2] == 0:
            coordenadas[vacio+anchura][-2] = 1
            if coordenadas[vacio+anchura][-1] == 0:
                descubrirVacios(vacio+anchura)
        if (vacio % anchura) != 0:
            if coordenadas[vacio+anchura-1][-2] == 0:
                coordenadas[vacio+anchura-1][-2] = 1
                if coordenadas[vacio+anchura-1][-1] == 0:
                        descubrirVacios(vacio+anchura-1)
        if ((vacio+1) % anchura) != 0:
            if coordenadas[vacio+anchura+1][-2] == 0:
                coordenadas[vacio+anchura+1][-2] = 1
                if coordenadas[vacio+anchura+1][-1] == 0:
                    descubrirVacios(vacio+anchura+1)
    if (vacio % anchura) != 0:
        if coordenadas[vacio-1][-2] == 0:
            coordenadas[vacio-1][-2] = 1
            if coordenadas[vacio-1][-1] == 0:
                descubrirVacios(vacio-1)
    if ((vacio+1) % anchura) != 0:
        if coordenadas[vacio+1][-2] == 0:
            coordenadas[vacio+1][-2] = 1
            if coordenadas[vacio+1][-1] == 0:
                descubrirVacios(vacio+1)
    return coordenadas #devuelve la lista acutualizada con los vacios abiertos


def verificarVictoria(): #se verifica si quedan casilla sin bomba por descubrir
    victoria = "Sin especificar"
    contador = 0
    while victoria != False and contador != len(coordenadas): 
        if coordenadas[contador][-2] == 0 and coordenadas[contador][-1] != -1:
            victoria = False #mientras victoria != False el bucle busca casilla
        else:                #por casilla alguna casilla que no este descubierta
            victoria = True  #y no contenga una bomba. Si no lo encuentra se gana la partida
        contador = contador + 1
    return victoria #devuelve el valor de victoria (booleano)


def descubrirTablero(): #en caso de explotar una bomba el juego te muestra el resto
    for t in range(len(coordenadas)):
        if coordenadas[t][-2] == 0 and coordenadas[t][-1] == -1:
            coordenadas[t][-2] = 1 #abre las casillas donde hay bombas
        elif coordenadas[t][-2] == -1 and coordenadas[t][-1] != -1:
            coordenadas[t][-2] = 0 #quita las banderas donde no hay bombas
            
            
anchura = int(input("Anchura del tablero: ")) #selecciona anchura tablero (x)
altura = int(input("Altura del tablero: ")) #seleccionar altura tablero (y)
for x in range(anchura): #se crean las coordenadas
  for y in range(altura):
    coordenadas.append([x + 1, y + 1, 0, 0])
    # estructura de las listas anidadas:
    #(coordenadaX, coordenadaY, descubierto?, contenido)
    # descubierto? puede tomar los valores 0 (no descubierto), 1(descubierto) y -1(con bandera)
    # el contenido puede ser 0(vacio), 1, 2, 3, 4, 5, 6, 7, 8 o -1(bomba)
actualizarTablero() #se muestra el tablero
print("REGLAS:")
print("-Las coordenadas X son las horizontales y las Y las verticles.")
print("-No se puede colocar bandera en la primera jugada.")
print("-Para colocar una bandera escribe 'b' o 'bandera'.")
print("-Para quitar una bandera, coloca otra encima.")
print()
coordenadaActual = pedirCoordenada() #se pide la primera coordenada (esta no puede tener bomba)
pedirCoordenadaNumero = coordenadaActual[1] #se extrae el numero de la coordenada
pedirCoordenadaBandera = coordenadaActual[0] #se extrae si tiene bandera
if pedirCoordenadaBandera == False: #si no se ha colocado una bandera
    ponerBombas() #se reparten las bombas
    coordenadas[pedirCoordenadaNumero][-2] = 1 #se descubre la primera casilla
    if coordenadas[pedirCoordenadaNumero][-1] == 0: #si es un vacio sa descubren
        descubrirVacios(pedirCoordenadaNumero)      #las casillas contiguas
while finDeJuego == False: #mientras el juego no se haya acabado
    actualizarTablero() #se actualiza el tablero
    coordenadaActual = pedirCoordenada() #se pide coordenada
    pedirCoordenadaNumero = coordenadaActual[1]
    pedirCoordenadaBandera = coordenadaActual[0]
    if pedirCoordenadaBandera == True: #si se esta colocando una bandera
        if coordenadas[pedirCoordenadaNumero][-2] == -1: #si se coloca una bandera
            coordenadas[pedirCoordenadaNumero][-2] = 0   #en otra bandera, se quita
        elif coordenadas[pedirCoordenadaNumero][-2] == 0:
            coordenadas[pedirCoordenadaNumero][-2] = -1 #coloca la bandera
    elif pedirCoordenadaBandera == False: #si no se esta colocando una bandera
        coordenadas[pedirCoordenadaNumero][-2] = 1 #se descubre la casilla
        if coordenadas[pedirCoordenadaNumero][-1] == 0: #si es un vacio
            descubrirVacios(pedirCoordenadaNumero) #se abren las casillas contiguas
        elif coordenadas[pedirCoordenadaNumero][-1] == -1: #si es una bomba
            descubrirTablero() 
            actualizarTablero()
            print("\nHAS PERDIDO!") #has perdido
            finDeJuego=True #y fin de partida
        elif verificarVictoria() == True: #se verifica que se hayan abierto todas las casillas
            actualizarTablero()
            print("\nHAS GANADO!") 
            finDeJuego=True
