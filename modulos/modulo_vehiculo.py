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
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargado"
        else:
            return "La furgoneta no esta cargado"

class Moto(Vehiculos): # herencia de clases
    haceCaballito = ""
    def caballito(self):
        self.haceCaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.haceCaballito)

class VElectricos(Vehiculos):
    def __init__(self, marca_vehiculo, marca_modelo):
        super().__init__(marca_vehiculo, marca_modelo)
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargando = True



