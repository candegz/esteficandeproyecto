import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st 
import tkinter as tk
from tkinter import messagebox

# class juego:

#     def __init__(self):
#         self.ventana = tk.Tk()
#         self.ventana.geometry("600x800")
#         self.ventana.title("Ta Te Ti")
#         self.paginas = ttk.Notebook(self.ventana)
#         self.paginas.grid(column = 0, row = 0, padx = 10, pady=10)
#         self.tablero =[]
#         self.listaBotones=[]
#         self.turno = 0
#         self.iniciar()
        
#         self.ventana.mainloop()
    
#     def iniciar(self):

#         self.pagina1 = ttk.Frame(self.paginas)
#         self.paginas.add(self.pagina1, text= "Registrar equipo")

#         self.titulo = ttk.Label(self.pagina1, text = "Ta Te Ti", font = ("Comic Sans MS", 25))
#         self.titulo.grid(columnspan = 2, row=1, padx= 100, pady= 4)

#         self.imagen = tk.PhotoImage(file = ("tres-en-raya.png"))
#         self.image = ttk.Label(self.pagina1, image= self.imagen)
#         self.image.grid(columnspan =2, row =2)

#         self.contenedor1 = ttk.LabelFrame(self.pagina1, text = "Registro")
#         self.contenedor1.grid(column = 0, row =3, padx =4, pady= 10)

#         self.eti1 =ttk.Label(self.contenedor1, text = "Nombre jugador #1: ")
#         self.eti1.grid(column =0, row=3, padx=4, pady=4 )
#         self.jugador1 = tk.StringVar()
#         self.entryjugador1 = ttk.Entry(self.contenedor1, textvariable= self.jugador1)
#         self.entryjugador1.grid(column =1, row=3, padx= 4, pady=4)

#         self.eti2 =ttk.Label(self.contenedor1, text = "Nombre jugador #2: ")
#         self.eti2.grid(column =0, row=4, padx=4, pady=4 )
#         self.jugador2 = tk.StringVar()
#         self.entryjugador2 = ttk.Entry(self.contenedor1, textvariable= self.jugador2)
#         self.entryjugador2.grid(column =1, row=4, padx= 4, pady=4)

#         self.botonregistro = ttk.Button(self.contenedor1, text = "registrar" , command = self.Registrar)
#         self.botonregistro.grid(columnspan=2, row=5, padx=4, pady=4)

#     def Registrar(self):
#         user1 = (self.jugador1.get(), 1)
#         self.juego.gamerone(user1)

#         user2 = (self.jugador2.get(), 2)
#         self.juego.gamertwo(user2)

#         mb.showinfo("Informacion", "Los jugadores fueron registrados con exito")
#         self.contenedor1.destroy()
#         self.botonjugar = ttk.Button(self.pagina1, text="Comenzar", command= self.juegotablero)
#         self.botonjugar.grid(columnspan=2, row=3, padx=4, pady=4)

   
# JuegoUno = juego()

# class TaTeTi:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Ta Te Ti")
#         self.jugador = "X"
#         self.tablero = [""] * 9
#         self.botones = []
#         self.crear_interfaz()

#     def crear_interfaz(self):
#         for i in range(9):
#             boton = tk.Button(self.root, text="", font=("Helvetica", 24), height=2, width=5, command=lambda i=i: self.hacer_movimiento(i))
#             boton.grid(row=i // 3, column=i % 3)
#             self.botones.append(boton)

#     def hacer_movimiento(self, indice):
#         if self.tablero[indice] == "" and not self.verificar_ganador():
#             self.tablero[indice] = self.jugador
#             self.botones[indice]["text"] = self.jugador
#             if self.verificar_ganador():
#                 messagebox.showinfo("Fin del juego", f"Ganador: Jugador {self.jugador}")
#             elif "" not in self.tablero:
#                 messagebox.showinfo("Fin del juego", "Empate")
#             else:
#                 self.jugador = "O" if self.jugador == "X" else "X"

#     def verificar_ganador(self):
#         combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
#         for a, b, c in combinaciones_ganadoras:
#             if self.tablero[a] == self.tablero[b] == self.tablero[c] != "":
#                 return True
#         return False

# def main():
#     root = tk.Tk()
#     Ta_Te_Ti= TaTeTi(root)
#     root.mainloop()

# if __name__ == '__main__':
#     main()

import tkinter as tk
from tkinter import ttk, messagebox

class Juego:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x800")
        self.ventana.title("Ta Te Ti")
        self.paginas = ttk.Notebook(self.ventana)
        self.paginas.grid(column=0, row=0, padx=10, pady=10)
        self.tablero = []
        self.listaBotones = []
        self.turno = 0
        self.user1 = None
        self.user2 = None
        self.ta_teti_actual = None
        self.iniciar()

        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventanas)  # Maneja el cierre de la ventana principal

        self.ventana.mainloop()

    def iniciar(self):
        self.pagina1 = ttk.Frame(self.paginas)
        self.paginas.add(self.pagina1, text="Registrar equipo")

        self.titulo = ttk.Label(self.pagina1, text="Ta Te Ti", font=("Comic Sans MS", 25))
        self.titulo.grid(columnspan=2, row=1, padx=100, pady=4)

        self.imagen = tk.PhotoImage(file=("tres-en-raya.png"))
        self.image = ttk.Label(self.pagina1, image=self.imagen)
        self.image.grid(columnspan=2, row=2)

        self.contenedor1 = ttk.LabelFrame(self.pagina1, text="Registro")
        self.contenedor1.grid(column=0, row=3, padx=4, pady=10)

        self.eti1 = ttk.Label(self.contenedor1, text="Nombre jugador #1: ")
        self.eti1.grid(column=0, row=3, padx=4, pady=4)
        self.jugador1 = tk.StringVar()
        self.entryjugador1 = ttk.Entry(self.contenedor1, textvariable=self.jugador1)
        self.entryjugador1.grid(column=1, row=3, padx=4, pady=4)

        self.eti2 = ttk.Label(self.contenedor1, text="Nombre jugador #2: ")
        self.eti2.grid(column=0, row=4, padx=4, pady=4)
        self.jugador2 = tk.StringVar()
        self.entryjugador2 = ttk.Entry(self.contenedor1, textvariable=self.jugador2)
        self.entryjugador2.grid(column=1, row=4, padx=4, pady=4)

        self.botonregistro = ttk.Button(self.contenedor1, text="registrar", command=self.Registrar)
        self.botonregistro.grid(columnspan=2, row=5, padx=4, pady=4)

    def Registrar(self):
        nombre1 = self.jugador1.get()
        nombre2 = self.jugador2.get()
        if nombre1.strip() == "" or nombre2.strip() == "":
            messagebox.showerror("Error", "Debe ingresar ambos nombres para jugar.")
            return

        self.user1 = (nombre1, 1)
        self.user2 = (nombre2, 2)

        self.paginas.forget(0)  # Oculta la página de registro
        self.juegotablero()

    def juegotablero(self):
        if self.ta_teti_actual:
            self.ta_teti_actual.root.destroy()  # Destruye la ventana anterior del juego si existe

        root = tk.Tk()
        self.ta_teti_actual = TaTeTi(root, self.user1, self.user2, self.mostrar_ventana_final)
        root.mainloop()

    def mostrar_ventana_final(self):
        self.ventana_final = VentanaFinal(self.ventana, self)

    def reiniciar_juego(self):
        self.ventana_final.root.destroy()
        self.ventana_final.root.quit()
        self.juegotablero()

    def cerrar_ventanas(self):
        if self.ta_teti_actual:
            self.ta_teti_actual.root.destroy()  # Destruye la ventana del juego si existe
        self.ventana.destroy()

class TaTeTi:
    def __init__(self, root, user1, user2, callback):
        self.root = root
        self.root.title("Ta Te Ti")
        self.jugador = "X"
        self.tablero = [""] * 9
        self.botones = []
        self.user1 = user1
        self.user2 = user2
        self.callback = callback
        self.crear_interfaz()

    def crear_interfaz(self):
        for i in range(9):
            boton = tk.Button(self.root, text="", font=("Helvetica", 24), height=2, width=5,
                              command=lambda i=i: self.hacer_movimiento(i))
            boton.grid(row=i // 3, column=i % 3)
            self.botones.append(boton)

    def hacer_movimiento(self, indice):
        if self.tablero[indice] == "" and not self.verificar_ganador():
            self.tablero[indice] = self.jugador
            self.botones[indice]["text"] = self.jugador
            if self.verificar_ganador():
                ganador = self.user1[0] if self.jugador == "X" else self.user2[0]
                messagebox.showinfo("Fin del juego", f"Ganador: {ganador}")
                self.callback()
            elif "" not in self.tablero:
                messagebox.showinfo("Fin del juego", "Empate")
                self.callback()
            else:
                self.jugador = "O" if self.jugador == "X" else "X"

    def verificar_ganador(self):
        combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in combinaciones_ganadoras:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != "":
                return True
        return False

class VentanaFinal:
    def __init__(self, root, juego):
        self.root = tk.Toplevel(root)
        self.root.title("Resultado Final")

        label = tk.Label(self.root, text="Seleccione una opción:")
        label.pack(pady=10)

        btn_nuevo_juego = tk.Button(self.root, text="Jugar de nuevo", command=juego.reiniciar_juego)
        btn_nuevo_juego.pack(pady=10)

        btn_registrar_nombres = tk.Button(self.root, text="Registrar nuevos nombres", command=juego.iniciar)
        btn_registrar_nombres.pack(pady=10)

        btn_cerrar_programa = tk.Button(self.root, text="Cerrar el programa", command=juego.cerrar_ventanas)
        btn_cerrar_programa.pack(pady=10)

def main():
    JuegoUno = Juego()

if __name__ == '__main__':
    main()

