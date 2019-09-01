import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()

# crear tabla-------------
# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


# insertar un registro -------------------
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('balon', 12, 'deportes')")

#insertar varios registros a la vez -------------------
# variosProductos = [
#     ("Camiseta", 10, "Deportes"),
#     ("Jarron", 10, "Ceramica"),
#     ("Camion", 10, "Juqueteria")
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)

# leer registros de una tabla---------------
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()
for producto in variosProductos:
    print(producto)

    
miConexion.commit()
miConexion.close()