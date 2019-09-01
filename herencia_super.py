class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def descripcion(self):
        print("nombre: ", self.nombre, "\nedad: ", self.edad, "\nElugar_residencia ", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, lugar_residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, lugar_residencia_empleado) # el metodo super llama al metodo init de la clase padre

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion() # el metodo super llama al metodo de clases padres de la clase padre
        print("salario: ", self.salario, "\nantiguedad: ", self.antiguedad)

Antonio = Empleado(444, 35, "Antonio", 45, "maldonaod")
Antonio.descripcion()

print(isinstance(Antonio, Empleado)) # para ver si un objeto es una instancia de una clase padre