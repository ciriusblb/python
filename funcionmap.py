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
    Empleado("juan1", "director1", 750),
    Empleado("juan2", "director2", 850),
    Empleado("juan3", "director3", 250),
    Empleado("juan4", "director4", 270),
    Empleado("juan5", "director5", 210)
]

def calculocomision(empleado):
    empleado.salario = empleado.salario*1.03
    return empleado

listaEmpleadosComision = map(calculocomision, empleados)

for empleado in listaEmpleadosComision:
    print(empleado)



