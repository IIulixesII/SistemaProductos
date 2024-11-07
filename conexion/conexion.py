import sqlite3 as sql
import os

def create_db():
    # Elimina la base de datos si existe
    if os.path.exists("productos.db"):
        os.remove("productos.db")

    # Crea una conexión para la nueva base de datos
    conn = sql.connect("productos.db")
    conn.commit()
    conn.close()

def create_table():
    # Crea la tabla productos con un campo autoincrementable 'id'
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            precio INTEGER,
            categoria TEXT,
            img TEXT
        )"""
    )
    conn.commit()
    conn.close()

def insert_row(nombre, precio, categoria, img):
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio, categoria, img) VALUES (?, ?, ?, ?)",
        (nombre, precio, categoria, img)
    )
    conn.commit()
    conn.close()

def read_rows():
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conn.close()
    return datos

def delete_row(nombre):
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
    conn.commit()
    conn.close()
    
def read_product_by_id(producto_id):
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    return cursor.fetchone()  # Retorna una tupla con los datos del producto

# Ejecuta estas funciones para configurar la base de datos al inicio
if __name__ == "__main__":
    create_db()
    create_table()
