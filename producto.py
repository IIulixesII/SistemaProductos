
class Producto:
    def __init__(self, nombre, descripcion, precio, imagen):
        # Inicializa los atributos del producto
        self.nombre = nombre  
        self.descripcion = descripcion  
        self.precio = precio  
        self.imagen = imagen  

    def mostrar_info(self):
        return f"Producto: {self.nombre}\nDescripción: {self.descripcion}\nPrecio: ${self.precio}\nImagen: {self.imagen}"

# ARRAY para almacenar los productos
productos = []

def agregar_producto():
    # Solicita la información del producto al usuario
    nombre = input("Ingrese el nombre del producto: ")  
    descripcion = input("Ingrese la descripción del producto: ")  
    precio = float(input("Ingrese el precio del producto: ")) 
    imagen = input("Ingrese el nombre o ruta de la imagen del producto: ")  

    # Crea un nuevo objeto Producto con la información proporcionada
    producto = Producto(nombre, descripcion, precio, imagen)
    # Agrega el objeto Producto a la lista de productos
    productos.append(producto)
    print("\nProducto agregado exitosamente!")  

def mostrar_productos():
    if not productos: #not  hace que si es none productos es verdadero
        print("\nNo hay productos disponibles.") 
    else:
        # Recorre la lista de productos utilizando un bucle
        for i in range(len(productos)):
            print(f"\nProducto #{i + 1}:")  # Muestra los productos de la array sumando 1+ 
            print(productos[i].mostrar_info())  # Llama al método 'mostrar_info' 
