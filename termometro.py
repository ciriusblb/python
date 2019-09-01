import serial
import tkinter
import time
from time import sleep
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

progreso = 0
maximo = 100
valores = 0

def progress(val):
    global progreso 
    progreso = val
    # if action == "subir":
    #     progreso += val
    #     if progreso >= maximo:
    #         progreso = 100
    # else:
    #     progreso -= val
    #     if progreso <= 0:
    #         progreso = 0
    pgbar['value'] = progreso

root = tkinter.Tk()
root.title("Termometro v1.0")
root.geometry("300x300")
barraMenu = Menu(root)
root.config(menu = barraMenu)
miFrame = Frame(root)
miFrame.pack()

def infoAdicional():
    messagebox.showinfo("Termometro de Ciro", "Medidor de temperatura de 2019")
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")
def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
    if valor == "yes":
        root.destroy()
def stop():
    pgbar['value'] = 0
    arduino.close()
def start():
    arduino.open()
def update():
    global valores
    while 1:
        line = int(arduino.readline())
        print(line)
        # if line > valores:
            # progress(line, "subir")
        progress(line)
        # else:
            # progress(line, "bajar")
        # valores = line
        root.update()
        sleep(1)




archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Nuevo", command = start)
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_command(label = "Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Cerrar", command = stop)
archivoMenu.add_command(label = "Salir", command = salirAplicacion)


archivoEdicion = Menu(barraMenu, tearoff =0 )
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")

archivoHerramientas = Menu(barraMenu, tearoff =0)
archivoAyuda = Menu(barraMenu, tearoff =0)
archivoAyuda.add_command(label = "Licencia", command = avisoLicencia)
archivoAyuda.add_command(label = "Información", command = infoAdicional)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Edicion", menu = archivoEdicion)
barraMenu.add_cascade(label = "Herramientas", menu = archivoHerramientas)
barraMenu.add_cascade(label = "Ayuda", menu = archivoAyuda)


for i in range(10):
    Label(miFrame, text =str(100 - (i+1)*10) +"-" ).grid(row = i, column = 0, padx = 1, pady = 1)

pgbar = Progressbar(
    miFrame,
    length = 200,
    orient = VERTICAL,
    maximum = maximo,
    value = progreso,
    mode='determinate'
)
pgbar.grid(row = 0, column = 1, rowspan = 10)
# pgbar.pack()


# btnSubir = Button(
#     miFrame,
#     text = "Detener App",
#     command = lambda:stop()
# )
# btnSubir.pack()
# btnBajar = Button(
#     miFrame,
#     text = "Bajar",
#     command = lambda:progress(10, "bajar")
# )
# btnBajar.pack()

root.after(1,update) 
root.mainloop()
