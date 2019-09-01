from tkinter import *

root = Tk()
miFrame = Frame(root, width = 1200, height = 600)
miFrame.pack()
minombre = StringVar()
#el metodo grid divide el frame en casillas pequeños cuadros
# padx y pady es el padding
#sticky es para situar el widget e,w,n,s

nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10) 

cuadroNombre = Entry(miFrame, textvariable = minombre)
cuadroNombre.grid(row = 0, column = 1 , padx = 10, pady = 10)
cuadroNombre.config(fg = "red", justify = "right")

apellidoLabel = Label(miFrame, text = "Apellido: ")
apellidoLabel.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10) 

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row = 1, column = 1 , padx = 10, pady = 10)

direccionlabel = Label(miFrame, text = "Direccion: ")
direccionlabel.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10) 

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row = 2, column = 1 , padx = 10, pady = 10)

passLabel = Label(miFrame, text = "Password: ")
passLabel.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10) 

cuadroPass = Entry(miFrame)
cuadroPass.grid(row = 3, column = 1 , padx = 10, pady = 10)
cuadroPass.config(show = "*")

comentarioLabel = Label(miFrame, text = "Comentarios: ")
comentarioLabel.grid(row = 4, column = 0, sticky = "e", padx = 10, pady = 10) 

textComentario = Text(miFrame, width = 30, height = 10)
textComentario.grid(row = 4, column = 1 , padx = 10, pady = 10)

scrollVert = Scrollbar(miFrame, command = textComentario.yview)
scrollVert.grid(row= 4, column = 2, sticky = "nsew") # el scroll se posicion a al alatura del Text
textComentario.config(yscrollcommand=scrollVert.set)  # el scroll se posicion al altura del cursor

def codigoBoton():
    minombre.set("Ciro")

botonEnvio = Button(root, text = "Enviar", command = codigoBoton)
botonEnvio.pack()

root.mainloop()