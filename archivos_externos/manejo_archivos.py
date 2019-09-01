from io import open
# crear archivo ----------------
# archivo_texto = open("archivo.txt", "w")
# frase = "Estupendo dia para estudiar Python \n el miercoles"
# archivo_texto.write(frase)
# archivo_texto.close()

#leeer archivoo ----------------
# archivo_texto = open("archivo.txt", "r")
# texto = archivo_texto.read()
# archivo_texto.close()
# print(texto)

# leer archivos por linea ------------
# archivo_texto = open("archivo.txt", "r")
# lineas_texto = archivo_texto.readlines()
# archivo_texto.close()
# print(lineas_texto) # lista de lineas (array)

# agregar texto a un archivo existente ----------
# archivo_texto = open("archivo.txt", "a")
# archivo_texto.write("\n siempre es una buena ocacion para estudiar texto")
# archivo_texto.close()

# leer un archivo luego de situar el cursor en una posicion --------
# archivo_texto = open("archivo.txt", "r")
# archivo_texto.seek(11) #posicion del cursor
# texto = archivo_texto.read()
# print(texto)

# leer un archivo hasta cieta posicion ------
# archivo_texto = open("archivo.txt", "r")
# texto = archivo_texto.read(11) # leer hast al posicion 11 y dejar el cursor en esa posicion
# print(texto)


# leer y escribir un archivo ------
archivo_texto = open("archivo.txt", "r+")
lista_texto = archivo_texto.readlines()
lista_texto[0] = "Esta linea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()


