from tkinter import *
raiz = Tk()
raiz.title("Ventana de pruebas")
# raiz.resizable(0,0) # para no redimencionar le ancho y alto del cuadro 1 = True, 0 = False
# raiz.iconbitmap("imagen.ico") # para poner icono
# raiz.geometry("650x350") # ancho y alto del cuadro
raiz.config(bg ="blue") #agregar background
raiz.config(bd = 45) # grozor de borde
raiz.config(relief = "groove") # tipo de borde
raiz.config(cursor = "hand2") # diseño en el cursor
miFrame = Frame() # frame base para los widgets(boton, label, cajas de texto)
miFrame.pack(fill = "both", expand = "True") #empaquetar el frame dentro de la raiz
miFrame.config(width = "650", height= "350") 
miFrame.config(bg ="red")
miFrame.config(bd = 35) # grozor de borde
miFrame.config(relief = "sunken") # tipo de borde
miFrame.config(cursor = "pirate") # diseño en el cursor
raiz.mainloop()