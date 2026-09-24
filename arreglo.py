class Ventas:
    def __init__(self):
        self.meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]

        self.departamentos = ["Ropa", "Deportes", "Jugueteria"]

        self.ventas = [[0, 0, 0] for i in range(12)]

    def insertar(self):
        mes = input("Ingresa el mes: ")
        departamento = input("Ingresa el departamento: ")
        venta = float(input("Ingresa la venta: "))

        fila = self.meses.index(mes)
        columna = self.departamentos.index(departamento)

        self.ventas[fila][columna] = venta

        print("Venta agregada correctamente.")

    def buscar(self):
        mes = input("Ingresa el mes que quieres buscar: ")
        departamento = input("Ingresa el departamento: ")

        fila = self.meses.index(mes)
        columna = self.departamentos.index(departamento)

        print("La venta es:", self.ventas[fila][columna])

    def eliminar(self):
        mes = input("Ingresa el mes de la venta que quieres eliminar: ")
        departamento = input("Ingresa el departamento: ")

        fila = self.meses.index(mes)
        columna = self.departamentos.index(departamento)

        self.ventas[fila][columna] = 0

        print("Venta eliminada correctamente.")

    def mostrar(self):
        print("\n\tRopa\tDeportes\tJugueteria")

        for i in range(12):
            print(self.meses[i], "\t", 
                  self.ventas[i][0], "\t",
                  self.ventas[i][1], "\t\t",
                  self.ventas[i][2])


ventas = Ventas()

while True:

    print("\n¿Que quieres hacer?")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar ventas")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        ventas.insertar()

    elif opcion == "2":
        ventas.buscar()

    elif opcion == "3":
        ventas.eliminar()

    elif opcion == "4":
        ventas.mostrar()

    elif opcion == "5":
        print("Fin.")
        break

    else:
        print("Opcion no valida.")