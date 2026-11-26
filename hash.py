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
            contenido = " -> ".join(f"{k}" for k, _ in cubeta) if cubeta else "(vacía)"
            print(f"  [{i:2}] {contenido}")


def main():
    directorio = TablaHash()
    contactos = {
        "Ana": "999-123-4567",
        "Luis": "999-234-5678",
        "María": "999-345-6789",
        "Carlos": "999-456-7890",
        "Sofía": "999-567-8901",
        "Jorge": "999-678-9012",
        "Elena": "999-789-0123",
        "Pedro": "999-890-1234",
        "Laura": "999-901-2345",
        "Diego": "999-012-3456",
    }
    for nombre, tel in contactos.items():
        directorio.insertar(nombre, tel)

    print("=== BÚSQUEDA HASH: DIRECTORIO TELEFÓNICO ===")
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


if __name__ == "__main__":
    main()