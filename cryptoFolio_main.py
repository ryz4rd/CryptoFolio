from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

class Product:
    # BASICO
    #db_name = 'database.db'
    def __init__(self, window):
        self.wind = window
        self.wind.title("Estado de cuenta criptomonedas")
        self.wind.geometry("850x900")
        self.customize = ttk.Style()
        
        # COMPRA O VENTA SELECCION
        def alertbox():
            self.toplevel = Toplevel()
            self.toplevel.geometry("290x90")
            self.toplevel.title("Compra o venta")
            self.buy = Button(self.toplevel, text="COMPRA", font="Arial 20")
            self.buy.grid(row=0, column=0, pady=15, padx=8) 
            self.sell = Button(self.toplevel, text="VENTA", font="Arial 20")
            self.sell.grid(row=0, column=1, pady=15, padx=8)

        # Crear un contenedor de caja
        box_cont = LabelFrame(self.wind, text = "Seleciona una criptomoneda: ", font = "Sans 12")
        box_cont.grid(row = 0, column = 0, columnspan = 3, pady = 15)

        # Cypto Input
        Label(box_cont, text = "Criptomoneda: ", font = "Sans 12").grid(row = 2, column = 0)
        self.name = (Entry(box_cont, font = "Monospace 13"))
        self.name.focus()
        self.name.grid(row = 2, column = 1)

        # Cantidad de criptomonedas 
        Label(box_cont, text = "Cantidad: ", font = "Sans 12").grid(row = 2, column = 2, padx=9)
        self.cuanty = (Entry(box_cont, font = "Monospace 13"))
        self.cuanty.grid(row = 2, column = 3)

        #Precio de criptomonedas
        Label(box_cont, text = "Precio: ", font = "Sans 12").grid(row = 3, column = 0, pady = 6)
        self.price = (Entry(box_cont, font = "Monospace 13"))
        self.price.grid(row = 3, column = 1)
        
        # Save Button
        ttk.Button(box_cont, text="GUARDAR DATOS", command=alertbox).grid(row=3, column=3, columnspan = 2, sticky = W + E)

        #Cuadro para visulizar las criptomonedas (CATIDAD, PRECIO, GANANCIA)
        self.tree = ttk.Treeview(height=35, columns=("#0", "#1", "#2"))
        self.tree.grid(row=5, column=0, padx=(25))
        self.tree.heading('#0', text= "Criptomoneda", anchor= CENTER)
        self.tree.heading('#1', text= "Cantidad", anchor= CENTER)
        self.tree.heading('#2', text= "Precio", anchor= CENTER)
        self.tree.heading('#3', text= "Ganancias", anchor= CENTER)


if __name__ == '__main__':
    window = Tk()
    appliccation = Product(window)
    window.mainloop()
