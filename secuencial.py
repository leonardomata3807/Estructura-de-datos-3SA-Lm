def busqueda_secuencial(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i]["nombre"].lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones


def main():
    
    inventario = [
        {"nombre": "Leche", "precio": 28.50, "stock": 40},
        {"nombre": "Pan", "precio": 15.00, "stock": 25},
        {"nombre": "Huevo", "precio": 45.00, "stock": 60},
        {"nombre": "Arroz", "precio": 22.00, "stock": 35},
        {"nombre": "Frijol", "precio": 30.00, "stock": 50},
        {"nombre": "Aceite", "precio": 52.00, "stock": 18},
        {"nombre": "Azucar", "precio": 26.00, "stock": 42},
        {"nombre": "Cafe", "precio": 85.00, "stock": 20},
        {"nombre": "Galletas", "precio": 18.00, "stock": 70},
        {"nombre": "Refresco", "precio": 20.00, "stock": 90},
    ]

    print("=== BÚSQUEDA SECUENCIAL: INVENTARIO DE TIENDA ===")
    print("Productos disponibles:", ", ".join(p["nombre"] for p in inventario))

    producto = input("\nProducto a buscar: ").strip()
    pos, comp = busqueda_secuencial(inventario, producto)

    if pos != -1:
        p = inventario[pos]
        print(f"\n✔ Encontrado en la posición {pos}")
        print(f"  Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Stock: {p['stock']}")
    else:
        print("\n✘ El producto no existe en el inventario.")
    print(f"  Comparaciones realizadas: {comp}")


if __name__ == "__main__":
    main()