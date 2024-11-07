import unittest
from conexion.conexion import create_table, insert_row, read_rows

class TestConexion(unittest.TestCase):

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
        
if __name__ == '__main__':
    unittest.main()
