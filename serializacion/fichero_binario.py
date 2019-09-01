import pickle

# crear el archivo con informacion en binario----------
# lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]
# fichero_binario = open("lista_nombres", "wb")
# pickle.dump(lista_nombres, fichero_binario)
# fichero_binario.close()

# leer un archivo con informacion en bianrio ---------
# fichero = open("lista_nombres", "rb")
# lista = pickle.load(fichero)
# print(lista)


#selializar objetos en binario en un fichero---------------

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    def arrancar(self):
        self.enmarcha = True
    def  acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)

coche1 = Vehiculos("Marca1", "Modelo1")
coche2 = Vehiculos("Marca2", "Modelo2")
coche3 = Vehiculos("Marca3", "Modelo3")
coches = [coche1, coche2, coche3]

fichero = open("loscoches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del (fichero) # para borrar el fichero del directorio

# rescatar y leer el fichero con los objetos en binario

ficheroApertura = open("loscoches", "rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()
for c in misCoches:
    print(c.estado())
