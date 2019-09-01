from tkinter import *

root = Tk()

playa = IntVar()
montania = IntVar()
turismoRural = IntVar()

def opcionesViaje():
    opcionesElegidas = ""
    if playa.get() == 1:
        opcionesElegidas+= " Playa"
    if montania.get() == 1:
        opcionesElegidas+= " Montaña"
    if turismoRural.get() == 1:
        opcionesElegidas+= " Turismo rural"

    textoFinal.config(text = opcionesElegidas)


frame = Frame(root)
frame.pack()

Label(frame, text = "Elije destinos", width = 50).pack()

Checkbutton(frame, text = "Playa", variable = playa, onvalue = 1, offvalue = 0, command=opcionesViaje).pack()
Checkbutton(frame, text = "Montaña", variable = montania, onvalue = 1, offvalue = 0, command=opcionesViaje).pack()
Checkbutton(frame, text = "Turismo rural", variable = turismoRural, onvalue = 1, offvalue = 0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
