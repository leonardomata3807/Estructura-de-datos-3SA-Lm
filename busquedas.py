def busqueda_secuencial(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i]["nombre"].lower() == objetivo.lower():
            return i, comparaciones
    return -1, comparaciones


def ejercicio_secuencial():
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
    print("\n=== BÚSQUEDA SECUENCIAL: INVENTARIO DE TIENDA ===")
    print("Productos:", ", ".join(p["nombre"] for p in inventario))
    producto = input("\nProducto a buscar: ").strip()
    pos, comp = busqueda_secuencial(inventario, producto)
    if pos != -1:
        p = inventario[pos]
        print(f"\n✔ Encontrado en la posición {pos}")
        print(f"  Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Stock: {p['stock']}")
    else:
        print("\n✘ El producto no existe en el inventario.")
    print(f"  Comparaciones realizadas: {comp}")


def busqueda_binaria(lista, objetivo):
    inicio, fin, comparaciones = 0, len(lista) - 1, 0
    while inicio <= fin:
        medio = (inicio + fin) // 2
        comparaciones += 1
        if lista[medio]["matricula"] == objetivo:
            return medio, comparaciones
        elif objetivo < lista[medio]["matricula"]:
            fin = medio - 1
        else:
            inicio = medio + 1
    return -1, comparaciones


def ejercicio_binaria():
    alumnos = [
        {"matricula": 1001, "nombre": "Ana López", "promedio": 92},
        {"matricula": 1005, "nombre": "Luis Pérez", "promedio": 85},
        {"matricula": 1008, "nombre": "María Gómez", "promedio": 97},
        {"matricula": 1012, "nombre": "Carlos Ruiz", "promedio": 78},
        {"matricula": 1015, "nombre": "Sofía Martín", "promedio": 88},
        {"matricula": 1020, "nombre": "Jorge Díaz", "promedio": 81},
        {"matricula": 1024, "nombre": "Elena Castro", "promedio": 94},
        {"matricula": 1030, "nombre": "Pedro Salas", "promedio": 73},
        {"matricula": 1033, "nombre": "Laura Vega", "promedio": 90},
        {"matricula": 1040, "nombre": "Diego Torres", "promedio": 86},
    ]
    alumnos.sort(key=lambda a: a["matricula"])
    print("\n=== BÚSQUEDA BINARIA: REGISTRO DE ALUMNOS ===")
    print("Matrículas:", ", ".join(str(a["matricula"]) for a in alumnos))
    try:
        matricula = int(input("\nMatrícula a buscar: "))
    except ValueError:
        print("Debes escribir un número entero.")
        return
    pos, comp = busqueda_binaria(alumnos, matricula)
    if pos != -1:
        a = alumnos[pos]
        print(f"\n✔ Encontrado en la posición {pos}")
        print(f"  Alumno: {a['nombre']} | Promedio: {a['promedio']}")
    else:
        print("\n✘ La matrícula no está registrada.")
    print(f"  Comparaciones realizadas: {comp}")


class TablaHash:
    def __init__(self, tamano=11):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def _hash(self, clave):
        return sum(ord(c) for c in clave.lower()) % self.tamano

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        for i, (k, _) in enumerate(self.tabla[indice]):
            if k.lower() == clave.lower():
                self.tabla[indice][i] = (clave, valor)
                return
        self.tabla[indice].append((clave, valor))

    def buscar(self, clave):
        indice = self._hash(clave)
        comparaciones = 0
        for k, v in self.tabla[indice]:
            comparaciones += 1
            if k.lower() == clave.lower():
                return v, indice, comparaciones
        return None, indice, comparaciones

    def mostrar(self):
        for i, cubeta in enumerate(self.tabla):
            contenido = " -> ".join(k for k, _ in cubeta) if cubeta else "(vacía)"
            print(f"  [{i:2}] {contenido}")


def ejercicio_hash():
    directorio = TablaHash()
    contactos = {
        "Ana": "999-123-4567", "Luis": "999-234-5678", "María": "999-345-6789",
        "Carlos": "999-456-7890", "Sofía": "999-567-8901", "Jorge": "999-678-9012",
        "Elena": "999-789-0123", "Pedro": "999-890-1234", "Laura": "999-901-2345",
        "Diego": "999-012-3456",
    }
    for nombre, tel in contactos.items():
        directorio.insertar(nombre, tel)
    print("\n=== BÚSQUEDA HASH: DIRECTORIO TELEFÓNICO ===")
    print("Estructura de la tabla hash:")
    directorio.mostrar()
    nombre = input("\nNombre a buscar: ").strip()
    tel, indice, comp = directorio.buscar(nombre)
    if tel:
        print(f"\n✔ Encontrado en la casilla {indice}")
        print(f"  {nombre.title()}: {tel}")
    else:
        print(f"\n✘ El contacto no existe (se revisó la casilla {indice}).")
    print(f"  Comparaciones realizadas: {comp}")


def menu():
    while True:
        print("\n" + "=" * 45)
        print("        MÉTODOS DE BÚSQUEDA - MENÚ")
        print("=" * 45)
        print("1. Búsqueda Secuencial (inventario)")
        print("2. Búsqueda Binaria    (alumnos)")
        print("3. Búsqueda Hash       (directorio)")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ejercicio_secuencial()
        elif opcion == "2":
            ejercicio_binaria()
        elif opcion == "3":
            ejercicio_hash()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()