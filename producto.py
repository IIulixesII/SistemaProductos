# producto.py

class Producto:
    def __init__(self, nombre, descripcion, precio, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen

    # Método que devuelve la información del producto
    def mostrar_info(self):
        return f"Producto: {self.nombre}\nDescripción: {self.descripcion}\nPrecio: ${self.precio}\nImagen: {self.imagen}"

productos = []  # Lista global para almacenar productos

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    imagen = input("Ingrese el nombre o ruta de la imagen del producto: ")

    producto = Producto(nombre, descripcion, precio, imagen)
    productos.append(producto)
    print("\nProducto agregado exitosamente!")

def mostrar_productos():
    if not productos:  # Verifica si la lista de productos está vacía
        print("\nNo hay productos disponibles.")
    else:
        for i in range(len(productos)):  # Usar un bucle for con range para recorrer los índices
            print(f"\nProducto #{i + 1}:")
            print(productos[i].mostrar_info())  # Llama al método 'mostrar_info' para mostrar los detalles de cada producto
