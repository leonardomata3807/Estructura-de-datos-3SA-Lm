
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)


while True:
    print("\n--- QUICKSORT ---")
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
            print("Lista ordenada:", quicksort(numeros))

        except ValueError:
            print("Ingresa solamente números enteros.")

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
