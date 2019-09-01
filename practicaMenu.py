from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Ciro", "Procesador de textos de 2019")
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")
def salirAplicacion():
    # valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
    # if valor == "yes":
    #     root.destroy()

    valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicacion?")
    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento")

barraMenu = Menu(root)
root.config(menu = barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Guardar", command = cerrarDocumento)
archivoMenu.add_command(label = "Guardar como", command = salirAplicacion)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Cerrar", command = avisoLicencia)
archivoMenu.add_command(label = "Salir", command = infoAdicional)


archivoEdicion = Menu(barraMenu, tearoff =0 )
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")
archivoHerramientas = Menu(barraMenu)
archivoAyuda = Menu(barraMenu)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Edicion", menu = archivoEdicion)
barraMenu.add_cascade(label = "Herramientas", menu = archivoHerramientas)
barraMenu.add_cascade(label = "Ayuda", menu = archivoAyuda)

root.mainloop()
