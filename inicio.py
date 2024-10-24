
from producto import agregar_producto, mostrar_productos  # Importar las funciones


def menu():
    while True:
        print("\n--- Sistema de Subida de Productos ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto()  # Pasar la lista de productos a la función
        elif opcion == '2':
            mostrar_productos()  # Pasar la lista de productos a la función
        elif opcion == '3':
            print("Saliendo del sistema...")
            break  # Termina el bucle y cierra el programa
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
