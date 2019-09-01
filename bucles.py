# for i in ["pildoras", "informaticas", 3]:
#     print("Hola", end= " ") #para quitar el salto de  linea

# -----------------ejercicio-------------------
# email = False
# for i in "ciriusblb@gmail.com": #iterar i tantas veces caracteres tenga el string
#     if i == "@":
#         email = True

# if email:
#     print("email corecto")
# else:
#     print("enamil incorrrecto")

# ----------for-------

# for i in range(5):
#     print(i)

# for i in range(5, 10): # de donde a donde
#     print(f"numero {i}")

# for i in range(5, 40, 5): # de donde a donde y de cuando en cuanto
#     print(f"numero {i}")


# ----------while------------------

# i = 1
# while i <= 10:
#     print("Ejecucion "+ str(i))
#     i= i+1
# print("termino")

# ----------------------ejercicio------------------------------

# edad = int(input("ingrese edad: "))
# while edad<5 or edad>100:
#     print("edad incorrecta")
#     edad = int(input("introduce edad de nuevo: "))

# print("bye " + str(edad))

# ----------------------ejercicio------------------------------
# import math
# print("programa raiz cuadrada")
# numero = int(input("ingrese numero: "))

# intentos = 1
# while numero < 0:
#     print("no hay raiz de numero negativo")
#     if intentos == 3:
#         print("no sabes ni que son numeros negativos, largate")
#         break
#     numero = int(input("vuelva a ingresar numero: "))
#     if numero < 0:
#         intentos = intentos + 1

# if intentos < 3:
#     solucion = math.sqrt(numero)
#     print("la raiz de: "+ str(numero) + " es: " + str(solucion))


#--------------continue, pass, else---------------

# for i in "python":
#     if i == "h":
#         continue #pasa a la siguiente iteracion ignorando el codigo de abajo
#     print("letra:  " +i)

# ----------ejemplo------------------
# c = 0
# for i in "ciro yupanqui":
#     if i == " ":
#         continue #pasa a la siguiente iteracion ignorando el codigo de abajo
#     c+=1
# print("tamaño: "+ str(c))

# ------------pass---------
# class miclase:
#     pass #para implementar mas tarde
#     # el pass sirve par ignorar codigo


#--------------else------------
#  email = input("email: ")
#  for i in email:
#      if i == "@":
#          arroba = True
#          break

# else:  # else del for, en caso de que el for termine sin saltos(break)
#     arroba = False
# print(arroba)



