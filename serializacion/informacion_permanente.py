import pickle
class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("se ha creado una persona con el nombre de: ", self.nombre)
    
    def __str__(self): # convertir en cadena de texto la inforamcion de un objeto
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class listaPersonas:
    personas =[]

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+") #agregar informacion binario
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)
    
    def mostrarInfoFicheroExterno(self):
        print("leyendo informacion")
        for p in self.personas:
            print(p)

miLista = listaPersonas()

# agregando personas-----------------
p = Persona("Antonio", "masculino", 19)
miLista.agregarPersonas(p)
miLista.mostrarInfoFicheroExterno()

# p = Persona("Antonio", "masculino", 19)
# miLista.agregarPersonas(p)
# p = Persona("ana", "femenino", 39)
# miLista.agregarPersonas(p)

# miLista.mostrarPersonas()

