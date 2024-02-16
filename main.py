from collections import deque 

turno = deque(["0", "X"])
tablero = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "],
]

def rotar():
    turno.rotate()
    return turno[0]
    

def mostrar():
    print(" ")
    for fila in tablero:
        print(fila)

def procesar(posicion):
    fila, columna = posicion.split (",") 
    return [int (fila)-1, int (columna)-1]

def posicion_correcta(posicion):
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= 2:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False

def actualizar(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador 

def winner(j):
    if tablero[0] == [j, j, j,] or tablero [1] == [j, j, j,] or tablero [2] == [j, j, j,]:
        return True
    elif tablero[0][0]==j and tablero [1][0] ==j and tablero[2][0]==j:
        return True
    elif tablero[0][1]==j and tablero [1][1] ==j and tablero[2][1]==j:
        return True
    elif tablero[0][2]==j and tablero [1][2] ==j and tablero[2][2]==j:
        return True
    elif tablero[0][0]==j and tablero [1][1] ==j and tablero[2][2]==j:
        return True
    elif tablero[0][2]==j and tablero [1][1] ==j and tablero[2][0]==j:
        return True
    return False

def completo():
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True

def juego():
    mostrar()
    jugador = rotar()
    while True:
        posicion= input("Jugador {}. Elige una posicion fila, columna de 1 a 3(Ejemplo 1, 3): ".format(jugador))
        if posicion == 'salir':
            break 
        try:
            posicion_l = procesar(posicion)
        except: 
            print ("Error, posicion {} no es valida. Elige una posicion fila, columna de 1 a 3(Ejemplo 1, 3): ".format(posicion))
            continue
        if posicion_correcta(posicion_l):
            print("correcto")
            actualizar(posicion_l, jugador)
            mostrar()
            if winner(jugador):
                print ("Jugador de {} gano :D".format(jugador))
                break
            elif completo():
                print ("Empate")
                break
            jugador = rotar() 
        
        else:
            print("Posicion {} es incorrecta".format(posicion))

juego()

