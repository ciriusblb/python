# def numero_par(num):
#     if num % 2 == 0:
#         return True

# numeros = [12,13,14,15,16,17,18]
# # print(list(filter(numero_par,numeros)))

# print(list(filter(lambda numero_par: numero_par %2 ==0, numeros)))


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} ".format(self.nombre, self.cargo, self.salario)

    
empleados = [
    Empleado("juan1", "director1", 75000),
    Empleado("juan2", "director2", 85000),
    Empleado("juan3", "director3", 25000),
    Empleado("juan4", "director4", 27000),
    Empleado("juan5", "director5", 21000)
]

salarios_altos = filter(lambda empleado: empleado.salario>50000, empleados)

for emplado_salario in salarios_altos:
    print(emplado_salario)



