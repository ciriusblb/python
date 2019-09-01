class Coche():
    def __init__(self): # constructor __init__
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # encapsulamiento, poniendo dos subguiones antes de la propiedad
        self.__enmarcha = False # el encapsualmiento sirve para que la propiedad solo sea accecible desde dedntro de la clase
        
    def arrancar(self, arrancamos): # metodos
        self.__enmarcha = arrancamos 
        if self.__enmarcha:
            chequeo = self.__chequeo_interno()
        if self.__enmarcha and chequeo:
            return "el coche esta en marcha"
        elif self.__enmarcha and chequeo== False:
            return "Algo ha ido mal, no podemos arrancar"
        else: 
            return "el coche esta detenido"

    def estado(self):
        print("El coche tiene ruedas: ", self.__ruedas)
        print("El coche tiene ancho: ", self.__anchoChasis)
        print("El coche tiene largo: ", self.__largoChasis)
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "cerradas"
        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

miCoche = Coche() # instancia 
print(miCoche.arrancar(True))
print(miCoche.estado())

print("acontinuacion creamos el segundo objeto------------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
print(miCoche2.estado())

