
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


def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)


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


def radix_sort(lista):
    if any(numero < 0 for numero in lista):
        raise ValueError("Radix Sort no acepta números negativos.")

    resultado = lista.copy()

    if not resultado:
        return resultado

    maximo = max(resultado)
    exp = 1

    while maximo // exp > 0:
        salida = [0] * len(resultado)
        conteo = [0] * 10

        for numero in resultado:
            digito = (numero // exp) % 10
            conteo[digito] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        for i in range(len(resultado) - 1, -1, -1):
            digito = (resultado[i] // exp) % 10
            salida[conteo[digito] - 1] = resultado[i]
            conteo[digito] -= 1

        resultado = salida
        exp *= 10

    return resultado


def pedir_numeros():
    """Pide la cantidad de números y los números. Regresa la lista o None."""
    cantidad = int(input("¿Cuántos números deseas ingresar? "))

    if cantidad <= 0:
        print("Ingresa una cantidad mayor que cero.")
        return None

    numeros = []
    for i in range(cantidad):
        numero = int(input(f"Número {i + 1}: "))
        numeros.append(numero)

    return numeros


METODOS = {
    "1": ("SHELL SORT", shell_sort),
    "2": ("QUICKSORT", quicksort),
    "3": ("HEAPSORT", heapsort),
    "4": ("RADIX SORT", radix_sort),
}


def main():
    while True:
        print("\n===== MÉTODOS DE ORDENAMIENTO =====")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion in METODOS:
            nombre, funcion = METODOS[opcion]
            print(f"\n--- {nombre} ---")

            try:
                numeros = pedir_numeros()

                if numeros is None:
                    continue

                print("Lista original:", numeros)

                print("Lista ordenada:", funcion(numeros.copy()))

            except ValueError as error:
                mensaje = str(error)
                if "invalid literal" in mensaje:
                    print("Ingresa solamente números enteros.")
                else:
                    print("Error:", mensaje)

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()