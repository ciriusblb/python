# print("programa de evaluacion de notas de alumnos")

# nota_alumno = input("Introduce la nota del alumno; ") #todo valor ingresado por input entra de tipo string
# def evaluacion(nota):
#     valoracion = "aprobado"
#     if nota < 5:
#         valoracion = "suspenso"
#     return valoracion

# print(evaluacion(int(nota_alumno)))


# ---------------------------------------------
# print("Verificacion de acceso")
# edad_usuario = int(input("Ingrese edad: "))
# if edad_usuario < 18:
#     print("no puede pasar")
# elif edad_usuario > 100: # nueva sentencia elif  = else if
#     print("eadad icorrecta")
# else: #el else funciona con los dos condicionales en l aparte superior
#     print("puedes psar")



# elif --------------------------------------
# print("Verificando las notas")
# nota_alumno = int(input("ingrese nota: "))
# if nota_alumno < 5:
#     print("insuficiente")
# elif nota_alumno < 6:
#     print("suficiente")
# elif nota_alumno < 7:
#     print("bien")
# elif nota_alumno < 8:
#     print("notalbe")
# else:
#     print("sobresaliente")

# --------concatenacion de operadores-----------------
# edad = 7
# if 0 < edad < 100:
#     print("coreccto")
# else: 
#     print("incorrectp")

# -------------------concatenacion de operadores----------------------------------

# salario_presidente = int(input("Introduce salario presidente: "))
# print("salario presidente: " + str(salario_presidente))

# salario_director = int(input("Introduce salario director: "))
# print("salario director: " + str(salario_director))

# salario_jefe_area = int(input("Introduce salario jefe de area: "))
# print("salario jefe de area: " + str(salario_jefe_area))

# salario_administrativo = int(input("Introduce salario administrativo: "))
# print("salario administrativo: " + str(salario_administrativo))

# if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
#     print("coreccto")
# else:
#     print("incorrecto")



#------------------------------------

# distancia_escuela = int(input("distancia escuela: "))
# print(distancia_escuela)

# numero_hermanos = int(input("numero hermanos: "))
# print(numero_hermanos)

# salario_familiar = int(input("salario familiar: "))
# print(salario_familiar)

# if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 2000:
#     print("derecho a beca")
# else:
#     print("no tiene derecho")


# -------------------------------------------
print("Asignaturas optativas año 2019")
print("Matematica, Informatica, Ciencias")
opcion = input("Escoja asignatura: ")
asignatura = opcion.lower()
if(asignatura in ("matematica", "informatica", "ciencias")):
    print("asignatura el elejido: " + asignatura)
else: 
    print("eroror al escojer la asigantura")