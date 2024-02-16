import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st 
import conexion

class juego:

    def __init__(self):
        self.juego = conexion.Datos()
        self.ventana = tk.Tk()
        self.ventana.geometry("600x800")
        self.ventana.title("Ta Te Ti")
        self.paginas = ttk.Notebook(self.ventana)
        self.paginas.grid(column = 0, row = 0, padx = 10, pady=10)
        self.tablero =[]
        self.listaBotones=[]
        self.turno = 0
        self.iniciar()
        self.Reglas()
        
        self.ventana.mainloop()
    
    def iniciar(self):

        self.pagina1 = ttk.Frame(self.paginas)
        self.paginas.add(self.pagina1, text= "Registrar equipo")

        self.titulo = ttk.Label(self.pagina1, text = "Ta Te Ti", font = ("Comic Sans MS", 25))
        self.titulo.grid(columnspan = 2, row=1, padx= 100, pady= 4)

        self.imagen = tk.PhotoImage(file = ("tres-en-raya.png"))
        self.image = ttk.Label(self.pagina1, image= self.imagen)
        self.image.grid(columnspan =2, row =2)

        self.contenedor1 = ttk.LabelFrame(self.pagina1, text = "Registro")
        self.contenedor1.grid(column = 0, row =3, padx =4, pady= 10)

        self.eti1 =ttk.Label(self.contenedor1, text = "Nombre jugador #1: ")
        self.eti1.grid(column =0, row=3, padx=4, pady=4 )
        self.jugador1 = tk.StringVar()
        self.entryjugador1 = ttk.Entry(self.contenedor1, textvariable= self.jugador1)
        self.entryjugador1.grid(column =1, row=3, padx= 4, pady=4)

        self.eti2 =ttk.Label(self.contenedor1, text = "Nombre jugador #2: ")
        self.eti2.grid(column =0, row=4, padx=4, pady=4 )
        self.jugador2 = tk.StringVar()
        self.entryjugador2 = ttk.Entry(self.contenedor1, textvariable= self.jugador2)
        self.entryjugador2.grid(column =1, row=4, padx= 4, pady=4)

        self.botonregistro = ttk.Button(self.contenedor1, text = "registrar" , command = self.Registrar)
        self.botonregistro.grid(columnspan=2, row=5, padx=4, pady=4)

    def Registrar(self):
        user1 = (self.jugador1.get(), 1)
        self.juego.gamerone(user1)

        user2 = (self.jugador2.get(), 2)
        self.juego.gamertwo(user2)

        mb.showinfo("Informacion", "Los jugadores fueron registrados con exito")
        self.contenedor1.destroy()
        self.botonjugar = ttk.Button(self.pagina1, text="Comenzar", command= self.juegotablero)
        self.botonjugar.grid(columnspan=2, row=3, padx=4, pady=4)

    def juegotablero(self):

        self.pagina1.destroy()

        gamers = (self.jugador1.get(), self.jugador2.get())
        self.juego.Partida(gamers)

        self.pagina2 = tk.Toplevel()
        self.pagina2.geometry("600x800")
        self.pagina2.title("Ta Te Ti")
        self.pagina2.config(background= "#66B2FF")

        for i in range (0,9):
            self.tablero.append("N")

        self.boton0 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (0,))
        self.listaBotones.append(self.boton0)
        self.boton0.place(x=60 , y=50)

        self.boton1 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (1,))
        self.listaBotones.append(self.boton1)
        self.boton1.place(x=160 , y=50)

        self.boton2 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (2,))
        self.listaBotones.append(self.boton2)
        self.boton2.place(x=260 , y=50)

        self.boton3 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (3,))
        self.listaBotones.append(self.boton3)
        self.boton3.place(x=60 , y=150)

        self.boton4 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (4,))
        self.listaBotones.append(self.boton4)
        self.boton4.place(x=160 , y=150)

        self.boton5 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (5,))
        self.listaBotones.append(self.boton5)
        self.boton5.place(x=260 , y=150)

        self.boton6 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (6,))
        self.listaBotones.append(self.boton6)
        self.boton6.place(x=60 , y=250)

        self.boton7 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (7,))
        self.listaBotones.append(self.boton7)
        self.boton7.place(x=160 , y=250)

        self.boton8 = ttk.Button(self.pagina2, command = lambda: self.Cambiar (8,))
        self.listaBotones.append(self.boton8)
        self.boton8.place(x=260 , y=250)

        self.botonjugar = ttk.Button(self.pagina2, text = "volver" , command = self.Iniciargame2)
        self.botonjugar.place(x=260, y=350)

        for i in range (0,9):
            self.listaBotones[i].config(state="Normal")
            self.listaBotones[i].config(text="")
            self.tablero[i]="N" 
        
    def Iniciargame2(self):
        self.pagina2.destroy()
        self.pagina3.destroy()
        self.Iniciargame()

    def cambiar(self , num):
        if self.tablero[num] == "N" and self.turno ==0:
            self.listaBotones[num].config(text = "X")
            self.tablero[num] = "X"
            self.turno = 1

            self.eti3 = ttk.Label(self.pagina2, text = "Turno de: " + str(self.jugador1.get()), font = ("Comic Sans MS", 15))
            self.eti3.place(x=60, y=350)
            self.eti3.config(background="#66B2FF")
            self.validar()

        elif self.tablero[num] =="N" and self.turno == 1:
            self.listaBotones[num].config(text = "O")
            self.tablero[num] = "O"
            self.turno = 0

            self.eti3 = ttk.Label(self.pagina2, text = "Turno de: " + str(self.jugador2.get()), font = ("Comic Sans MS", 15))
            self.eti3.place(x=60, y=350)
            self.eti3.config(background="#66B2FF")
            self.validar()
         
        self.listaBotones[num].config(state = "disable")

    def validar(self):

        if(self.tablero[0] == "X" and self.tablero[1] == "X" and self.tablero[2] == "X" or self.tablero[3] == "X" and self.tablero[4] == "X" and self.tablero[5] == "X" or self.tablero[6] == "X" and self.tablero[7] == "X" and self.tablero[8] == "X"):
            mb.showinfo("ganador", "Ganador Jugador" + str(self.jugador1.get()))
            self.jugarotra()

        elif(self.tablero[0] == "X" and self.tablero[3] == "X" and self.tablero[6] == "X" or self.tablero[1] == "X" and self.tablero[4] == "X" and self.tablero[7] == "X" or self.tablero[2] == "X" and self.tablero[3] == "X" and self.tablero[8] == "X"):
            mb.showinfo("ganador", "Ganador Jugador" + str(self.jugador1.get()))
            self.jugarotra()

        elif(self.tablero[0] == "X" and self.tablero[4] == "X" and self.tablero[8] == "X" or self.tablero[6] == "X" and self.tablero[4] == "X" and self.tablero[2] == "X"):
            mb.showinfo("ganador", "Ganador Jugador" + str(self.jugador1.get()))
            self.jugarotra()

        elif(self.tablero[0] == "O" and self.tablero[1] == "O" and self.tablero[2] == "O" or self.tablero[3] == "O" and self.tablero[4] == "O" and self.tablero[5] == "O" or self.tablero[6] == "O" and self.tablero[7] == "O" and self.tablero[8] == "O"):
            mb.showinfo("ganador", "Ganador Jugador" + str(self.jugador2.get()))
            self.jugarotra()

        elif(self.tablero[0] == "O" and self.tablero[3] == "O" and self.tablero[6] == "O" or self.tablero[1] == "O" and self.tablero[4] == "O" and self.tablero[7] == "O" or self.tablero[2] == "O" and self.tablero[3] == "O" and self.tablero[8] == "O"):
            mb.showinfo("ganador", "Ganador Jugador" + str(self.jugador2.get()))
            self.jugarotra()

        elif(self.tablero[0] == "O" and self.tablero[4] == "O" and self.tablero[8] == "O" or self.tablero[6] == "O" and self.tablero[4] == "O" and self.tablero[2] == "O"):
            mb.showinfo("ganador", "Ganador Jugador" + str(self.jugador2.get()))
            self.jugarotra()

    def jugarotra(self):
        self.pagina2.destroy()

        self.pagina3 = tk.Toplevel()
        self.pagina3.geometry("310x310")
        self.pagina3.title("Final")

        self.imagen = tk.PhotoImage(file = "game-over-typography-free-png.png")
        self.image = ttk.Label(self.pagina3, image= self.imagen)
        self.image.grid(columnspan = 2, row = 2)

        self.botonvolver = ttk.Button(self.pagina3, text = "Volver", command = self.Iniciargame2)
        self.botonvolver.grid(column = 0, row = 3)

        self.botonjugar = ttk.Button(self.pagina3, text = "Jugar" , command = self.tablero2)
        self.botonjugar.grid(column = 1, row = 3)

    
    def tablero2(self):
        self.pagina3.destroy()
        self.juegotablero()
    
    def Reglas(self):
        self.pagina4 = ttk.Frame(self.paginas)
        self.paginas.add(self.pagina4, text = "Reglas del juego")

        self.contenedor2 = ttk.LabelFrame(self.pagina4, text ="Reglas")
        self.contenedor2.grid(column=0, row = 0, padx=5, pady = 10)

        self.espacio = st.ScrolledText(self.contenedor2, width = 40, height = 10)
        self.espacio.grid(column = 0, row = 2, padx = 10, pady = 10 )
        listado = self.juego.BuscarReglas()
        self.espacio.delete ("1. 0", tk.END)

        for row in listado:
            self.espacio.insert(tk.END, row[0] + "\nDescripcion: \n" +row[1] + "")
    
JuegoUno = juego()