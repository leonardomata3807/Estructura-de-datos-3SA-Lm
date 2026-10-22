
class Cola:
    def __init__(self):
        self.elementos = []

    def insertar(self, dato):
        self.elementos.append(dato)

    def quitar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


servicios = {
    1: Cola(),
    2: Cola(),
    3: Cola()
}

contadores = {
    1: 0,
    2: 0,
    3: 0
}

print("SISTEMA DE ATENCION - COMPANIA DE SEGUROS")
print("Servicios disponibles: 1, 2 y 3")
print("C1, C2 o C3: registrar cliente")
print("A1, A2 o A3: atender cliente")
print("S: salir del sistema")

while True:
    comando = input("\nIngrese un comando: ").upper()

    if comando == "S":
        print("Sistema finalizado.")
        break

    elif len(comando) == 2 and comando[0] in ["C", "A"] and comando[1] in "123":
        accion = comando[0]
        servicio = int(comando[1])

        if accion == "C":
            contadores[servicio] += 1
            turno = contadores[servicio]

            servicios[servicio].insertar(turno)

            print("Cliente registrado.")
            print("Su numero de atencion es:", turno)
            print("Servicio:", servicio)

        elif accion == "A":
            if servicios[servicio].esta_vacia():
                print("No hay clientes esperando en este servicio.")
            else:
                turno = servicios[servicio].quitar()
                print("Atendiendo al cliente numero:", turno)
                print("Servicio:", servicio)

    else:
        print("Comando no valido. Intente nuevamente.")
