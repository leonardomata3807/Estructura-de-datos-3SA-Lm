
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None


def insertar_inicio(p, dato):
    q = Nodo(dato)
    q.liga = p
    return q


def insertar_final(p, dato):
    q = Nodo(dato)

    if p is None:
        return q

    aux = p
    while aux.liga is not None:
        aux = aux.liga

    aux.liga = q
    return p


def insertar_posicion(p, dato, posicion):
    if posicion < 1:
        print("Posicion no valida")
        return p

    if posicion == 1:
        return insertar_inicio(p, dato)

    aux = p
    contador = 1

    while aux is not None and contador < posicion - 1:
        aux = aux.liga
        contador += 1

    if aux is None:
        print("Posicion fuera de la lista")
        return p

    q = Nodo(dato)
    q.liga = aux.liga
    aux.liga = q
    return p


def buscar(p, dato):
    posicion = 1

    while p is not None:
        if p.dato == dato:
            print("Dato encontrado en la posicion", posicion)
            return

        p = p.liga
        posicion += 1

    print("Dato no encontrado")


def eliminar(p, dato):
    if p is None:
        print("La lista esta vacia")
        return p

    if p.dato == dato:
        print("Dato eliminado")
        return p.liga

    aux = p

    while aux.liga is not None:
        if aux.liga.dato == dato:
            aux.liga = aux.liga.liga
            print("Dato eliminado")
            return p

        aux = aux.liga

    print("Dato no encontrado")
    return p


def mostrar(p):
    if p is None:
        print("La lista esta vacia")
        return

    while p is not None:
        print(p.dato, end=" -> ")
        p = p.liga

    print("NIL")


def contar(p):
    cantidad = 0

    while p is not None:
        cantidad += 1
        p = p.liga

    print("Cantidad de nodos:", cantidad)


inicio = None
opcion = 0

while opcion != 8:
    print("\n--- LISTA SIMPLEMENTE LIGADA ---")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Insertar en una posicion")
    print("4. Buscar un numero")
    print("5. Eliminar un numero")
    print("6. Mostrar lista")
    print("7. Contar nodos")
    print("8. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        dato = int(input("Ingresa un numero: "))
        inicio = insertar_inicio(inicio, dato)

    elif opcion == 2:
        dato = int(input("Ingresa un numero: "))
        inicio = insertar_final(inicio, dato)

    elif opcion == 3:
        dato = int(input("Ingresa un numero: "))
        posicion = int(input("Ingresa la posicion: "))
        inicio = insertar_posicion(inicio, dato, posicion)

    elif opcion == 4:
        dato = int(input("Numero a buscar: "))
        buscar(inicio, dato)

    elif opcion == 5:
        dato = int(input("Numero a eliminar: "))
        inicio = eliminar(inicio, dato)

    elif opcion == 6:
        mostrar(inicio)

    elif opcion == 7:
        contar(inicio)

    elif opcion == 8:
        print("Programa terminado")

    else:
        print("Opcion no valida")
