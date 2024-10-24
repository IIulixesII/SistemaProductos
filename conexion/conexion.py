import sqlite3 as sql

def createDB():
    conn = sql.connect("productos.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productos(
        nombre text,
        precio integer,
        categoria text,
        img text
        )"""
    )
    conn.commit()
    conn.close()

def insertrow(nombre, precio, categoria, img):
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO productos (nombre, precio, categoria, img) VALUES ('{nombre}', {precio}, '{categoria}', '{img}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def insertrows(ProductosList):
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    instruccion = "INSERT INTO productos (nombre, precio, categoria, img) VALUES (?, ?, ?, ?)"
    cursor.executemany(instruccion, ProductosList)  # Ejecutar para múltiples filas
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    instruccion = "SELECT * FROM productos"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.close()
    print(datos)


def deleteRow(nombre):
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    instruccion = "DELETE FROM productos WHERE nombre = ?"
    cursor.execute(instruccion, (nombre,))  # Pasar el nombre como parámetro
    conn.commit()  # Guardar los cambios
    conn.close()
    print(f"Producto '{nombre}' eliminado.")

if __name__ == "__main__":
    createTable()  # Crear la tabla si no existe
    ProductosList = [
        ("Telefono", 500000, "Electronico", "img/saff/aff"),
        ("Auriculares", 30000, "Electronico", "img/afaf/awds"),
        ("Play5", 1000000, "Electronico", "img/afdad/sad")
    ]
    
deleteRow("Computadora")      
readRows()  # Leer y mostrar las filas
