
def heapify(lista, n, i):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda

    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha

    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)


def heapsort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)

    return lista


while True:
    print("\n--- HEAPSORT ---")
    print("1. Ordenar números")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        try:
            cantidad = int(input("¿Cuántos números deseas ingresar? "))

            if cantidad <= 0:
                print("Ingresa una cantidad mayor que cero.")
                continue

            numeros = []

            for i in range(cantidad):
                numero = int(input(f"Número {i + 1}: "))
                numeros.append(numero)

            print("Lista original:", numeros)
            print("Lista ordenada:", heapsort(numeros.copy()))

        except ValueError:
            print("Ingresa solamente números enteros.")

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
