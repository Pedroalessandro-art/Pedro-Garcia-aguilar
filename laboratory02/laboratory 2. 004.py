print("=== MENÚ DE COMIDA ===")
print("1. Pizza")
print("2. Hamburguesa")
print("3. Tacos")
print("4. Ensalada")

option = int(input("Elige una opción: "))

match option:
    case 1:
        print("Pediste una Pizza")
    case 2:
        print("Pediste una Hamburguesa")
    case 3:
        print("Pediste unos Tacos")
    case 4:
        print("Pediste una Ensalada")
    case _:
        print("Opción no válida")