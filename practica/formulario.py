from tkinter import *
from tkinter import messagebox
import sqlite3

# --- INICIO  funciones de BBDD conectar y salir-------
def Conectar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARHCAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100)
            )
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("ATENCION", "la BBDD ya existe")

def Salir():
    valor = messagebox.askquestion("SALIR", "¿Desea salir de la aplicacion?")
    if valor == "yes":
        root.destroy()
# --- FIN  funciones de BBDD conectar y salir-------
# --- INICIO  funciones de BORRAR borrar campos-------
def BorrarCampos():
    miId.set("")
    miNombre.set("")
    miPassword.set("")
    miApellido.set("")
    miDireccion.set("")
    comentarioText.delete('1.0', END)
# --- FIN  funciones de BORRAR borrar campos-------

# --- INICIO  funcion insertar usuario-------
def Create():
    miConexion = sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()

    # miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '"+ 
    #     miNombre.get() +"','"+
    #     miPassword.get()+ "','"+
    #     miApellido.get()+"','"+
    #     miDireccion.get()+"','"+
    #     comentarioText.get("1.0", END)+"')")

    datos = miNombre.get(), miPassword.get(), miApellido.get(), miDireccion.get(), comentarioText.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))
    miConexion.commit()
    messagebox.showinfo("BBDD", "registro insertado con exito")
    miConexion.close()
    BorrarCampos()
# --- Fin  funcion insertar usuario-------

# --- INICIO  funcion leer usuario-------
def Read():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = '"+miId.get()+"'")
    miUsuario = miCursor.fetchall()
    BorrarCampos()
    for usuario in miUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPassword.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        comentarioText.insert('1.0', usuario[5])

    miConexion.commit()
    miConexion.close()
# --- Fin  funcion leer usuario-------

# --- INICIO  funcion editar usuario-------
def Update():
    miConexion = sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()
    datos = miNombre.get(), miPassword.get(), miApellido.get(), miDireccion.get(), comentarioText.get("1.0", END)
    # miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = '"+
    #     miNombre.get()+"', PASSWORD = '"+
    #     miPassword.get()+"', APELLIDO = '"+
    #     miApellido.get()+"', DIRECCION = '"+
    #     miDireccion.get()+"', COMENTARIOS = '"+
    #     comentarioText.get("1.0", END)+"' WHERE ID = '"+ miId.get()+"'")
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = ?, PASSWORD = ?, APELLIDO = ?, DIRECCION = ?, COMENTARIOS = ? WHERE ID = '"+ miId.get()+"'", (datos))
    miConexion.commit()
    messagebox.showinfo("BBDD", "registro editado con exito")
    miConexion.close()
    BorrarCampos()
# --- Fin  funcion editar usuario-------

# --- INICIO  funcion eliminar usuario-------
def Delete():
    miConexion = sqlite3.connect("Usuarios")
    miCursor= miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID = '"+miId.get()+"'")
    miConexion.commit()
    messagebox.showinfo("BBDD", "registro eliminado con exito")
    miConexion.close()
    BorrarCampos()
# --- Fin  funcion eliminar usuario-------

root = Tk()
# -------------inicio barra Menu -----------------------------
barraMenu = Menu(root)
root.config(menu = barraMenu,  width = "300", height = "300")

BBDDMenu = Menu(barraMenu, tearoff = 0)
BBDDMenu.add_command(label = "Conectar", command = Conectar)
BBDDMenu.add_command(label = "Salir", command = Salir)

Borrar = Menu(barraMenu, tearoff = 0)
Borrar.add_command(label = "Borrar campos", command = BorrarCampos)

CRUD = Menu(barraMenu, tearoff = 0)
CRUD.add_command(label = "Crear", command= Create) 
CRUD.add_command(label = "Leer", command= Read) 
CRUD.add_command(label = "Actualizar", command = Update) 
CRUD.add_command(label = "Borrar", command = Delete) 

Ayuda = Menu(barraMenu, tearoff = 0)
Ayuda.add_command(label = "Licencia")
Ayuda.add_command(label = "Acerca de ...")

barraMenu.add_cascade(label = "BBDDMenu", menu = BBDDMenu)
barraMenu.add_cascade(label = "Borrar", menu = Borrar)
barraMenu.add_cascade(label = "CRUD", menu = CRUD)
barraMenu.add_cascade(label = "Ayuda", menu = Ayuda)
# -----------fin barra menu ---------------------------------
#--------------inicio formulario ---------------------------
miFrame = Frame(root)
miFrame.pack()

#------definicion de variables del formulario--------
miId = StringVar()
miNombre = StringVar()
miPassword = StringVar()
miApellido = StringVar()
miDireccion = StringVar()



#------------ inicio  id label and entry -----------------------
idLabel = Label(miFrame, text = "ID: ")
idLabel.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10, columnspan = 2)

idCuadro = Entry(miFrame, textvariable = miId)
idCuadro.grid(row = 0, column = 2, padx = 10, pady = 10,  columnspan = 2)
#------------ fin  id label and entry --------------------------
#------------ inicio  nombre label and entry -------------------
nombreLabel = Label(miFrame, text = "Nombre: ")
nombreLabel.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10, columnspan = 2)

nombreCuadro = Entry(miFrame, textvariable = miNombre)
nombreCuadro.grid(row = 1, column = 2, padx = 10, pady = 10,  columnspan = 2)
nombreCuadro.config(fg = "red", justify = "right")
#------------ fin nombre label and entry -----------------------
#------------ inicio  passwrord label and entry -------------------
passwrordLabel = Label(miFrame, text = "Password: ")
passwrordLabel.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10, columnspan = 2)

passwrordCuadro = Entry(miFrame, textvariable = miPassword)
passwrordCuadro.grid(row = 2, column = 2, padx = 10, pady = 10,  columnspan = 2)
passwrordCuadro.config(show = "*")
#------------ fin passwrord label and entry -----------------------
#------------ inicio  apellido label and entry -------------------
apellidoLabel = Label(miFrame, text = "Apellido: ")
apellidoLabel.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10, columnspan = 2)

apellidoCuadro = Entry(miFrame, textvariable = miApellido)
apellidoCuadro.grid(row = 3, column = 2, padx = 10, pady = 10,  columnspan = 2)
#------------ fin apellido label and entry -----------------------
#------------ inicio  direccion label and entry -------------------
direccionLabel = Label(miFrame, text = "Direccion: ")
direccionLabel.grid(row = 4, column = 0, sticky = "e", padx = 10, pady = 10, columnspan = 2)

direccionCuadro = Entry(miFrame, textvariable = miDireccion)
direccionCuadro.grid(row = 4, column = 2, padx = 10, pady = 10,  columnspan = 2)
#------------ fin direccion label and entry -----------------------
#------------ inicio  comentarios label and entry -------------------
comentarioLabel = Label(miFrame, text = "Comentarios: ")
comentarioLabel.grid(row = 5, column = 0, sticky = "e", padx = 10, pady = 10, columnspan = 2) 

comentarioText = Text(miFrame, width = 13, height = 5)
comentarioText.grid(row = 5, column = 2, sticky = "e", padx = 10, pady = 10)

scrollVert = Scrollbar(miFrame, command = comentarioText.yview)
scrollVert.grid(row = 5, column = 3, sticky = "nsew")
comentarioText.config(yscrollcommand = scrollVert.set)
#------------ fin comentarios label and entry -----------------------

#------------ inicio  botones -------------------}
miFrameBotones = Frame(root)
miFrameBotones.pack()
botonCreate = Button(miFrameBotones, text = "Create", command= Create)
botonCreate.grid(row = 6, column = 0, sticky = "e", padx = 10, pady = 10)
# botonCreate.pack()

botonRead = Button(miFrameBotones, text = "Read", command= Read)
botonRead.grid(row = 6, column = 1, sticky = "e", padx = 10, pady = 10)
# botonRead.pack()

botonUpdate = Button(miFrameBotones, text = "Update", command = Update)
botonUpdate.grid(row = 6, column = 2, sticky = "e", padx = 10, pady = 10)
# botonUpdate.pack()

botonDelete = Button(miFrameBotones, text = "Delete", command = Delete)
botonDelete.grid(row = 6, column = 3, sticky = "e", padx = 10, pady = 10)
# botonDelete.pack()
#------------ fin  botones -------------------


root.mainloop()
