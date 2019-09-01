# #------------generadores -------------
# # funciones que nos devuelven un valor de una lista
# def generaPares(limite):
#     num = 1
#     while num< limite:
#         yield num*2 # este valor se devuelve, pero num no pierde suvalor y hace como si nunca terminara la funcion
#         num = num+1

# devuelvePares = generaPares(10) # queda en estado de suspension
# # es como si se ejecutra la funcion varias veces, pero no 
# # for i in devuelvePares:
# #     print(i)
# #asi obtenermos los valores que vayamos necesitantp
# print(next(devuelvePares))
# # aqui podriamos poner codigo
# print(next(devuelvePares))
# # aqui podriamos poner codigo
# print(next(devuelvePares))


#------yield from ---------------
def devuelve_ciudades(*ciudades): # el asterisco quieres decir que ciudades es un tupla de tamaño indefinido
    for elemento in ciudades:
        # for subElemento in elemento:
        #     yield subElemento
        yield from elemento

ciudades_devueltas = devuelve_ciudades("madrid", "peru", "casas")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
