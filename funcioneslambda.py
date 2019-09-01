# def area_triangulo(base,altura):
#     return (base*altura)/2

# print(area_triangulo(5,7))


#---funcion lambda-------

area_triangulo = lambda base, altura: (base*altura)/2
print(area_triangulo(5,7))

raiz = lambda numero, ponente: numero**ponente
rais = lambda numero, ponente: pow(numero,ponente)

print(raiz(5,3))
print(rais(5,3))
