class Coche():
    def desplazamiento(self):
        print("me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("me desplazo en 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("me desplazo en 6 ruedas")

# mivehuculo = Moto()
# mivehuculo.desplazamiento()

# mivehuculo2 = Coche()
# mivehuculo2.desplazamiento()

# mivehuculo3 = Camion()
# mivehuculo3.desplazamiento()

# polimorfismo  cambiar de forma de una clase
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento() # usar el metodo de la clase instanciada

mivehuculo =Coche() # instanciamos a cualquier clase
desplazamientoVehiculo(mivehuculo) #pasar instancia a un metodo