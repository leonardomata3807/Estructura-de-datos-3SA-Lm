class Cola:
    def __init__(self):
        self.elementos = []

    def insertar(self, dato):
        self.elementos.append(dato)

    def quitar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        print(self.elementos)


def sumar_colas(cola_a, cola_b):
    resultado = Cola()

    if len(cola_a.elementos) != len(cola_b.elementos):
        print("Las colas deben tener la misma cantidad de elementos")
        return resultado

    for i in range(len(cola_a.elementos)):
        suma = cola_a.elementos[i] + cola_b.elementos[i]
        resultado.insertar(suma)

    return resultado


cola_a = Cola()
for numero in [3, 4, 2, 8, 12]:
    cola_a.insertar(numero)

cola_b = Cola()
for numero in [6, 2, 9, 11, 3]:
    cola_b.insertar(numero)

cola_resultado = sumar_colas(cola_a, cola_b)

print("Cola A:")
cola_a.mostrar()

print("Cola B:")
cola_b.mostrar()

print("Cola Resultado:")
cola_resultado.mostrar()
