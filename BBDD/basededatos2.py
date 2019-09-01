import sqlite3
miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

# miCursor.execute('''
#     CREATE TABLE PRODUCTOS(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARHCHAR(50) UNIQUE,
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
#     )
# ''')

# productos = [
#     ("pelota", 10, "jugueteria"),
#     ("pantalon", 15, "confeccion"),
#     ("destornillador", 25, "ferreteria"),
#     ("jarron", 45, "ceramica")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)
# miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 100 WHERE ID = 3")
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 2")
miCursor.execute("SELECT * FROM PRODUCTOS")
productos = miCursor.fetchall()
for producto in productos:
    print(producto)

miConexion.commit()
miConexion.close()

