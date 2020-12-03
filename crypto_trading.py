from tkinter import ttk
from tkinter import *
import sqlite3

class Product:
    # BASICO
    #db_name = 'database.db'
    def __init__(self, window):
        self.wind = window
        self.wind.title("Estado de cuenta criptomonedas")
        self.wind.geometry("750x800")

        # Crear un contenedor de caja
        box_cont = LabelFrame(self.wind, text = "Seleciona una criptomoneda: ", font = "Sans 12")
        box_cont.grid(row = 0, column = 0, columnspan = 3, pady = 15)

        # Cypto Input
        Label(box_cont, text = "Criptomoneda: ", font = "Sans 12").grid(row = 2, column = 0)
        self.name = (Entry(box_cont, font = "Monospace 13"))
        self.name.focus()
        self.name.grid(row = 2, column = 1)

        # Cantidad de criptomonedas 
        Label(box_cont, text = "Cantidad: ", font = "Sans 12").grid(row = 2, column = 2, padx=(9))
        self.cuanty = (Entry(box_cont, font = "Monospace 13"))
        self.cuanty.grid(row = 2, column = 3)

        #Precio de criptomonedas
        Label(box_cont, text = "Precio: ", font = "Sans 12").grid(row = 3, column = 0, pady = 6)
        self.price = (Entry(box_cont, font = "Monospace 13"))
        self.price.grid(row = 3, column = 1)
        
        # Save Button
        ttk.Button(box_cont, text="GUARDAR DATOS").grid(row=3, column=3, columnspan = 2, sticky = W + E)

if __name__ == '__main__':
    window = Tk()
    appliccation = Product(window)
    window.mainloop()
