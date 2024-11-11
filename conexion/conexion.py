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
    
def insert_usuario(nombre, contraseña, gmail, fecha_nacimiento, foto_perfil=None):
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuario (nombre, contraseña, gmail, fecha_nacimiento, foto_perfil) VALUES (?, ?, ?, ?, ?)",
        (nombre, contraseña, gmail, fecha_nacimiento, foto_perfil)
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
def create_table_usuarioadmin():
    # Crea la tabla usuarioadmin con los campos 'nombre' y 'contraseña'
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuarioadmin(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            contraseña TEXT NOT NULL
        )"""
    )
    conn.commit()
    conn.close()
def insert_admin_user():
    # Inserta un usuario administrador con nombre 'ulises' y contraseña 'ulises12'
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarioadmin (nombre, contraseña) VALUES (?, ?)",
        ('ulises', 'ulises12')
    )
    conn.commit()
    conn.close()
def create_table_usuario():
    # Crea la tabla usuario con los campos 'nombre', 'contraseña', 'gmail', 'fecha_nacimiento' y 'foto_perfil'
    conn = sql.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            contraseña TEXT NOT NULL,
            gmail TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            foto_perfil TEXT
        )"""
    )
    conn.commit()
    conn.close()
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
 
    delete_row("ProductoEliminar")
