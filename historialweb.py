
class Pila:
    def __init__(self):
        self.sitios = []

    def apilar(self, sitio):
        self.sitios.append(sitio)

    def desapilar(self):
        if len(self.sitios) > 0:
            return self.sitios.pop()
        return None

    def esta_vacia(self):
        return len(self.sitios) == 0

    def mostrar(self):
        if self.esta_vacia():
            print("El historial esta vacio")
        else:
            print("\nHistorial de sitios visitados:")
            for sitio in reversed(self.sitios):
                print(sitio)


historial = Pila()

while True:
    print("\n--- NAVEGADOR WEB ---")
    print("1. Visitar sitio")
    print("2. Mostrar historial")
    print("3. Regresar al sitio anterior")
    print("4. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        sitio = input("Escribe la direccion del sitio: ")
        historial.apilar(sitio)
        print("Sitio visitado:", sitio)

    elif opcion == "2":
        historial.mostrar()

    elif opcion == "3":
        if len(historial.sitios) > 1:
            historial.desapilar()
            print("Regresaste a:", historial.sitios[-1])
        elif len(historial.sitios) == 1:
            print("No hay un sitio anterior")
        else:
            print("No hay sitios en el historial")

    elif opcion == "4":
        print("Cerrando navegador...")
        break

    else:
        print("Opcion no valida")
