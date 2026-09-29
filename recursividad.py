inventario = {
    "Ropa": {
        "Hombre": {
            "Playeras": 20,
            "Pantalones": 15,
            "Sudaderas": 10
        },
        "Mujer": {
            "Blusas": 18,
            "Vestidos": 12,
            "Pantalones": 14
        }
    },

    "Electronica": {
        "Celulares": {
            "iPhone": 8,
            "Samsung": 12,
            "Xiaomi": 10
        },
        "Computadoras": {
            "Laptops": 7,
            "PC": 5,
            "Monitores": 9
        }
    },

    "Deportes": {
        "Futbol": {
            "Balones": 20,
            "Tachones": 15,
            "Guantes": 8
        },
        "Basquetbol": {
            "Balones": 12,
            "Tenis": 10,
            "Playeras": 15
        }
    }
}


# Funcion recursiva para mostrar el inventario
def mostrar_inventario(inventario, nivel=0):

    for nombre in inventario:

        print("  " * nivel + nombre)

        if type(inventario[nombre]) == dict:

            mostrar_inventario(inventario[nombre], nivel + 1)


# Funcion recursiva para buscar un producto
def buscar_producto(inventario, producto):

    for nombre in inventario:

        if nombre.lower() == producto.lower():

            return True

        if type(inventario[nombre]) == dict:

            encontrado = buscar_producto(inventario[nombre], producto)

            if encontrado:

                return True

    return False


# Funcion recursiva para contar productos
def contar_productos(inventario):

    total = 0

    for nombre in inventario:

        if type(inventario[nombre]) == dict:

            total = total + contar_productos(inventario[nombre])

        else:

            total = total + inventario[nombre]

    return total


print("===== SISTEMA DE INVENTARIO =====")

print("\nInventario de la tienda:\n")

mostrar_inventario(inventario)

print("\n===============================")

producto = input("\nEscribe el producto que quieres buscar: ")

if buscar_producto(inventario, producto):

    print("El producto SI se encuentra en el inventario.")

else:

    print("El producto NO se encuentra en el inventario.")


print("\nCantidad total de productos:", contar_productos(inventario))