import unittest
from conexion.conexion import insert_row, read_rows, delete_row, create_db, create_table, create_table_usuario, create_table_usuarioadmin

class TestConexion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crea la base de datos y las tablas antes de ejecutar las pruebas
        create_db()
        create_table()
        create_table_usuario()
        create_table_usuarioadmin()

    def test_agregar_producto(self):
        # Inserta un producto de prueba
        insert_row("ProductoAgregar", 200, "CategoriaAgregar", "img/agregar.jpg")
        
        # Verifica que el producto fue insertado
        productos = read_rows()
        # Busca el producto en la lista, ignorando el 'id'
        self.assertIn(
            ("ProductoAgregar", 200, "CategoriaAgregar", "img/agregar.jpg"),
            [(nombre, precio, categoria, img) for (_, nombre, precio, categoria, img) in productos],
            "El producto no se insertó correctamente"
        )

    def tearDown(self):
        # Limpieza después de cada prueba
        delete_row("ProductoAgregar")

if __name__ == "__main__":
    unittest.main()
