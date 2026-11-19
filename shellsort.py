
def shell_sort(lista):
    n = len(lista)
    salto = n // 2

    while salto > 0:
        for i in range(salto, n):
            temporal = lista[i]
            j = i

            while j >= salto and lista[j - salto] > temporal:
                lista[j] = lista[j - salto]
                j -= salto

            lista[j] = temporal

        salto //= 2

    return lista


while True:
    print("\n--- SHELL SORT ---")
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
            print("Lista ordenada:", shell_sort(numeros.copy()))

        except ValueError:
            print("Ingresa solamente números enteros.")

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
