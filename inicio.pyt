# Clase Producto
class Producto:
    def __init__(self, nombre, descripcion, precio, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen

    def mostrar_info(self):
        return f"Producto: {self.nombre}\nDescripción: {self.descripcion}\nPrecio: ${self.precio}\nImagen: {self.imagen}"

# Lista para almacenar los productos
productos = []

# Función para agregar un producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    imagen = input("Ingrese el nombre o ruta de la imagen del producto: ")

    producto = Producto(nombre, descripcion, precio, imagen)
    productos.append(producto)
    print("\nProducto agregado exitosamente!")

# Función para mostrar todos los productos
def mostrar_productos():
    if not productos:
        print("\nNo hay productos disponibles.")
    else:
        for idx, producto in enumerate(productos, 1):
            print(f"\nProducto #{idx}")
            print(producto.mostrar_info())

# Menú principal
def menu():
    while True:
        print("\n--- Sistema de Subida de Productos ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el sistema
    menu()
 
