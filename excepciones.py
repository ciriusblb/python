# def suma(num1, num2):
# 	return num1+num2

# def resta(num1, num2):
# 	return num1-num2

# def multiplica(num1, num2):
# 	return num1*num2

# def divide(num1,num2):
#     try:
#         return num1/num2
#     except ZeroDivisionError: #tipo de error que queremos comunicaar
#         print("No se puede dividir entre 0")
#         return "Operacion erronea"			

# op1=(int(input("Introduce el primer n�mero: ")))

# op2=(int(input("Introduce el segundo n�mero: ")))		
	
# operacion=input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

# if operacion=="suma":
# 	print(suma(op1,op2))

# elif operacion=="resta":
# 	print(resta(op1,op2))

# elif operacion=="multiplica":
# 	print(multiplica(op1,op2))

# elif operacion=="divide":
# 	print(divide(op1,op2))

# else:
# 	print ("Operacion no contemplada")


# print("Operaci�n ejecutada. Continuaci�n de ejec�ci�n del programa ")

# -----------------------difernetes excepciones y finally ------------------
# def divide():
#     try:
#         op1 = float(input("primer numero: "))
#         op2 = float(input("segundo numero: "))
#         print("la division es: "+ str(op1/op2))

#     # except: #excepcion general
#     #     print("error")
#     except ValueError: # especificamos los tipos de excepciones
#         print("el valor introducido es incorrecto")
#     except ZeroDivisionError: # especificamos los tipos de excepciones
#         print("no se puede dividir entre cero")
#     finally:# el codigo que se ejecutara siempre si o si 
#         print("calculo finalizado") 

# divide()


# --------------------lanzamiento de excepciones intencioanl (Raise) -----------


# def evaluaedad(edad):

#     if edad < 0:
#         raise TypeError("No se permiten edades negativas")

#     if edad<20:
#         return "eres muy joven"
#     elif edad <40:
#         return "eres joven"
#     elif edad <65:
#         return "eres maduro"
#     elif edad <100:
#         return "cuidate"
# print(evaluaedad(-90))


# --------------------ejmplo (Raise) -----------
import math
def calcularRaiz(num1):
    if num1 <0:
        raise ValueError("El numero no puefde ser negativo")
    else:
        return math.sqrt(num1)

opt = int(input("numero: "))
try:
    print(calcularRaiz(opt))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("finalizado")





