import easygui

# Pedir el primer número
numero1 = easygui.enterbox("Ingrese el número 1:", "Entrada de Número 1")

# Pedir el segundo número
numero2 = easygui.enterbox("Ingrese el número 2:", "Entrada de Número 2")

# Convertir las entradas a enteros y sumar
try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    total = numero1 + numero2
    print(f"El total es: {total}")
except ValueError:
    print("Por favor, ingrese números válidos.")
