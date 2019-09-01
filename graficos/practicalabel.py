from tkinter import *

root = Tk()
miFrame = Frame(root, width = 500, height = 400)
miFrame.pack()

# miImagen = PhotoImage(file = "mouse.gif") #colocar una imagen de tipo png y gif en label
# Label(miFrame, image = miImagen).place(x = 100, y =200)

miLabel = Label(miFrame, text = "Hola alumnos de python", fg = "red", font = ("Comic Sans MS", 18))
miLabel.place(x=100, y = 200) # para ubicar el label por coordenadaas xy
root.mainloop()